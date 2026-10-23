"""
Módulo: test_main.py
Descripción: Pruebas de la aplicación: ruta de salud y manejo de errores de dominio.
¿Para qué? Verificar que cada excepción responde con su propio código HTTP (H16).
¿Impacto? Sin esto, cambiar una palabra de un mensaje podía cambiar el código de estado.
"""

import pytest
from fastapi.testclient import TestClient

from app.exceptions import AlreadyVotedError, ConflictError, ForbiddenError, NotFoundError
from app.main import create_app


@pytest.fixture
def client() -> TestClient:
    app = create_app()

    @app.get("/boom/{kind}")
    def boom(kind: str) -> None:
        errors = {
            "conflict": ConflictError(),
            "voted": AlreadyVotedError(),
            "forbidden": ForbiddenError(),
            "missing": NotFoundError("Election not found"),
        }
        raise errors[kind]

    return TestClient(app)


def test_health_is_ok(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.parametrize(
    ("kind", "status", "code"),
    [
        ("conflict", 409, "conflict"),
        ("voted", 409, "already_voted"),
        ("forbidden", 403, "forbidden"),
        ("missing", 404, "not_found"),
    ],
)
def test_domain_errors_carry_their_own_status(
    client: TestClient, kind: str, status: int, code: str
) -> None:
    response = client.get(f"/boom/{kind}")
    assert response.status_code == status
    assert response.json()["code"] == code
