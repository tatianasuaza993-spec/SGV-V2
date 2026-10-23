"""
Módulo: database.py
Descripción: Motor, fábrica de sesiones y dependencia `get_db` de SQLAlchemy.
¿Para qué? Dar a cada petición su propia sesión desde un pool de conexiones.
¿Impacto? Sin pool, cada consulta abriría una conexión nueva (hallazgo H7) y los errores de la
base se confundirían con resultados vacíos.
"""

from collections.abc import Iterator
from functools import lru_cache

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config import get_settings


@lru_cache
def get_engine() -> Engine:
    """Crea el motor una sola vez, con pool y verificación de conexiones."""
    return create_engine(
        get_settings().database_url,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
    )


@lru_cache
def get_session_factory() -> sessionmaker[Session]:
    """Fábrica de sesiones ligada al motor."""
    return sessionmaker(bind=get_engine(), autoflush=False, expire_on_commit=False)


def get_db() -> Iterator[Session]:
    """Dependencia de FastAPI: entrega una sesión y la cierra al terminar la petición."""
    session = get_session_factory()()
    try:
        yield session
    finally:
        session.close()
