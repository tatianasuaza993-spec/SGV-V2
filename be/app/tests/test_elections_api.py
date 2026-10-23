"""
Módulo: test_elections_api.py
Descripción: Pruebas de elecciones y cargos (RF-009, RF-019).
¿Para qué? Verificar las reglas de H4 (estados y bloqueos) y H1 (aislamiento por institución).
¿Impacto? Garantizan que una elección en curso o con votos no se pueda alterar ni borrar, y que
un colegio no pueda tocar las elecciones de otro.
"""

from datetime import UTC, datetime, timedelta

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models import ElectionStatus, Role, Vote
from app.tests.factories import (
    auth_headers,
    make_election,
    make_institution,
    make_position,
    make_user,
)

NOW = datetime.now(UTC)


def _payload(**overrides):
    payload = {
        "title": "Gobierno escolar 2026",
        "description": "Elección de representantes",
        "starts_at": (NOW + timedelta(days=1)).isoformat(),
        "ends_at": (NOW + timedelta(days=2)).isoformat(),
        "positions": ["Personero", "Contralor"],
    }
    payload.update(overrides)
    return payload


@pytest.fixture
def school(db_session: Session):
    institution = make_institution(db_session, "Colegio A")
    return {
        "institution": institution,
        "admin": make_user(db_session, institution, Role.ADMIN),
        "teacher": make_user(db_session, institution, Role.TEACHER),
        "student": make_user(db_session, institution, Role.STUDENT),
    }


@pytest.fixture
def other_admin(db_session: Session):
    return make_user(db_session, make_institution(db_session, "Colegio B"), Role.ADMIN)


def _create(client: TestClient, admin, **overrides):
    return client.post("/api/v1/elections", json=_payload(**overrides), headers=auth_headers(admin))


def test_admin_creates_election_pending_with_positions(client: TestClient, school) -> None:
    response = _create(client, school["admin"])
    assert response.status_code == 201
    body = response.json()
    assert body["status"] == "pending"
    assert body["results_published"] is False
    assert sorted(p["name"] for p in body["positions"]) == ["Contralor", "Personero"]
    assert body["institution_id"] == str(school["institution"].id)


def test_student_and_teacher_cannot_create(client: TestClient, school) -> None:
    for role in ("student", "teacher"):
        response = _create(client, school[role])
        assert response.status_code == 403


def test_create_requires_authentication(client: TestClient) -> None:
    assert client.post("/api/v1/elections", json=_payload()).status_code == 401


def test_end_before_start_is_rejected(client: TestClient, school) -> None:
    response = _create(
        client,
        school["admin"],
        starts_at=(NOW + timedelta(days=3)).isoformat(),
        ends_at=(NOW + timedelta(days=2)).isoformat(),
    )
    assert response.status_code == 422


def test_dates_without_timezone_are_rejected(client: TestClient, school) -> None:
    """H8: las fechas deben traer zona horaria."""
    naive = (datetime.now() + timedelta(days=1)).replace(tzinfo=None).isoformat()
    assert _create(client, school["admin"], starts_at=naive).status_code == 422


def test_duplicate_or_empty_positions_are_rejected(client: TestClient, school) -> None:
    assert _create(client, school["admin"], positions=["A", "a"]).status_code == 422
    assert _create(client, school["admin"], positions=[]).status_code == 422
    assert _create(client, school["admin"], positions=["  "]).status_code == 422


def test_list_shows_only_own_institution(client: TestClient, school, other_admin) -> None:
    _create(client, school["admin"])
    _create(client, other_admin)
    response = client.get("/api/v1/elections", headers=auth_headers(school["student"]))
    assert response.status_code == 200
    assert [e["institution_id"] for e in response.json()] == [str(school["institution"].id)]


def test_other_institution_cannot_read_update_delete_or_change_status(
    client: TestClient, school, other_admin
) -> None:
    """H1: el rol de administrador no basta; la elección debe ser de su institución."""
    election_id = _create(client, school["admin"]).json()["id"]
    headers = auth_headers(other_admin)
    url = f"/api/v1/elections/{election_id}"
    assert client.get(url, headers=headers).status_code == 403
    assert client.patch(url, json={"title": "Hackeada"}, headers=headers).status_code == 403
    assert client.delete(url, headers=headers).status_code == 403
    status_response = client.post(f"{url}/status", json={"status": "active"}, headers=headers)
    assert status_response.status_code == 403


def test_unknown_election_is_404(client: TestClient, school) -> None:
    url = "/api/v1/elections/00000000-0000-0000-0000-000000000000"
    assert client.get(url, headers=auth_headers(school["admin"])).status_code == 404


def test_teacher_can_edit_title_but_student_cannot(client: TestClient, school) -> None:
    election_id = _create(client, school["admin"]).json()["id"]
    url = f"/api/v1/elections/{election_id}"
    ok = client.patch(url, json={"title": "Nuevo título"}, headers=auth_headers(school["teacher"]))
    assert ok.status_code == 200
    assert ok.json()["title"] == "Nuevo título"
    denied = client.patch(url, json={"title": "Otro"}, headers=auth_headers(school["student"]))
    assert denied.status_code == 403


def test_pending_election_can_change_dates_and_positions(client: TestClient, school) -> None:
    election_id = _create(client, school["admin"]).json()["id"]
    response = client.patch(
        f"/api/v1/elections/{election_id}",
        json={"ends_at": (NOW + timedelta(days=5)).isoformat(), "positions": ["Personero"]},
        headers=auth_headers(school["admin"]),
    )
    assert response.status_code == 200
    assert [p["name"] for p in response.json()["positions"]] == ["Personero"]


def test_active_election_rejects_critical_changes(client: TestClient, school) -> None:
    """H4: no se cambian fechas ni cargos de una elección en curso."""
    admin = auth_headers(school["admin"])
    election_id = _create(client, school["admin"]).json()["id"]
    url = f"/api/v1/elections/{election_id}"
    client.post(f"{url}/status", json={"status": "active"}, headers=admin)
    response = client.patch(
        url, json={"ends_at": (NOW + timedelta(days=9)).isoformat()}, headers=admin
    )
    assert response.status_code == 409
    assert client.patch(url, json={"description": "ok"}, headers=admin).status_code == 200


def test_valid_status_sequence(client: TestClient, school) -> None:
    admin = auth_headers(school["admin"])
    url = f"/api/v1/elections/{_create(client, school['admin']).json()['id']}/status"
    assert client.post(url, json={"status": "active"}, headers=admin).json()["status"] == "active"
    done = client.post(url, json={"status": "finished"}, headers=admin)
    assert done.json()["status"] == "finished"


@pytest.mark.parametrize("target", ["finished", "pending"])
def test_invalid_transitions_from_pending(client: TestClient, school, target: str) -> None:
    admin = auth_headers(school["admin"])
    url = f"/api/v1/elections/{_create(client, school['admin']).json()['id']}/status"
    response = client.post(url, json={"status": target}, headers=admin)
    assert response.status_code == 409
    assert response.json()["code"] == "invalid_state_transition"


def test_finished_election_cannot_reopen(client: TestClient, school) -> None:
    admin = auth_headers(school["admin"])
    url = f"/api/v1/elections/{_create(client, school['admin']).json()['id']}/status"
    client.post(url, json={"status": "active"}, headers=admin)
    client.post(url, json={"status": "finished"}, headers=admin)
    assert client.post(url, json={"status": "active"}, headers=admin).status_code == 409


def test_admin_deletes_pending_election(client: TestClient, school) -> None:
    admin = auth_headers(school["admin"])
    url = f"/api/v1/elections/{_create(client, school['admin']).json()['id']}"
    assert client.delete(url, headers=admin).status_code == 204
    assert client.get(url, headers=admin).status_code == 404


def test_teacher_cannot_delete(client: TestClient, school) -> None:
    url = f"/api/v1/elections/{_create(client, school['admin']).json()['id']}"
    assert client.delete(url, headers=auth_headers(school["teacher"])).status_code == 403


def test_active_election_cannot_be_deleted(client: TestClient, school) -> None:
    admin = auth_headers(school["admin"])
    url = f"/api/v1/elections/{_create(client, school['admin']).json()['id']}"
    client.post(f"{url}/status", json={"status": "active"}, headers=admin)
    assert client.delete(url, headers=admin).status_code == 409


def test_election_with_votes_cannot_be_deleted_or_edited(
    client: TestClient, school, db_session: Session
) -> None:
    """H4: con votos registrados no se elimina ni se cambian sus fechas."""
    election = make_election(db_session, school["institution"])
    position = make_position(db_session, election)
    db_session.add(Vote(election_id=election.id, position_id=position.id))
    db_session.commit()
    admin = auth_headers(school["admin"])
    url = f"/api/v1/elections/{election.id}"
    assert election.status == ElectionStatus.PENDING
    assert client.delete(url, headers=admin).status_code == 409
    response = client.patch(
        url, json={"ends_at": (NOW + timedelta(days=9)).isoformat()}, headers=admin
    )
    assert response.status_code == 409
