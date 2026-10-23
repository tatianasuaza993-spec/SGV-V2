"""
Módulo: models
Descripción: Importa todos los modelos para que `Base.metadata` los conozca (Alembic y pruebas).
¿Impacto? Si un modelo no se importa aquí, Alembic no lo ve y la migración queda incompleta.
"""

from app.models.base import Base
from app.models.candidacy import Candidacy
from app.models.communication import ContactMessage, Notification
from app.models.election import Election, Position
from app.models.enums import CandidacyStatus, DocumentType, ElectionStatus, Role
from app.models.institution import Institution
from app.models.invitation_code import InvitationCode
from app.models.user import PasswordResetToken, User
from app.models.vote import Vote, VoteRecord

__all__ = [
    "Base",
    "Candidacy",
    "CandidacyStatus",
    "ContactMessage",
    "DocumentType",
    "Election",
    "ElectionStatus",
    "Institution",
    "InvitationCode",
    "Notification",
    "PasswordResetToken",
    "Position",
    "Role",
    "User",
    "Vote",
    "VoteRecord",
]
