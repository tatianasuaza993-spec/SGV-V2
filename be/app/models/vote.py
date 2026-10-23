"""
Módulo: vote.py
Descripción: Modelos `Vote` (el voto, anónimo) y `VoteRecord` (la constancia de participación).
¿Para qué? Garantizar el secreto del sufragio y un solo voto por persona y cargo (RF-027).
¿Impacto? Este módulo es el corazón de la confianza en la elección:
  - H2: `UNIQUE(user_id, position_id)` en `vote_records` lo hace cumplir la base de datos, no una
    consulta previa que dos peticiones simultáneas podrían esquivar.
  - H3: `votes` no guarda usuario ni fecha y su id es un UUID aleatorio; antes ambas tablas
    compartían la misma fecha exacta y ids consecutivos, y se podían unir.
Límite conocido: quien tenga acceso de administrador a la base y observe las inserciones en
tiempo real podría correlacionarlas; el sistema protege los datos en reposo.
"""

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, IdMixin


class Vote(IdMixin, Base):
    """Voto anónimo. `candidacy_id` nulo significa voto en blanco."""

    __tablename__ = "votes"

    election_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("elections.id"), index=True, nullable=False
    )
    position_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("positions.id"), index=True, nullable=False
    )
    candidacy_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("candidacies.id"), index=True
    )


class VoteRecord(IdMixin, Base):
    """Constancia de que una persona votó en un cargo (sin decir por quién)."""

    __tablename__ = "vote_records"
    __table_args__ = (
        UniqueConstraint("user_id", "position_id", name="uq_vote_records_user_position"),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), index=True, nullable=False
    )
    election_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("elections.id"), index=True, nullable=False
    )
    position_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("positions.id"), index=True, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
