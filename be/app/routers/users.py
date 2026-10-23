"""
Módulo: users.py (router)
Descripción: Endpoints del perfil de la persona autenticada.
¿Para qué? Que el frontend sepa quién es el usuario y a qué institución pertenece.
¿Impacto? Es la primera ruta protegida: demuestra el flujo token → usuario → rol.
"""

from fastapi import APIRouter, Depends

from app.dependencies import get_current_user
from app.models import User
from app.schemas.auth import UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
def read_me(user: User = Depends(get_current_user)):
    return user
