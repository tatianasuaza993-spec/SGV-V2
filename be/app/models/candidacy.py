"""
Módulo: candidacy.py
Descripción: Modelo `Candidacy` (candidatura) con su estado de revisión.
¿Para qué? Registrar quién se postula a qué cargo y si fue aprobado (RF-017, 022, 033-036).
¿Impacto? Antes no existía estado ni aprobación y retirar una candidatura la borraba (H12).
Ahora «retirada» es un estado y solo se vota por candidaturas aprobadas.
"""

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, IdMixin, TimestampMixin
from app.models.enums import CandidacyStatus, enum_column


class Candidacy(IdMixin, TimestampMixin, Base):
    __tablename__ = "candidacies"
    __table_args__ = (
        UniqueConstraint("user_id", "position_id", name="uq_candidacies_user_position"),
        UniqueConstraint("position_id", "number", name="uq_candidacies_position_number"),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), index=True, nullable=False
    )
    election_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("elections.id", ondelete="CASCADE"), index=True, nullable=False
    )
    position_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("positions.id", ondelete="CASCADE"), index=True, nullable=False
    )
    number: Mapped[int | None] = mapped_column(Integer)
    slogan: Mapped[str | None] = mapped_column(String(200))
    proposal: Mapped[str | None] = mapped_column(Text)
    photo_url: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[CandidacyStatus] = mapped_column(
        enum_column(CandidacyStatus, "candidacy_status"),
        server_default=text("'pending'"),
        default=CandidacyStatus.PENDING,
        nullable=False,
    )
    review_notes: Mapped[str | None] = mapped_column(Text)
    reviewed_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"))
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
