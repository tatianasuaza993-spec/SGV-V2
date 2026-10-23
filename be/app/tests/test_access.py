"""
Módulo: test_access.py
Descripción: Pruebas de la guardia de aislamiento por institución (H1). No usan base de datos.
¿Para qué? Demostrar que una persona no puede actuar sobre recursos de otra institución.
¿Impacto? Es la regla que evita que un administrador de un colegio borre una elección ajena.
"""

import uuid

import pytest

from app.exceptions import ForbiddenError
from app.models import DocumentType, Role, User
from app.services.access import require_same_institution


def _user(institution_id: uuid.UUID | None) -> User:
    return User(
        institution_id=institution_id,
        document_type=DocumentType.CC,
        document_number="1",
        first_name="A",
        last_name="B",
        email="a@example.com",
        hashed_password="x",
        role=Role.ADMIN,
    )


def test_same_institution_is_allowed() -> None:
    institution_id = uuid.uuid4()
    require_same_institution(_user(institution_id), institution_id)


def test_other_institution_is_forbidden() -> None:
    with pytest.raises(ForbiddenError):
        require_same_institution(_user(uuid.uuid4()), uuid.uuid4())


def test_user_without_institution_is_forbidden() -> None:
    with pytest.raises(ForbiddenError):
        require_same_institution(_user(None), uuid.uuid4())
