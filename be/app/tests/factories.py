"""
Módulo: factories.py
Descripción: Funciones auxiliares que crean datos de prueba válidos.
¿Para qué? Que cada prueba cree solo lo que necesita sin repetir campos obligatorios.
¿Impacto? Sin ellas, cada prueba repetiría decenas de líneas de preparación.
"""

import itertools
from datetime import UTC, datetime, timedelta

from sqlalchemy.orm import Session

from app.models import (
    Candidacy,
    DocumentType,
    Election,
    Institution,
    Position,
    Role,
    User,
)
from app.utils.security import create_access_token

_counter = itertools.count(1)


def make_institution(session: Session, name: str = "Colegio de Prueba") -> Institution:
    institution = Institution(name=name, address="Calle 1 # 2-3")
    session.add(institution)
    session.flush()
    return institution


def make_user(
    session: Session,
    institution: Institution | None,
    role: Role = Role.STUDENT,
) -> User:
    number = next(_counter)
    user = User(
        institution_id=institution.id if institution else None,
        document_type=DocumentType.TI,
        document_number=f"1000{number:06d}",
        first_name="Persona",
        last_name=f"Prueba {number}",
        email=f"persona{number}@example.com",
        hashed_password="not-a-real-hash",
        role=role,
    )
    session.add(user)
    session.flush()
    return user


def make_election(session: Session, institution: Institution) -> Election:
    now = datetime.now(UTC)
    election = Election(
        institution_id=institution.id,
        title="Elección de prueba",
        starts_at=now + timedelta(days=1),
        ends_at=now + timedelta(days=2),
    )
    session.add(election)
    session.flush()
    return election


def make_position(session: Session, election: Election, name: str = "Personero") -> Position:
    position = Position(election_id=election.id, name=name)
    session.add(position)
    session.flush()
    return position


def make_candidacy(
    session: Session, user: User, election: Election, position: Position
) -> Candidacy:
    candidacy = Candidacy(user_id=user.id, election_id=election.id, position_id=position.id)
    session.add(candidacy)
    session.flush()
    return candidacy


def auth_headers(user: User) -> dict[str, str]:
    """Encabezado Authorization con un token de acceso válido para el usuario."""
    return {"Authorization": f"Bearer {create_access_token(user.id, user.role.value)}"}
