"""Esquema inicial de SGV

¿Qué? Crea todas las tablas del sistema de votación.
¿Para qué? Partir de un esquema que ya incluye las correcciones H1 a H12 del análisis.
¿Impacto? Las restricciones críticas viven en la base: un voto por persona y cargo,
votos sin usuario ni fecha, fechas con zona horaria y estados validados.

Revision ID: 0001
Revises:
"""

import sqlalchemy as sa
from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def _id() -> sa.Column:
    return sa.Column("id", sa.Uuid(), nullable=False)


def _created_at() -> sa.Column:
    return sa.Column(
        "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
    )


def _updated_at() -> sa.Column:
    return sa.Column(
        "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
    )


def upgrade() -> None:
    op.create_table(
        "institutions",
        _id(),
        sa.Column("name", sa.String(256), nullable=False),
        sa.Column("nit", sa.String(15), nullable=True),
        sa.Column("address", sa.String(100), nullable=False),
        sa.Column("phone", sa.String(15), nullable=True),
        sa.Column("email", sa.String(256), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        _created_at(),
        _updated_at(),
        sa.PrimaryKeyConstraint("id", name="pk_institutions"),
        sa.UniqueConstraint("nit", name="uq_institutions_nit"),
    )

    op.create_table(
        "users",
        _id(),
        sa.Column("institution_id", sa.Uuid(), nullable=True),
        sa.Column("document_type", sa.String(20), nullable=False),
        sa.Column("document_number", sa.String(20), nullable=False),
        sa.Column("first_name", sa.String(100), nullable=False),
        sa.Column("last_name", sa.String(100), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("course", sa.String(20), nullable=True),
        sa.Column("avatar_url", sa.String(255), nullable=True),
        sa.Column("role", sa.String(20), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true"), nullable=False),
        sa.Column(
            "failed_login_attempts", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.Column("locked_until", sa.DateTime(timezone=True), nullable=True),
        _created_at(),
        _updated_at(),
        sa.PrimaryKeyConstraint("id", name="pk_users"),
        sa.ForeignKeyConstraint(
            ["institution_id"], ["institutions.id"], name="fk_users_institution_id_institutions"
        ),
        sa.UniqueConstraint("document_number", name="uq_users_document_number"),
        sa.UniqueConstraint("email", name="uq_users_email"),
        sa.CheckConstraint(
            "document_type IN ('CC', 'TI', 'CE', 'PPT')", name="ck_users_document_type"
        ),
        sa.CheckConstraint("role IN ('admin', 'teacher', 'student')", name="ck_users_role"),
    )
    op.create_index("ix_users_institution_id", "users", ["institution_id"])

    op.create_table(
        "invitation_codes",
        _id(),
        sa.Column("institution_id", sa.Uuid(), nullable=False),
        sa.Column("code", sa.String(32), nullable=False),
        sa.Column("role", sa.String(20), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("max_uses", sa.Integer(), server_default=sa.text("1"), nullable=False),
        sa.Column("uses", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true"), nullable=False),
        sa.Column("created_by", sa.Uuid(), nullable=True),
        _created_at(),
        sa.PrimaryKeyConstraint("id", name="pk_invitation_codes"),
        sa.ForeignKeyConstraint(
            ["institution_id"],
            ["institutions.id"],
            name="fk_invitation_codes_institution_id_institutions",
        ),
        sa.ForeignKeyConstraint(
            ["created_by"], ["users.id"], name="fk_invitation_codes_created_by_users"
        ),
        sa.UniqueConstraint("code", name="uq_invitation_codes_code"),
        sa.CheckConstraint(
            "role IN ('admin', 'teacher', 'student')", name="ck_invitation_codes_role"
        ),
        sa.CheckConstraint(
            "role IN ('admin', 'teacher')", name="ck_invitation_codes_role_allowed"
        ),
        sa.CheckConstraint("max_uses >= 1", name="ck_invitation_codes_max_uses_positive"),
        sa.CheckConstraint(
            "uses >= 0 AND uses <= max_uses", name="ck_invitation_codes_uses_within_limit"
        ),
    )
    op.create_index("ix_invitation_codes_institution_id", "invitation_codes", ["institution_id"])

    op.create_table(
        "password_reset_tokens",
        _id(),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("token_hash", sa.String(64), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("used_at", sa.DateTime(timezone=True), nullable=True),
        _created_at(),
        sa.PrimaryKeyConstraint("id", name="pk_password_reset_tokens"),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name="fk_password_reset_tokens_user_id_users",
            ondelete="CASCADE",
        ),
        sa.UniqueConstraint("token_hash", name="uq_password_reset_tokens_token_hash"),
    )
    op.create_index("ix_password_reset_tokens_user_id", "password_reset_tokens", ["user_id"])

    op.create_table(
        "elections",
        _id(),
        sa.Column("institution_id", sa.Uuid(), nullable=False),
        sa.Column("title", sa.String(150), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("starts_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ends_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("status", sa.String(20), server_default=sa.text("'pending'"), nullable=False),
        sa.Column(
            "results_published", sa.Boolean(), server_default=sa.text("false"), nullable=False
        ),
        _created_at(),
        _updated_at(),
        sa.PrimaryKeyConstraint("id", name="pk_elections"),
        sa.ForeignKeyConstraint(
            ["institution_id"], ["institutions.id"], name="fk_elections_institution_id_institutions"
        ),
        sa.CheckConstraint("ends_at > starts_at", name="ck_elections_ends_after_start"),
        sa.CheckConstraint(
            "status IN ('pending', 'active', 'finished')", name="ck_elections_election_status"
        ),
    )
    op.create_index("ix_elections_institution_id", "elections", ["institution_id"])

    op.create_table(
        "positions",
        _id(),
        sa.Column("election_id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_positions"),
        sa.ForeignKeyConstraint(
            ["election_id"],
            ["elections.id"],
            name="fk_positions_election_id_elections",
            ondelete="CASCADE",
        ),
        sa.UniqueConstraint("election_id", "name", name="uq_positions_election_name"),
    )
    op.create_index("ix_positions_election_id", "positions", ["election_id"])

    op.create_table(
        "candidacies",
        _id(),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("election_id", sa.Uuid(), nullable=False),
        sa.Column("position_id", sa.Uuid(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=True),
        sa.Column("slogan", sa.String(200), nullable=True),
        sa.Column("proposal", sa.Text(), nullable=True),
        sa.Column("photo_url", sa.String(255), nullable=True),
        sa.Column("status", sa.String(20), server_default=sa.text("'pending'"), nullable=False),
        sa.Column("review_notes", sa.Text(), nullable=True),
        sa.Column("reviewed_by", sa.Uuid(), nullable=True),
        sa.Column("reviewed_at", sa.DateTime(timezone=True), nullable=True),
        _created_at(),
        _updated_at(),
        sa.PrimaryKeyConstraint("id", name="pk_candidacies"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_candidacies_user_id_users"),
        sa.ForeignKeyConstraint(
            ["election_id"],
            ["elections.id"],
            name="fk_candidacies_election_id_elections",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["position_id"],
            ["positions.id"],
            name="fk_candidacies_position_id_positions",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["reviewed_by"], ["users.id"], name="fk_candidacies_reviewed_by_users"
        ),
        sa.UniqueConstraint("user_id", "position_id", name="uq_candidacies_user_position"),
        sa.UniqueConstraint("position_id", "number", name="uq_candidacies_position_number"),
        sa.CheckConstraint(
            "status IN ('pending', 'approved', 'rejected', 'withdrawn')",
            name="ck_candidacies_candidacy_status",
        ),
    )
    op.create_index("ix_candidacies_user_id", "candidacies", ["user_id"])
    op.create_index("ix_candidacies_election_id", "candidacies", ["election_id"])
    op.create_index("ix_candidacies_position_id", "candidacies", ["position_id"])

    # Voto anónimo: sin usuario y sin fecha (H3)
    op.create_table(
        "votes",
        _id(),
        sa.Column("election_id", sa.Uuid(), nullable=False),
        sa.Column("position_id", sa.Uuid(), nullable=False),
        sa.Column("candidacy_id", sa.Uuid(), nullable=True),
        sa.PrimaryKeyConstraint("id", name="pk_votes"),
        sa.ForeignKeyConstraint(
            ["election_id"], ["elections.id"], name="fk_votes_election_id_elections"
        ),
        sa.ForeignKeyConstraint(
            ["position_id"], ["positions.id"], name="fk_votes_position_id_positions"
        ),
        sa.ForeignKeyConstraint(
            ["candidacy_id"], ["candidacies.id"], name="fk_votes_candidacy_id_candidacies"
        ),
    )
    op.create_index("ix_votes_election_id", "votes", ["election_id"])
    op.create_index("ix_votes_position_id", "votes", ["position_id"])
    op.create_index("ix_votes_candidacy_id", "votes", ["candidacy_id"])

    # Un voto por persona y por cargo, garantizado por la base de datos (H2)
    op.create_table(
        "vote_records",
        _id(),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("election_id", sa.Uuid(), nullable=False),
        sa.Column("position_id", sa.Uuid(), nullable=False),
        _created_at(),
        sa.PrimaryKeyConstraint("id", name="pk_vote_records"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_vote_records_user_id_users"),
        sa.ForeignKeyConstraint(
            ["election_id"], ["elections.id"], name="fk_vote_records_election_id_elections"
        ),
        sa.ForeignKeyConstraint(
            ["position_id"], ["positions.id"], name="fk_vote_records_position_id_positions"
        ),
        sa.UniqueConstraint("user_id", "position_id", name="uq_vote_records_user_position"),
    )
    op.create_index("ix_vote_records_user_id", "vote_records", ["user_id"])
    op.create_index("ix_vote_records_election_id", "vote_records", ["election_id"])
    op.create_index("ix_vote_records_position_id", "vote_records", ["position_id"])

    op.create_table(
        "notifications",
        _id(),
        sa.Column("institution_id", sa.Uuid(), nullable=False),
        sa.Column("recipient_id", sa.Uuid(), nullable=False),
        sa.Column("sender_id", sa.Uuid(), nullable=True),
        sa.Column("title", sa.String(150), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("read_at", sa.DateTime(timezone=True), nullable=True),
        _created_at(),
        sa.PrimaryKeyConstraint("id", name="pk_notifications"),
        sa.ForeignKeyConstraint(
            ["institution_id"],
            ["institutions.id"],
            name="fk_notifications_institution_id_institutions",
        ),
        sa.ForeignKeyConstraint(
            ["recipient_id"],
            ["users.id"],
            name="fk_notifications_recipient_id_users",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["sender_id"], ["users.id"], name="fk_notifications_sender_id_users"
        ),
    )
    op.create_index("ix_notifications_institution_id", "notifications", ["institution_id"])
    op.create_index("ix_notifications_recipient_id", "notifications", ["recipient_id"])

    op.create_table(
        "contact_messages",
        _id(),
        sa.Column("user_id", sa.Uuid(), nullable=True),
        sa.Column("name", sa.String(150), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("subject", sa.String(150), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        _created_at(),
        sa.PrimaryKeyConstraint("id", name="pk_contact_messages"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_contact_messages_user_id_users"
        ),
    )


def downgrade() -> None:
    for table in (
        "contact_messages",
        "notifications",
        "vote_records",
        "votes",
        "candidacies",
        "positions",
        "elections",
        "password_reset_tokens",
        "invitation_codes",
        "users",
        "institutions",
    ):
        op.drop_table(table)
