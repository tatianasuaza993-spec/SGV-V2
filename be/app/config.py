"""
Módulo: config.py
Descripción: Configuración de la aplicación leída desde variables de entorno.
¿Para qué? Centralizar y validar la configuración al arrancar, sin valores en el código.
¿Impacto? Sin esto, la URL de la base, la clave JWT y los orígenes CORS quedarían escritos en el
código (hallazgo H9) y una clave débil pasaría sin avisar.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Variables de entorno del backend.

    ¿Qué? Modelo de configuración validado por Pydantic.
    ¿Para qué? Fallar al iniciar si falta una variable o la clave JWT es demasiado corta.
    ¿Impacto? Evita descubrir en producción que la aplicación corría con una clave insegura.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    environment: str = "development"

    # Base de datos
    database_url: str
    test_database_url: str | None = None

    # JWT
    secret_key: str = Field(min_length=32)
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7

    # Navegador: CORS y URL pública del frontend (sin valores por defecto: H9)
    cors_origins: list[str]
    frontend_url: str

    # Correo saliente
    smtp_host: str = "localhost"
    smtp_port: int = 1025
    smtp_from: str = "no-reply@sgv.local"


@lru_cache
def get_settings() -> Settings:
    """Devuelve la configuración (se lee una sola vez)."""
    return Settings()
