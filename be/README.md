# Backend — SGV

<!--
  ¿Qué? Guía del backend FastAPI del Sistema de Gestión de Votaciones.
  ¿Para qué? Levantar, probar y migrar el backend sin adivinar comandos.
  ¿Impacto? Sin esta guía, cada integrante configuraría el entorno de forma distinta.
-->

## Requisitos

Python 3.12+, [`uv`](https://docs.astral.sh/uv/) y una base PostgreSQL 17 (en el proyecto se
levanta con Docker Compose).

## Primer arranque

```bash
cd be
cp .env.example .env        # y completar SECRET_KEY con un valor aleatorio de 32+ caracteres
uv lock                     # primera vez: genera uv.lock (se commitea)
uv sync
uv run alembic upgrade head
uv run uvicorn app.main:app --reload
# API en http://localhost:8000 · documentación en http://localhost:8000/docs
```

## Pruebas

Las pruebas de base de datos usan una base **exclusiva y desechable** (`TEST_DATABASE_URL`, puerto
5433). Borran y recrean el esquema: nunca apuntar a la base de desarrollo.

```bash
uv run pytest -v
uv run ruff check app/ && uv run ruff format --check app/
```

## Estructura

```
app/
├── config.py        # variables de entorno validadas al arrancar
├── database.py      # motor, sesión y pool de conexiones
├── exceptions.py    # errores de dominio con su código HTTP
├── models/          # tablas (SQLAlchemy 2.0)
├── routers/         # endpoints /api/v1/...
├── services/        # lógica de negocio (incluye la guardia de institución)
└── tests/
alembic/             # migraciones
```
