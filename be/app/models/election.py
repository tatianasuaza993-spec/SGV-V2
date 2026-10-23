"""
Módulo: election.py
Descripción: Modelos `Election` y `Position` (RF-009).
¿Para qué? Describir una elección, sus cargos y su estado.
¿Impacto? El estado nace en «pending» (antes nacía «activa» por el valor por defecto, H4) y la
base impide que una elección termine antes de empezar.
"""

import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    String,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, IdMixin, TimestampMixin
from app.models.enums import ElectionStatus, enum_column


class Election(IdMixin, TimestampMixin, Base):
    __tablename__ = "elections"
    __table_args__ = (CheckConstraint("ends_at > starts_at", name="ends_after_start"),)

    institution_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("institutions.id"), index=True, nullable=False
    )
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    ends_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[ElectionStatus] = mapped_column(
        enum_column(ElectionStatus, "election_status"),
        server_default=text("'pending'"),
        default=ElectionStatus.PENDING,
        nullable=False,
    )
    # El administrador decide cuándo se publican los resultados (H5, RF-015)
    results_published: Mapped[bool] = mapped_column(
        Boolean, server_default=text("false"), default=False, nullable=False
    )
    # Los cargos se borran en cascada desde la base de datos (ON DELETE CASCADE); si hay votos,
    # la base impide borrar la elección (H4).
    positions: Mapped[list["Position"]] = relationship(
        cascade="all, delete-orphan",
        passive_deletes=True,
        order_by="Position.name",
        lazy="selectin",
    )


class Position(IdMixin, Base):
    """Cargo que se elige dentro de una elección (personero, contralor, representante...)."""

    __tablename__ = "positions"
    __table_args__ = (UniqueConstraint("election_id", "name", name="uq_positions_election_name"),)

    election_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("elections.id", ondelete="CASCADE"), index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
