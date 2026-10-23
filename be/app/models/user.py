"""
Módulo: user.py
Descripción: Modelos `User` y `PasswordResetToken`.
¿Para qué? Representar a las personas del sistema y la recuperación de contraseña (RF-004).
¿Impacto? `institution_id` es opcional porque administradores y docentes se vinculan después con
un código de invitación (RF-006); los estudiantes los crea la institución.
"""

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, IdMixin, TimestampMixin
from app.models.enums import DocumentType, Role, enum_column


class User(IdMixin, TimestampMixin, Base):
    __tablename__ = "users"

    institution_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("institutions.id"), index=True
    )
    document_type: Mapped[DocumentType] = mapped_column(
        enum_column(DocumentType, "document_type"), nullable=False
    )
    document_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    course: Mapped[str | None] = mapped_column(String(20))
    avatar_url: Mapped[str | None] = mapped_column(String(255))
    role: Mapped[Role] = mapped_column(enum_column(Role, "role"), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, server_default=text("true"), default=True, nullable=False
    )
    # Límite de intentos de inicio de sesión (H10)
    failed_login_attempts: Mapped[int] = mapped_column(
        Integer, server_default=text("0"), default=0, nullable=False
    )
    locked_until: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class PasswordResetToken(IdMixin, Base):
    """Token de recuperación de contraseña. Se guarda su hash, nunca el token (RF-004)."""

    __tablename__ = "password_reset_tokens"

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    token_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    used_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


__all__ = ["PasswordResetToken", "User"]
