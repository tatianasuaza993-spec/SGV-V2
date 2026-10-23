"""
Módulo: auth.py (schemas)
Descripción: Modelos Pydantic de entrada y salida de autenticación, instituciones y códigos.
¿Para qué? Validar todo lo que llega del cliente y decidir qué se devuelve.
¿Impacto? La respuesta de usuario nunca incluye la contraseña (RS-003) y la contraseña débil se
rechaza antes de llegar a la base (RF-002).
"""

import re
import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from app.models import DocumentType, Role


def validate_password_strength(value: str) -> str:
    """Mínimo 8 caracteres con mayúscula, minúscula y número; máximo 72 bytes (límite de bcrypt)."""
    if len(value) < 8:
        raise ValueError("Password must have at least 8 characters")
    if len(value.encode()) > 72:
        raise ValueError("Password must have at most 72 bytes")
    if not re.search(r"[A-Z]", value) or not re.search(r"[a-z]", value):
        raise ValueError("Password must include upper and lower case letters")
    if not re.search(r"\d", value):
        raise ValueError("Password must include a number")
    return value


class RegisterRequest(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    document_type: DocumentType
    document_number: str = Field(min_length=3, max_length=20)
    password: str
    # Solo administradores y docentes se registran solos (RF-002); los estudiantes los crea la
    # institución.
    role: Literal["admin", "teacher"]

    _check_password = field_validator("password")(validate_password_strength)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)


class RefreshRequest(BaseModel):
    refresh_token: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    institution_id: uuid.UUID | None
    document_type: DocumentType
    document_number: str
    first_name: str
    last_name: str
    email: EmailStr
    role: Role
    course: str | None
    is_active: bool


class InstitutionCreate(BaseModel):
    name: str = Field(min_length=2, max_length=256)
    address: str = Field(min_length=2, max_length=100)
    nit: str | None = Field(default=None, max_length=15)
    phone: str | None = Field(default=None, max_length=15)
    email: EmailStr | None = None
    description: str | None = None


class InstitutionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    address: str
    nit: str | None
    phone: str | None
    email: str | None
    description: str | None


class JoinInstitutionRequest(BaseModel):
    code: str = Field(min_length=4, max_length=32)


class InvitationCodeCreate(BaseModel):
    role: Literal["admin", "teacher"]
    expires_in_days: int = Field(default=7, ge=1, le=90)
    max_uses: int = Field(default=1, ge=1, le=500)


class InvitationCodeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    institution_id: uuid.UUID
    code: str
    role: Role
    expires_at: datetime
    max_uses: int
    uses: int
    is_active: bool
