"""
Módulo: main.py
Descripción: Punto de entrada de FastAPI: CORS, manejo de errores y rutas.
¿Para qué? Armar la aplicación con la configuración leída de variables de entorno (H9).
¿Impacto? Los errores de dominio responden con su código HTTP propio (H16) y los errores de la
base de datos se registran y responden 500, nunca como «sin datos» (H7).
"""

import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.config import get_settings
from app.exceptions import DomainError
from app.routers import auth, health, institutions, invitation_codes, users

logger = logging.getLogger(__name__)

API_PREFIX = "/api/v1"


def create_app() -> FastAPI:
    settings = get_settings()
    docs_enabled = settings.environment != "production"
    app = FastAPI(
        title="SGV API",
        version="0.1.0",
        docs_url="/docs" if docs_enabled else None,
        redoc_url=None,
        openapi_url="/openapi.json" if docs_enabled else None,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(DomainError)
    async def handle_domain_error(_: Request, exc: DomainError) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message, "code": exc.code},
        )

    @app.exception_handler(SQLAlchemyError)
    async def handle_database_error(_: Request, exc: SQLAlchemyError) -> JSONResponse:
        logger.exception("Database error", exc_info=exc)
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error", "code": "internal_error"},
        )

    for router in (
        health.router,
        auth.router,
        users.router,
        institutions.router,
        invitation_codes.router,
    ):
        app.include_router(router, prefix=API_PREFIX)
    return app


app = create_app()
