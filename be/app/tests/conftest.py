"""
Módulo: conftest.py
Descripción: Configuración compartida de las pruebas: entorno, base de datos de pruebas y sesión.
¿Para qué? Que las pruebas usen una base exclusiva y desechable creada con las migraciones.
¿Impacto? Probar sobre el esquema de las migraciones (y no sobre `create_all`) garantiza que lo
que se despliega es lo que se probó. Nunca se corre contra la base de desarrollo.
"""

import os
from collections.abc import Iterator
from pathlib import Path

# Variables mínimas para que la aplicación arranque en las pruebas. Se definen ANTES de importar
# `app`, porque la configuración se valida al importar.
os.environ.setdefault("DATABASE_URL", "postgresql://sgv_user:sgv_password@localhost:5432/sgv_db")
os.environ.setdefault("SECRET_KEY", "ci-test-secret-key-not-for-production-32")
os.environ.setdefault("CORS_ORIGINS", '["http://localhost:5173"]')
os.environ.setdefault("FRONTEND_URL", "http://localhost:5173")
os.environ.setdefault("ENVIRONMENT", "testing")

import pytest  # noqa: E402
from alembic import command  # noqa: E402
from alembic.config import Config  # noqa: E402
from sqlalchemy import Engine, create_engine, text  # noqa: E402
from sqlalchemy.orm import Session  # noqa: E402

BE_DIR = Path(__file__).resolve().parents[2]


def _alembic_config(url: str) -> Config:
    config = Config(str(BE_DIR / "alembic.ini"))
    config.set_main_option("script_location", str(BE_DIR / "alembic"))
    config.set_main_option("sqlalchemy.url", url.replace("%", "%%"))
    return config


@pytest.fixture(scope="session")
def db_engine() -> Iterator[Engine]:
    """Motor de la base de pruebas con el esquema creado por las migraciones."""
    url = os.environ.get("TEST_DATABASE_URL")
    if not url:
        message = "TEST_DATABASE_URL no está definida: las pruebas de base de datos no corren."
        if os.environ.get("CI"):
            pytest.fail(message)
        pytest.skip(message)
    if url == os.environ["DATABASE_URL"]:
        pytest.exit("TEST_DATABASE_URL apunta a la base de desarrollo: se detienen las pruebas.")

    engine = create_engine(url)
    with engine.begin() as connection:
        connection.execute(text("DROP SCHEMA public CASCADE"))
        connection.execute(text("CREATE SCHEMA public"))
    command.upgrade(_alembic_config(url), "head")
    yield engine
    engine.dispose()


@pytest.fixture
def db_session(db_engine: Engine) -> Iterator[Session]:
    """Sesión por prueba: todo lo que se escribe se deshace al terminar."""
    connection = db_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection, join_transaction_mode="create_savepoint")
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def client(db_session: Session):
    """Cliente HTTP que usa la sesión de pruebas (todo se deshace al terminar)."""
    from fastapi.testclient import TestClient

    from app.database import get_db
    from app.main import create_app

    app = create_app()
    app.dependency_overrides[get_db] = lambda: db_session
    return TestClient(app)
