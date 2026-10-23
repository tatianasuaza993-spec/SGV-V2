"""
Módulo: invitation_codes.py (router)
Descripción: El administrador genera, consulta y desactiva códigos de invitación (RF-018).
¿Para qué? Controlar quién puede vincularse a la institución como administrador o docente (H6).
¿Impacto? Todas las rutas comparan la institución del administrador con la del código (H1).
"""

import uuid

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import require_roles
from app.models import Role, User
from app.schemas.auth import InvitationCodeCreate, InvitationCodeResponse
from app.services import auth_service

router = APIRouter(prefix="/invitation-codes", tags=["invitation-codes"])


@router.post("", response_model=InvitationCodeResponse, status_code=status.HTTP_201_CREATED)
def create_code(
    data: InvitationCodeCreate,
    admin: User = Depends(require_roles(Role.ADMIN)),
    db: Session = Depends(get_db),
):
    return auth_service.create_invitation_code(db, admin, data)


@router.get("", response_model=list[InvitationCodeResponse])
def list_codes(admin: User = Depends(require_roles(Role.ADMIN)), db: Session = Depends(get_db)):
    return auth_service.list_invitation_codes(db, admin)


@router.post("/{code_id}/deactivate", response_model=InvitationCodeResponse)
def deactivate_code(
    code_id: uuid.UUID,
    admin: User = Depends(require_roles(Role.ADMIN)),
    db: Session = Depends(get_db),
):
    return auth_service.deactivate_invitation_code(db, admin, code_id)
