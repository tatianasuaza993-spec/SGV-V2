"""
Módulo: test_schema_constraints.py
Descripción: Pruebas de las restricciones críticas del esquema, sobre la base de pruebas.
¿Para qué? Comprobar que la base de datos (y no solo el código) hace cumplir las reglas de voto.
¿Impacto? H2 y H3 son los fallos que más afectan la confianza en una elección.
"""

from datetime import timedelta

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import Election, InvitationCode, Role, Vote, VoteRecord
from app.tests.factories import (
    make_candidacy,
    make_election,
    make_institution,
    make_position,
    make_user,
)


def test_same_person_cannot_vote_twice_for_a_position(db_session: Session) -> None:
    """H2: la base impide el segundo registro de participación."""
    institution = make_institution(db_session)
    voter = make_user(db_session, institution)
    election = make_election(db_session, institution)
    position = make_position(db_session, election)

    db_session.add(VoteRecord(user_id=voter.id, election_id=election.id, position_id=position.id))
    db_session.flush()
    db_session.add(VoteRecord(user_id=voter.id, election_id=election.id, position_id=position.id))
    with pytest.raises(IntegrityError):
        db_session.flush()


def test_same_person_can_vote_in_different_positions(db_session: Session) -> None:
    institution = make_institution(db_session)
    voter = make_user(db_session, institution)
    election = make_election(db_session, institution)
    first = make_position(db_session, election, "Personero")
    second = make_position(db_session, election, "Contralor")

    db_session.add(VoteRecord(user_id=voter.id, election_id=election.id, position_id=first.id))
    db_session.add(VoteRecord(user_id=voter.id, election_id=election.id, position_id=second.id))
    db_session.flush()


def test_vote_table_cannot_identify_the_voter() -> None:
    """H3: `votes` no tiene usuario ni fecha, así que no se puede unir con `vote_records`."""
    assert set(Vote.__table__.columns.keys()) == {
        "id",
        "election_id",
        "position_id",
        "candidacy_id",
    }


def test_blank_vote_is_allowed(db_session: Session) -> None:
    institution = make_institution(db_session)
    election = make_election(db_session, institution)
    position = make_position(db_session, election)
    db_session.add(Vote(election_id=election.id, position_id=position.id, candidacy_id=None))
    db_session.flush()


def test_candidacy_starts_pending(db_session: Session) -> None:
    """H12: toda candidatura nace pendiente de aprobación."""
    institution = make_institution(db_session)
    user = make_user(db_session, institution)
    election = make_election(db_session, institution)
    position = make_position(db_session, election)
    candidacy = make_candidacy(db_session, user, election, position)
    db_session.refresh(candidacy)
    assert candidacy.status == "pending"


def test_person_cannot_run_twice_for_the_same_position(db_session: Session) -> None:
    institution = make_institution(db_session)
    user = make_user(db_session, institution)
    election = make_election(db_session, institution)
    position = make_position(db_session, election)
    make_candidacy(db_session, user, election, position)
    with pytest.raises(IntegrityError):
        make_candidacy(db_session, user, election, position)


def test_election_starts_pending(db_session: Session) -> None:
    """H4: una elección nueva nace en «pending»."""
    institution = make_institution(db_session)
    election = make_election(db_session, institution)
    db_session.refresh(election)
    assert election.status == "pending"
    assert election.results_published is False


def test_election_cannot_end_before_it_starts(db_session: Session) -> None:
    institution = make_institution(db_session)
    election = make_election(db_session, institution)
    election.ends_at = election.starts_at - timedelta(hours=1)
    with pytest.raises(IntegrityError):
        db_session.flush()


def test_election_dates_keep_their_timezone(db_session: Session) -> None:
    """H8: las fechas se guardan con zona horaria."""
    institution = make_institution(db_session)
    election = make_election(db_session, institution)
    db_session.refresh(election)
    assert election.starts_at.tzinfo is not None


def test_duplicate_email_is_rejected(db_session: Session) -> None:
    institution = make_institution(db_session)
    user = make_user(db_session, institution)
    other = make_user(db_session, institution)
    other.email = user.email
    with pytest.raises(IntegrityError):
        db_session.flush()


def test_invitation_code_cannot_exceed_its_uses(db_session: Session) -> None:
    """H6: los códigos tienen un número máximo de usos."""
    institution = make_institution(db_session)
    election = make_election(db_session, institution)
    db_session.add(
        InvitationCode(
            institution_id=institution.id,
            code="ABCD1234",
            role=Role.TEACHER,
            expires_at=election.ends_at,
            max_uses=1,
            uses=2,
        )
    )
    with pytest.raises(IntegrityError):
        db_session.flush()


def test_invitation_code_cannot_grant_student_role(db_session: Session) -> None:
    institution = make_institution(db_session)
    election = make_election(db_session, institution)
    db_session.add(
        InvitationCode(
            institution_id=institution.id,
            code="STUD1234",
            role=Role.STUDENT,
            expires_at=election.ends_at,
        )
    )
    with pytest.raises(IntegrityError):
        db_session.flush()


def test_election_with_votes_cannot_be_deleted(db_session: Session) -> None:
    """H4: la base impide borrar una elección que ya tiene votos."""
    institution = make_institution(db_session)
    election = make_election(db_session, institution)
    position = make_position(db_session, election)
    db_session.add(Vote(election_id=election.id, position_id=position.id))
    db_session.flush()
    db_session.delete(election)
    with pytest.raises(IntegrityError):
        db_session.flush()


def test_pending_election_without_votes_can_be_deleted(db_session: Session) -> None:
    institution = make_institution(db_session)
    election = make_election(db_session, institution)
    make_position(db_session, election)
    db_session.delete(election)
    db_session.flush()
    assert db_session.get(Election, election.id) is None
