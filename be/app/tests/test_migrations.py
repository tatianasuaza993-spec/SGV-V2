"""
Módulo: test_migrations.py
Descripción: Verifica que la migración y los modelos describen el mismo esquema.
¿Para qué? Detectar de inmediato si alguien cambia un modelo y olvida la migración.
¿Impacto? Sin esta prueba, el esquema desplegado y el que usa el código pueden diverger sin aviso.
"""

from alembic.autogenerate import compare_metadata
from alembic.migration import MigrationContext
from sqlalchemy import Engine

from app.models import Base


def test_migrations_match_models(db_engine: Engine) -> None:
    with db_engine.connect() as connection:
        context = MigrationContext.configure(connection, opts={"compare_type": True})
        differences = compare_metadata(context, Base.metadata)
    assert differences == []
