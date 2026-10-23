"""
Módulo: elections.py (router)
Descripción: Endpoints de elecciones. La lógica está en `election_service`.
¿Para qué? Exponer RF-009 (administrador), RF-019 (docente), RF-020 y RF-026 (consulta).
¿Impacto? Crear y eliminar son del administrador; editar y cambiar de estado, también del
docente. Todas las rutas comparan la institución en el servicio (H1).
"""

import uuid

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user, require_roles
from app.models import Role, User
from app.schemas.election import (
    ElectionCreate,
    ElectionResponse,
    ElectionStatusChange,
    ElectionUpdate,
)
from app.services import election_service

router = APIRouter(prefix="/elections", tags=["elections"])


@router.post("", response_model=ElectionResponse, status_code=status.HTTP_201_CREATED)
def create_election(
    data: ElectionCreate,
    admin: User = Depends(require_roles(Role.ADMIN)),
    db: Session = Depends(get_db),
):
    return election_service.create_election(db, admin, data)


@router.get("", response_model=list[ElectionResponse])
def list_elections(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return election_service.list_elections(db, user)


@router.get("/{election_id}", response_model=ElectionResponse)
def get_election(
    election_id: uuid.UUID,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return election_service.get_election_for_user(db, user, election_id)


@router.patch("/{election_id}", response_model=ElectionResponse)
def update_election(
    election_id: uuid.UUID,
    data: ElectionUpdate,
    user: User = Depends(require_roles(Role.ADMIN, Role.TEACHER)),
    db: Session = Depends(get_db),
):
    return election_service.update_election(db, user, election_id, data)


@router.delete("/{election_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_election(
    election_id: uuid.UUID,
    admin: User = Depends(require_roles(Role.ADMIN)),
    db: Session = Depends(get_db),
):
    election_service.delete_election(db, admin, election_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/{election_id}/status", response_model=ElectionResponse)
def change_status(
    election_id: uuid.UUID,
    data: ElectionStatusChange,
    user: User = Depends(require_roles(Role.ADMIN, Role.TEACHER)),
    db: Session = Depends(get_db),
):
    return election_service.change_status(db, user, election_id, data.status)
