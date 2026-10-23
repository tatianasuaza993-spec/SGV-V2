"""
Módulo: auth_service.py
Descripción: Lógica de negocio de registro, inicio de sesión, tokens e instituciones.
¿Para qué? Mantener las reglas fuera de los routers (que solo manejan HTTP).
¿Impacto? Aquí viven H10 (mensaje único y bloqueo por intentos) y H6 (códigos de invitación
con vigencia y usos). Un error en este módulo abre o cierra el acceso al sistema.
"""

import uuid
from datetime import UTC, datetime, timedelta
from functools import lru_cache

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.exceptions import (
    ConflictError,
    ForbiddenError,
    NotFoundError,
    UnauthorizedError,
    ValidationRuleError,
)
from app.models import Institution, InvitationCode, Role, User
from app.schemas.auth import (
    InstitutionCreate,
    InvitationCodeCreate,
    RegisterRequest,
    TokenResponse,
)
from app.services.access import require_same_institution
from app.utils.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    generate_invitation_code,
    hash_password,
    verify_password,
)

MAX_FAILED_ATTEMPTS = 5
LOCK_MINUTES = 15
# Un único mensaje para correo inexistente, contraseña incorrecta, cuenta bloqueada o inactiva
# (H10): quien ataca no puede saber si una cuenta existe.
INVALID_CREDENTIALS = "Invalid email or password"
INVALID_CODE = "Invalid or expired invitation code"


@lru_cache
def _dummy_hash() -> str:
    """Hash de relleno para que el tiempo de respuesta no delate si el correo existe."""
    return hash_password("Dummy-password-1")


def register_user(db: Session, data: RegisterRequest) -> User:
    """Crea una cuenta de administrador o docente sin institución (RF-002)."""
    email = data.email.lower()
    exists = db.scalar(
        select(User.id).where(
            (User.email == email) | (User.document_number == data.document_number)
        )
    )
    if exists is not None:
        raise ConflictError("Email or document number already registered")
    user = User(
        first_name=data.first_name.strip(),
        last_name=data.last_name.strip(),
        email=email,
        document_type=data.document_type,
        document_number=data.document_number.strip(),
        hashed_password=hash_password(data.password),
        role=Role(data.role),
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError as error:
        # Dos registros simultáneos pueden pasar la consulta previa: la base decide.
        db.rollback()
        raise ConflictError("Email or document number already registered") from error
    return user


def authenticate(db: Session, email: str, password: str, now: datetime | None = None) -> User:
    """Valida credenciales con mensaje único y bloqueo temporal tras varios fallos (H10)."""
    now = now or datetime.now(UTC)
    user = db.scalar(select(User).where(User.email == email.lower()))
    if user is None:
        verify_password(password, _dummy_hash())
        raise UnauthorizedError(INVALID_CREDENTIALS)
    if not user.is_active or (user.locked_until is not None and user.locked_until > now):
        raise UnauthorizedError(INVALID_CREDENTIALS)
    if not verify_password(password, user.hashed_password):
        user.failed_login_attempts += 1
        if user.failed_login_attempts >= MAX_FAILED_ATTEMPTS:
            user.locked_until = now + timedelta(minutes=LOCK_MINUTES)
            user.failed_login_attempts = 0
        db.commit()
        raise UnauthorizedError(INVALID_CREDENTIALS)
    user.failed_login_attempts = 0
    user.locked_until = None
    db.commit()
    return user


def issue_tokens(user: User) -> TokenResponse:
    return TokenResponse(
        access_token=create_access_token(user.id, user.role.value),
        refresh_token=create_refresh_token(user.id, user.role.value),
    )


def refresh_tokens(db: Session, refresh_token: str) -> TokenResponse:
    """Entrega un par de tokens nuevo a partir de un token de renovación válido."""
    claims = decode_token(refresh_token, "refresh")
    try:
        user = db.get(User, uuid.UUID(claims["sub"]))
    except ValueError as error:
        raise UnauthorizedError("Invalid or expired token") from error
    if user is None or not user.is_active:
        raise UnauthorizedError("Invalid or expired token")
    return issue_tokens(user)


def create_institution(db: Session, user: User, data: InstitutionCreate) -> Institution:
    """Un administrador sin institución crea la suya y queda vinculado a ella."""
    if user.role != Role.ADMIN:
        raise ForbiddenError("Only administrators can create an institution")
    if user.institution_id is not None:
        raise ConflictError("You already belong to an institution")
    institution = Institution(**data.model_dump())
    db.add(institution)
    try:
        db.flush()
    except IntegrityError as error:
        db.rollback()
        raise ConflictError("An institution with that NIT already exists") from error
    user.institution_id = institution.id
    db.commit()
    return institution


def create_invitation_code(
    db: Session, admin: User, data: InvitationCodeCreate, now: datetime | None = None
) -> InvitationCode:
    """Genera un código aleatorio con rol, vigencia y usos (RF-018, H6)."""
    if admin.institution_id is None:
        raise ForbiddenError("Create or join an institution first")
    now = now or datetime.now(UTC)
    for _ in range(5):
        invitation = InvitationCode(
            institution_id=admin.institution_id,
            code=generate_invitation_code(),
            role=Role(data.role),
            expires_at=now + timedelta(days=data.expires_in_days),
            max_uses=data.max_uses,
            created_by=admin.id,
        )
        try:
            with db.begin_nested():
                db.add(invitation)
                db.flush()
        except IntegrityError:
            continue  # colisión de código: se genera otro
        db.commit()
        return invitation
    raise ConflictError("Could not generate a unique code, try again")


def list_invitation_codes(db: Session, admin: User) -> list[InvitationCode]:
    if admin.institution_id is None:
        return []
    return list(
        db.scalars(
            select(InvitationCode)
            .where(InvitationCode.institution_id == admin.institution_id)
            .order_by(InvitationCode.created_at.desc())
        )
    )


def deactivate_invitation_code(db: Session, admin: User, code_id: uuid.UUID) -> InvitationCode:
    invitation = db.get(InvitationCode, code_id)
    if invitation is None:
        raise NotFoundError("Invitation code not found")
    require_same_institution(admin, invitation.institution_id)
    invitation.is_active = False
    db.commit()
    return invitation


def join_institution(
    db: Session, user: User, code: str, now: datetime | None = None
) -> Institution:
    """Vincula al usuario con una institución usando un código válido (RF-006)."""
    if user.role not in (Role.ADMIN, Role.TEACHER):
        raise ForbiddenError("Only administrators and teachers join with a code")
    if user.institution_id is not None:
        raise ConflictError("You already belong to an institution")
    now = now or datetime.now(UTC)
    invitation = db.scalar(
        select(InvitationCode).where(InvitationCode.code == code.strip().upper()).with_for_update()
    )
    if (
        invitation is None
        or not invitation.is_active
        or invitation.expires_at <= now
        or invitation.uses >= invitation.max_uses
        or invitation.role != user.role
    ):
        raise ValidationRuleError(INVALID_CODE)
    invitation.uses += 1
    user.institution_id = invitation.institution_id
    db.commit()
    institution = db.get(Institution, invitation.institution_id)
    assert institution is not None  # la llave foránea lo garantiza
    return institution
