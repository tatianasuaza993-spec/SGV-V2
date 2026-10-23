"""
Módulo: access.py
Descripción: Guardia de aislamiento por institución, compartida por todos los servicios.
¿Para qué? Que ninguna persona actúe sobre elecciones, candidaturas, votos o resultados de otra
institución (hallazgo H1).
¿Impacto? Antes las rutas solo exigían el rol: un administrador del Colegio A podía borrar una
elección del SENA conociendo su id. Con una sola función compartida, la regla no se olvida en
un controlador.
"""

import uuid

from app.exceptions import ForbiddenError
from app.models import User


def require_same_institution(user: User, institution_id: uuid.UUID) -> None:
    """Lanza `ForbiddenError` si el usuario no pertenece a la institución del recurso.

    Un usuario sin institución (aún no se vinculó con un código) tampoco tiene acceso.
    """
    if user.institution_id is None or user.institution_id != institution_id:
        raise ForbiddenError("This resource belongs to another institution")
