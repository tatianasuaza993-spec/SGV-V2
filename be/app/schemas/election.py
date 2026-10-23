"""
Módulo: election.py (schemas)
Descripción: Modelos Pydantic de elecciones y cargos.
¿Para qué? Validar fechas (con zona horaria, H8) y la lista de cargos.
¿Impacto? Una fecha sin zona horaria se rechaza: el servidor de despliegue puede estar en UTC y
desfasar la votación 5 horas respecto de Colombia.
"""

import uuid

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, field_validator

from app.models import ElectionStatus


def _clean_positions(names: list[str]) -> list[str]:
    cleaned = [name.strip() for name in names]
    if any(not name or len(name) > 100 for name in cleaned):
        raise ValueError("Each position needs a name of 1 to 100 characters")
    if len({name.lower() for name in cleaned}) != len(cleaned):
        raise ValueError("Position names must be unique")
    return cleaned


class PositionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str


class ElectionCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str | None = None
    starts_at: AwareDatetime
    ends_at: AwareDatetime
    positions: list[str] = Field(min_length=1, max_length=20)

    _check_positions = field_validator("positions")(_clean_positions)


class ElectionUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=150)
    description: str | None = None
    starts_at: AwareDatetime | None = None
    ends_at: AwareDatetime | None = None
    positions: list[str] | None = Field(default=None, min_length=1, max_length=20)

    @field_validator("positions")
    @classmethod
    def _check_positions(cls, value: list[str] | None) -> list[str] | None:
        return None if value is None else _clean_positions(value)


class ElectionStatusChange(BaseModel):
    status: ElectionStatus


class ElectionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    institution_id: uuid.UUID
    title: str
    description: str | None
    starts_at: AwareDatetime
    ends_at: AwareDatetime
    status: ElectionStatus
    results_published: bool
    positions: list[PositionResponse]
