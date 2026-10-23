"""
Módulo: test_auth_api.py
Descripción: Pruebas de registro, inicio de sesión, renovación y perfil (RF-002, RF-003).
¿Para qué? Verificar los escenarios de las historias HU-002 y HU-003 y el hallazgo H10.
¿Impacto? Garantiza que el login no delata qué cuentas existen y que se bloquea la fuerza bruta.
"""

from fastapi.testclient import TestClient

PASSWORD = "Clave-Segura1"


def _register(client: TestClient, email: str = "ana@example.com", role: str = "admin", **extra):
    payload = {
        "first_name": "Ana",
        "last_name": "Pérez",
        "email": email,
        "document_type": "CC",
        "document_number": extra.pop("document_number", "1001"),
        "password": PASSWORD,
        "role": role,
    }
    payload.update(extra)
    return client.post("/api/v1/auth/register", json=payload)


def _login(client: TestClient, email: str, password: str = PASSWORD):
    return client.post("/api/v1/auth/login", json={"email": email, "password": password})


def test_register_creates_account_without_exposing_password(client: TestClient) -> None:
    response = _register(client)
    assert response.status_code == 201
    body = response.json()
    assert body["email"] == "ana@example.com"
    assert body["role"] == "admin"
    assert body["institution_id"] is None
    assert "password" not in body and "hashed_password" not in body


def test_register_rejects_duplicate_email(client: TestClient) -> None:
    assert _register(client).status_code == 201
    response = _register(client, document_number="2002")
    assert response.status_code == 409


def test_register_rejects_duplicate_document(client: TestClient) -> None:
    assert _register(client).status_code == 201
    assert _register(client, email="otra@example.com").status_code == 409


def test_register_rejects_weak_password(client: TestClient) -> None:
    assert _register(client, password="corta").status_code == 422
    assert _register(client, password="todominusculas1").status_code == 422
    assert _register(client, password="SinNumeroAqui").status_code == 422


def test_register_rejects_student_role(client: TestClient) -> None:
    assert _register(client, role="student").status_code == 422


def test_login_returns_tokens_and_me_works(client: TestClient) -> None:
    _register(client)
    response = _login(client, "ana@example.com")
    assert response.status_code == 200
    tokens = response.json()
    me = client.get(
        "/api/v1/users/me", headers={"Authorization": f"Bearer {tokens['access_token']}"}
    )
    assert me.status_code == 200
    assert me.json()["email"] == "ana@example.com"


def test_login_is_case_insensitive_on_email(client: TestClient) -> None:
    _register(client)
    assert _login(client, "ANA@Example.com").status_code == 200


def test_login_error_is_identical_for_unknown_email_and_wrong_password(
    client: TestClient,
) -> None:
    """H10: el mensaje no revela si la cuenta existe."""
    _register(client)
    wrong_password = _login(client, "ana@example.com", "Incorrecta1")
    unknown_email = _login(client, "nadie@example.com")
    assert wrong_password.status_code == unknown_email.status_code == 401
    assert wrong_password.json() == unknown_email.json()


def test_account_locks_after_repeated_failures(client: TestClient) -> None:
    """H10: tras 5 fallos, ni siquiera la contraseña correcta entra mientras dure el bloqueo."""
    _register(client)
    for _ in range(5):
        assert _login(client, "ana@example.com", "Incorrecta1").status_code == 401
    locked = _login(client, "ana@example.com")
    assert locked.status_code == 401
    assert locked.json()["detail"] == "Invalid email or password"


def test_successful_login_resets_failed_attempts(client: TestClient) -> None:
    _register(client)
    for _ in range(3):
        _login(client, "ana@example.com", "Incorrecta1")
    assert _login(client, "ana@example.com").status_code == 200
    for _ in range(3):
        _login(client, "ana@example.com", "Incorrecta1")
    assert _login(client, "ana@example.com").status_code == 200


def test_refresh_returns_new_tokens(client: TestClient) -> None:
    _register(client)
    tokens = _login(client, "ana@example.com").json()
    response = client.post("/api/v1/auth/refresh", json={"refresh_token": tokens["refresh_token"]})
    assert response.status_code == 200
    assert response.json()["access_token"]


def test_access_token_cannot_be_used_to_refresh(client: TestClient) -> None:
    _register(client)
    tokens = _login(client, "ana@example.com").json()
    response = client.post("/api/v1/auth/refresh", json={"refresh_token": tokens["access_token"]})
    assert response.status_code == 401


def test_me_requires_authentication(client: TestClient) -> None:
    assert client.get("/api/v1/users/me").status_code == 401
    bad = client.get("/api/v1/users/me", headers={"Authorization": "Bearer nope"})
    assert bad.status_code == 401
