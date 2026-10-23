"""
Módulo: test_security.py
Descripción: Pruebas de hash de contraseñas, tokens JWT y códigos aleatorios. Sin base de datos.
¿Para qué? Verificar la base criptográfica del sistema.
¿Impacto? Un token de renovación aceptado como de acceso, o un token vencido aceptado, sería un
fallo grave de autenticación.
"""

import uuid
from datetime import timedelta

import pytest

from app.exceptions import UnauthorizedError
from app.utils.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    generate_invitation_code,
    hash_password,
    hash_token,
    verify_password,
)


def test_password_hash_is_not_plain_and_verifies() -> None:
    hashed = hash_password("Clave-Segura1")
    assert hashed != "Clave-Segura1"
    assert verify_password("Clave-Segura1", hashed)
    assert not verify_password("otra-clave", hashed)


def test_invalid_hash_does_not_verify() -> None:
    assert not verify_password("x", "no-es-un-hash")


def test_access_token_round_trip() -> None:
    user_id = uuid.uuid4()
    claims = decode_token(create_access_token(user_id, "admin"), "access")
    assert claims["sub"] == str(user_id)
    assert claims["role"] == "admin"


def test_refresh_token_is_not_valid_as_access_token() -> None:
    token = create_refresh_token(uuid.uuid4(), "teacher")
    with pytest.raises(UnauthorizedError):
        decode_token(token, "access")


def test_access_token_is_not_valid_as_refresh_token() -> None:
    token = create_access_token(uuid.uuid4(), "teacher")
    with pytest.raises(UnauthorizedError):
        decode_token(token, "refresh")


def test_expired_token_is_rejected() -> None:
    token = create_access_token(uuid.uuid4(), "admin", expires_delta=timedelta(seconds=-5))
    with pytest.raises(UnauthorizedError):
        decode_token(token, "access")


def test_tampered_token_is_rejected() -> None:
    token = create_access_token(uuid.uuid4(), "admin")
    with pytest.raises(UnauthorizedError):
        decode_token(token[:-3] + "abc", "access")


def test_invitation_codes_are_random_and_unambiguous() -> None:
    codes = {generate_invitation_code() for _ in range(200)}
    assert len(codes) == 200
    assert all(len(code) == 10 for code in codes)
    assert not any(char in code for code in codes for char in "01OIl")


def test_token_hash_is_stable_and_not_the_token() -> None:
    assert hash_token("abc") == hash_token("abc")
    assert hash_token("abc") != "abc"
    assert len(hash_token("abc")) == 64
