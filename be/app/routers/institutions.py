"""
Módulo: institutions.py (router)
Descripción: Crear una institución y unirse a una con código de invitación.
¿Para qué? Cubrir RF-006 y dar un punto de partida al primer administrador de cada institución.
¿Impacto? Sin esta ruta, un administrador recién registrado no tendría forma de operar.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user, require_roles
from app.models import Role, User
from app.schemas.auth import InstitutionCreate, InstitutionResponse, JoinInstitutionRequest
from app.services import auth_service

router = APIRouter(prefix="/institutions", tags=["institutions"])


@router.post("", response_model=InstitutionResponse, status_code=status.HTTP_201_CREATED)
def create_institution(
    data: InstitutionCreate,
    user: User = Depends(require_roles(Role.ADMIN)),
    db: Session = Depends(get_db),
):
    return auth_service.create_institution(db, user, data)


@router.post("/join", response_model=InstitutionResponse)
def join_institution(
    data: JoinInstitutionRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return auth_service.join_institution(db, user, data.code)
