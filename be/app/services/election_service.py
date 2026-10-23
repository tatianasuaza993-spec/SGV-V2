"""
Módulo: election_service.py
Descripción: Reglas de negocio de las elecciones (RF-009, RF-019, RF-020).
¿Para qué? Crear, consultar, editar, eliminar y cambiar de estado una elección.
¿Impacto? Aquí se implementan las reglas que antes faltaban (H4): estado inicial «pending»,
transiciones válidas, y bloqueo de cambios críticos si la elección está en curso o tiene votos.
Toda operación compara la institución (H1) con `require_same_institution`.
"""

import uuid
from datetime import UTC, datetime

from sqlalchemy import exists, select
from sqlalchemy.orm import Session

from app.exceptions import (
    ConflictError,
    ForbiddenError,
    InvalidStateTransitionError,
    NotFoundError,
    ValidationRuleError,
)
from app.models import Election, ElectionStatus, Position, User, Vote, VoteRecord
from app.schemas.election import ElectionCreate, ElectionUpdate
from app.services.access import require_same_institution

# Única secuencia permitida: pendiente → activa → finalizada
ALLOWED_TRANSITIONS: dict[ElectionStatus, set[ElectionStatus]] = {
    ElectionStatus.PENDING: {ElectionStatus.ACTIVE},
    ElectionStatus.ACTIVE: {ElectionStatus.FINISHED},
    ElectionStatus.FINISHED: set(),
}


def get_election_for_user(db: Session, user: User, election_id: uuid.UUID) -> Election:
    """Busca la elección y verifica que sea de la institución del usuario (H1)."""
    election = db.get(Election, election_id)
    if election is None:
        raise NotFoundError("Election not found")
    require_same_institution(user, election.institution_id)
    return election


def has_votes(db: Session, election_id: uuid.UUID) -> bool:
    """¿Ya hay votos o constancias de participación en esta elección?"""
    has_vote = db.scalar(select(exists().where(Vote.election_id == election_id)))
    has_record = db.scalar(select(exists().where(VoteRecord.election_id == election_id)))
    return bool(has_vote or has_record)


def _validate_window(starts_at: datetime, ends_at: datetime, now: datetime) -> None:
    if ends_at <= starts_at:
        raise ValidationRuleError("The end date must be after the start date")
    if ends_at <= now:
        raise ValidationRuleError("The end date must be in the future")


def _ensure_critical_changes_allowed(db: Session, election: Election) -> None:
    if election.status != ElectionStatus.PENDING:
        raise ConflictError("Dates and positions can only change while the election is pending")
    if has_votes(db, election.id):
        raise ConflictError("The election already has votes")


def list_elections(db: Session, user: User) -> list[Election]:
    if user.institution_id is None:
        return []
    return list(
        db.scalars(
            select(Election)
            .where(Election.institution_id == user.institution_id)
            .order_by(Election.starts_at.desc())
        )
    )


def create_election(
    db: Session, admin: User, data: ElectionCreate, now: datetime | None = None
) -> Election:
    if admin.institution_id is None:
        raise ForbiddenError("Create or join an institution first")
    _validate_window(data.starts_at, data.ends_at, now or datetime.now(UTC))
    election = Election(
        institution_id=admin.institution_id,
        title=data.title.strip(),
        description=data.description,
        starts_at=data.starts_at,
        ends_at=data.ends_at,
        positions=[Position(name=name) for name in data.positions],
    )
    db.add(election)
    db.commit()
    return election


def update_election(
    db: Session,
    user: User,
    election_id: uuid.UUID,
    data: ElectionUpdate,
    now: datetime | None = None,
) -> Election:
    election = get_election_for_user(db, user, election_id)
    changes = data.model_dump(exclude_unset=True)
    if {"starts_at", "ends_at", "positions"} & changes.keys():
        _ensure_critical_changes_allowed(db, election)
        starts_at = changes.get("starts_at") or election.starts_at
        ends_at = changes.get("ends_at") or election.ends_at
        _validate_window(starts_at, ends_at, now or datetime.now(UTC))
        election.starts_at = starts_at
        election.ends_at = ends_at
        if changes.get("positions"):
            existing = {position.name: position for position in election.positions}
            election.positions[:] = [
                existing.get(name) or Position(name=name) for name in changes["positions"]
            ]
    if changes.get("title"):
        election.title = changes["title"].strip()
    if "description" in changes:
        election.description = changes["description"]
    db.commit()
    return election


def delete_election(db: Session, user: User, election_id: uuid.UUID) -> None:
    election = get_election_for_user(db, user, election_id)
    if election.status != ElectionStatus.PENDING:
        raise ConflictError("Only pending elections can be deleted")
    if has_votes(db, election.id):
        raise ConflictError("The election already has votes")
    db.delete(election)
    db.commit()


def change_status(
    db: Session, user: User, election_id: uuid.UUID, new_status: ElectionStatus
) -> Election:
    election = get_election_for_user(db, user, election_id)
    if new_status not in ALLOWED_TRANSITIONS[election.status]:
        raise InvalidStateTransitionError(
            f"An election cannot go from {election.status.value} to {new_status.value}"
        )
    if new_status == ElectionStatus.ACTIVE and not election.positions:
        raise ValidationRuleError("An election needs at least one position to start")
    election.status = new_status
    db.commit()
    return election
