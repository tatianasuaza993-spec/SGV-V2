"""
Módulo: institution.py
Descripción: Modelo `Institution` (institución educativa).
¿Para qué? Agrupar usuarios y elecciones; es la frontera de aislamiento de los datos (H1).
¿Impacto? Sin institución como frontera, una persona podría actuar sobre elecciones ajenas.
"""

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, IdMixin, TimestampMixin


class Institution(IdMixin, TimestampMixin, Base):
    __tablename__ = "institutions"

    name: Mapped[str] = mapped_column(String(256), nullable=False)
    nit: Mapped[str | None] = mapped_column(String(15), unique=True)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(15))
    email: Mapped[str | None] = mapped_column(String(256))
    description: Mapped[str | None] = mapped_column(Text)
