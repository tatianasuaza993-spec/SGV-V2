"""
Módulo: dependencies.py
Descripción: Dependencias de FastAPI para identificar al usuario y exigir roles.
¿Para qué? Que cada ruta protegida obtenga al usuario autenticado y valide su rol en una línea.
¿Impacto? Exigir solo el rol no basta (H1): después hay que comparar la institución con
`require_same_institution`. Estas dependencias resuelven la parte de identidad y rol.
"""

import uuid

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.exceptions import ForbiddenError, UnauthorizedError
from app.models import Role, User
from app.utils.security import decode_token

# auto_error=False: la falta de token la reportamos nosotros como 401 (no el 403 por defecto)
_bearer = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(_bearer),
    db: Session = Depends(get_db),
) -> User:
    """Devuelve el usuario dueño del token de acceso, o responde 401."""
    if credentials is None:
        raise UnauthorizedError("Not authenticated")
    claims = decode_token(credentials.credentials, "access")
    try:
        user_id = uuid.UUID(claims["sub"])
    except ValueError as error:
        raise UnauthorizedError("Invalid or expired token") from error
    user = db.get(User, user_id)
    if user is None or not user.is_active:
        raise UnauthorizedError("Invalid or expired token")
    return user


def require_roles(*roles: Role):
    """Fábrica de dependencias: exige que el usuario tenga alguno de los roles dados."""

    def checker(user: User = Depends(get_current_user)) -> User:
        if user.role not in roles:
            raise ForbiddenError()
        return user

    return checker
