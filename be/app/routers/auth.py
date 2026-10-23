"""
Módulo: auth.py (router)
Descripción: Endpoints de registro, inicio de sesión y renovación de token.
¿Para qué? Exponer RF-002 y RF-003 por HTTP; la lógica está en `auth_service`.
¿Impacto? El cierre de sesión (RF-008) es del lado del cliente: el JWT no guarda estado, así que
el frontend descarta los tokens; el de acceso expira solo en 15 minutos.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import (
    LoginRequest,
    RefreshRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    return auth_service.register_user(db, data)


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = auth_service.authenticate(db, data.email, data.password)
    return auth_service.issue_tokens(user)


@router.post("/refresh", response_model=TokenResponse)
def refresh(data: RefreshRequest, db: Session = Depends(get_db)):
    return auth_service.refresh_tokens(db, data.refresh_token)
