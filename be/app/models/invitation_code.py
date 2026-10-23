"""
Módulo: invitation_code.py
Descripción: Modelo `InvitationCode` (RF-006 y RF-018).
¿Para qué? Vincular administradores y docentes a una institución con un código controlado.
¿Impacto? Antes el rol salía de comparar contra un código fijo escrito en los seeds (H6): quien
lo conociera era administrador para siempre. Ahora hay vigencia, usos y se puede desactivar.
"""

import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, IdMixin
from app.models.enums import Role, enum_column


class InvitationCode(IdMixin, Base):
    __tablename__ = "invitation_codes"
    __table_args__ = (
        CheckConstraint("role IN ('admin', 'teacher')", name="role_allowed"),
        CheckConstraint("max_uses >= 1", name="max_uses_positive"),
        CheckConstraint("uses >= 0 AND uses <= max_uses", name="uses_within_limit"),
    )

    institution_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("institutions.id"), index=True, nullable=False
    )
    code: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    role: Mapped[Role] = mapped_column(enum_column(Role, "role"), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    max_uses: Mapped[int] = mapped_column(
        Integer, server_default=text("1"), default=1, nullable=False
    )
    uses: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, server_default=text("true"), default=True, nullable=False
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
