"""
Módulo: test_institutions_api.py
Descripción: Pruebas de creación de institución y códigos de invitación (RF-006, RF-018).
¿Para qué? Verificar los hallazgos H6 (códigos controlados) y H1 (aislamiento por institución).
¿Impacto? Garantizan que un código fijo ya no convierte a cualquiera en administrador y que un
administrador no toca los códigos de otro colegio.
"""

from datetime import UTC, datetime, timedelta

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models import InvitationCode, Role
from app.tests.factories import make_institution

PASSWORD = "Clave-Segura1"
INSTITUTION = {"name": "Colegio Feliz", "address": "Calle 10 # 5-20"}


def _signup(client: TestClient, email: str, role: str, number: str) -> dict[str, str]:
    client.post(
        "/api/v1/auth/register",
        json={
            "first_name": "Persona",
            "last_name": "Prueba",
            "email": email,
            "document_type": "CC",
            "document_number": number,
            "password": PASSWORD,
            "role": role,
        },
    )
    tokens = client.post("/api/v1/auth/login", json={"email": email, "password": PASSWORD}).json()
    return {"Authorization": f"Bearer {tokens['access_token']}"}


def _join(client: TestClient, headers: dict[str, str], code: str):
    return client.post("/api/v1/institutions/join", json={"code": code}, headers=headers)


def _admin_with_institution(client: TestClient, email: str, number: str, name: str):
    headers = _signup(client, email, "admin", number)
    response = client.post(
        "/api/v1/institutions", json={**INSTITUTION, "name": name}, headers=headers
    )
    assert response.status_code == 201
    return headers


def test_admin_creates_institution_and_is_linked_to_it(client: TestClient) -> None:
    headers = _signup(client, "admin@example.com", "admin", "1")
    response = client.post("/api/v1/institutions", json=INSTITUTION, headers=headers)
    assert response.status_code == 201
    me = client.get("/api/v1/users/me", headers=headers).json()
    assert me["institution_id"] == response.json()["id"]


def test_teacher_cannot_create_institution(client: TestClient) -> None:
    headers = _signup(client, "docente@example.com", "teacher", "2")
    assert client.post("/api/v1/institutions", json=INSTITUTION, headers=headers).status_code == 403


def test_admin_cannot_create_a_second_institution(client: TestClient) -> None:
    headers = _admin_with_institution(client, "admin@example.com", "1", "Uno")
    assert client.post("/api/v1/institutions", json=INSTITUTION, headers=headers).status_code == 409


def test_unauthenticated_cannot_create_codes(client: TestClient) -> None:
    assert client.post("/api/v1/invitation-codes", json={"role": "teacher"}).status_code == 401


def test_teacher_joins_with_valid_code(client: TestClient) -> None:
    admin = _admin_with_institution(client, "admin@example.com", "1", "Uno")
    code = client.post("/api/v1/invitation-codes", json={"role": "teacher"}, headers=admin).json()
    teacher = _signup(client, "docente@example.com", "teacher", "2")
    response = _join(client, teacher, code["code"])
    assert response.status_code == 200
    me = client.get("/api/v1/users/me", headers=teacher).json()
    assert me["institution_id"] == code["institution_id"]


def test_code_cannot_be_reused_beyond_its_limit(client: TestClient) -> None:
    admin = _admin_with_institution(client, "admin@example.com", "1", "Uno")
    code = client.post(
        "/api/v1/invitation-codes", json={"role": "teacher", "max_uses": 1}, headers=admin
    ).json()
    first = _signup(client, "uno@example.com", "teacher", "2")
    second = _signup(client, "dos@example.com", "teacher", "3")
    assert _join(client, first, code["code"]).status_code == 200
    assert _join(client, second, code["code"]).status_code == 422


def test_code_for_another_role_is_rejected(client: TestClient) -> None:
    admin = _admin_with_institution(client, "admin@example.com", "1", "Uno")
    code = client.post("/api/v1/invitation-codes", json={"role": "admin"}, headers=admin).json()
    teacher = _signup(client, "docente@example.com", "teacher", "2")
    response = _join(client, teacher, code["code"])
    assert response.status_code == 422


def test_unknown_code_is_rejected_with_a_generic_message(client: TestClient) -> None:
    teacher = _signup(client, "docente@example.com", "teacher", "2")
    response = _join(client, teacher, "ZZZZZZZZZZ")
    assert response.status_code == 422
    assert response.json()["detail"] == "Invalid or expired invitation code"


def test_expired_code_is_rejected(client: TestClient, db_session: Session) -> None:
    institution = make_institution(db_session)
    db_session.add(
        InvitationCode(
            institution_id=institution.id,
            code="EXPIRED123",
            role=Role.TEACHER,
            expires_at=datetime.now(UTC) - timedelta(days=1),
        )
    )
    db_session.commit()
    teacher = _signup(client, "docente@example.com", "teacher", "2")
    response = _join(client, teacher, "EXPIRED123")
    assert response.status_code == 422


def test_deactivated_code_is_rejected(client: TestClient) -> None:
    admin = _admin_with_institution(client, "admin@example.com", "1", "Uno")
    code = client.post("/api/v1/invitation-codes", json={"role": "teacher"}, headers=admin).json()
    off = client.post(f"/api/v1/invitation-codes/{code['id']}/deactivate", headers=admin)
    assert off.status_code == 200
    teacher = _signup(client, "docente@example.com", "teacher", "2")
    response = _join(client, teacher, code["code"])
    assert response.status_code == 422


def test_admin_cannot_deactivate_codes_of_another_institution(client: TestClient) -> None:
    """H1: el rol de administrador no basta; también debe ser de la misma institución."""
    admin_a = _admin_with_institution(client, "a@example.com", "1", "Colegio A")
    admin_b = _admin_with_institution(client, "b@example.com", "2", "Colegio B")
    code = client.post("/api/v1/invitation-codes", json={"role": "teacher"}, headers=admin_a).json()
    response = client.post(f"/api/v1/invitation-codes/{code['id']}/deactivate", headers=admin_b)
    assert response.status_code == 403


def test_admin_lists_only_codes_of_their_institution(client: TestClient) -> None:
    admin_a = _admin_with_institution(client, "a@example.com", "1", "Colegio A")
    admin_b = _admin_with_institution(client, "b@example.com", "2", "Colegio B")
    client.post("/api/v1/invitation-codes", json={"role": "teacher"}, headers=admin_a)
    assert len(client.get("/api/v1/invitation-codes", headers=admin_a).json()) == 1
    assert client.get("/api/v1/invitation-codes", headers=admin_b).json() == []
