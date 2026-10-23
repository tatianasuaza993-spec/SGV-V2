"""
Módulo: enums.py
Descripción: Enumeraciones del dominio y helper para guardarlas como texto con restricción.
¿Para qué? Tener una sola definición de roles y estados, validada también en la base de datos.
¿Impacto? Sin restricción en la base, un valor inválido podría guardarse y romper las reglas.
"""

import enum

from sqlalchemy import Enum


class Role(enum.StrEnum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"


class DocumentType(enum.StrEnum):
    CC = "CC"
    TI = "TI"
    CE = "CE"
    PPT = "PPT"


class ElectionStatus(enum.StrEnum):
    PENDING = "pending"
    ACTIVE = "active"
    FINISHED = "finished"


class CandidacyStatus(enum.StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"


def enum_column(enum_cls: type[enum.StrEnum], name: str) -> Enum:
    """Columna de texto (VARCHAR) con CHECK que solo admite los valores del enum.

    ¿Qué? Evita enums nativos de PostgreSQL, que son difíciles de migrar.
    ¿Impacto? La base rechaza cualquier valor que no esté en el enum.
    """
    return Enum(
        enum_cls,
        name=name,
        native_enum=False,
        create_constraint=True,
        length=20,
        values_callable=lambda members: [member.value for member in members],
    )
