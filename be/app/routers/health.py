"""
Módulo: health.py
Descripción: Rutas de estado del servicio.
¿Para qué? Que Docker y la CI sepan si la API está viva y si la base de datos responde.
¿Impacto? Sin ellas, un contenedor puede parecer sano aunque no llegue a la base.
"""

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health() -> dict[str, str]:
    """El proceso está vivo."""
    return {"status": "ok"}


@router.get("/ready")
def ready(db: Session = Depends(get_db)) -> dict[str, str]:
    """La base de datos responde. Si falla, el error sube como 500 (no se oculta, H7)."""
    db.execute(text("SELECT 1"))
    return {"status": "ready"}
