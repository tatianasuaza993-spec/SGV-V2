"""
Módulo: security.py
Descripción: Hash de contraseñas con bcrypt, tokens JWT y generación de códigos aleatorios.
¿Para qué? Concentrar las funciones de seguridad que usa todo el sistema (RT-004, RT-005).
¿Impacto? Es la base de la autenticación: un error aquí compromete a todos los usuarios.
"""

import hashlib
import secrets
import uuid
from datetime import UTC, datetime, timedelta
from typing import Any, Literal

import bcrypt
import jwt

from app.config import get_settings
from app.exceptions import UnauthorizedError

TokenType = Literal["access", "refresh"]

# Alfabeto sin caracteres ambiguos (0/O, 1/I) para códigos que una persona debe transcribir
_CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"


def hash_password(plain_password: str) -> str:
    """Hashea una contraseña con bcrypt. Nunca se guarda en texto plano (RS-003)."""
    return bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compara una contraseña contra su hash. Un hash inválido cuenta como «no coincide»."""
    try:
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
    except ValueError:
        return False


def _create_token(
    user_id: uuid.UUID, role: str, token_type: TokenType, expires_delta: timedelta
) -> str:
    now = datetime.now(UTC)
    settings = get_settings()
    claims: dict[str, Any] = {
        "sub": str(user_id),
        "role": role,
        "type": token_type,
        "iat": now,
        "exp": now + expires_delta,
    }
    return jwt.encode(claims, settings.secret_key, algorithm=settings.algorithm)


def create_access_token(
    user_id: uuid.UUID, role: str, expires_delta: timedelta | None = None
) -> str:
    """Token de acceso de corta duración (por defecto 15 minutos)."""
    settings = get_settings()
    delta = expires_delta or timedelta(minutes=settings.access_token_expire_minutes)
    return _create_token(user_id, role, "access", delta)


def create_refresh_token(
    user_id: uuid.UUID, role: str, expires_delta: timedelta | None = None
) -> str:
    """Token de renovación de larga duración (por defecto 7 días)."""
    settings = get_settings()
    delta = expires_delta or timedelta(days=settings.refresh_token_expire_days)
    return _create_token(user_id, role, "refresh", delta)


def decode_token(token: str, expected_type: TokenType) -> dict[str, Any]:
    """Valida firma, vigencia y tipo del token.

    ¿Impacto? Sin comprobar el tipo, un token de renovación serviría como token de acceso.
    El mensaje de error es genérico para no dar pistas a un atacante.
    """
    settings = get_settings()
    try:
        claims = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except jwt.InvalidTokenError as error:
        raise UnauthorizedError("Invalid or expired token") from error
    if claims.get("type") != expected_type or "sub" not in claims:
        raise UnauthorizedError("Invalid or expired token")
    return claims


def hash_token(token: str) -> str:
    """Hash SHA-256 de un token de un solo uso (se guarda el hash, nunca el token)."""
    return hashlib.sha256(token.encode()).hexdigest()


def generate_invitation_code(length: int = 10) -> str:
    """Código aleatorio criptográficamente seguro para invitaciones (H6)."""
    return "".join(secrets.choice(_CODE_ALPHABET) for _ in range(length))


__all__ = [
    "create_access_token",
    "create_refresh_token",
    "decode_token",
    "generate_invitation_code",
    "hash_password",
    "hash_token",
    "verify_password",
]
