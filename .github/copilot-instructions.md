# 🎓 Instrucciones del Proyecto — SGV (Sistema de Gestión de Votaciones)

<!--
  ¿Qué? Reglas, convenciones y decisiones técnicas del proyecto SGV.
  ¿Para qué? Que cualquier integrante (o herramienta de IA) escriba código y documentación
  consistentes con el resto del repositorio.
  ¿Impacto? Sin una fuente única de reglas, cada persona decide distinto y el proyecto pierde
  coherencia, calidad y trazabilidad.
-->

> La estructura, las convenciones y el flujo de trabajo se basan en el proyecto de referencia
> [`ergrato-dev/proyecto-be_fastapi-fe_react`](https://github.com/ergrato-dev/proyecto-be_fastapi-fe_react)
> (CC BY-NC-SA 4.0). El código de SGV se escribe desde cero.

---

## 1. Identidad del proyecto

| Campo          | Valor                                                                                   |
| -------------- | --------------------------------------------------------------------------------------- |
| **Nombre**     | SGV — Sistema de Gestión de Votaciones                                                  |
| **Tipo**       | Proyecto educativo — SENA, Tecnólogo en ADSO                                            |
| **Propósito**  | Gestionar elecciones del gobierno escolar con seguridad, transparencia y secreto del voto |
| **Equipo**     | Sandy Tatiana Suaza Ramos y Santiago Alejandro Peña Gironza                              |
| **Alcance**    | 39 requisitos funcionales — ver [`docs/requisitos/`](../docs/requisitos/README.md)       |

---

## 2. Stack tecnológico

| Capa              | Tecnología                                                                  |
| ----------------- | --------------------------------------------------------------------------- |
| **Backend**       | Python 3.12+, FastAPI, SQLAlchemy 2.0, Alembic, Pydantic 2, JWT, bcrypt     |
| **Frontend**      | React, Vite, TypeScript (strict), TailwindCSS 4, React Router 7, i18next    |
| **Base de datos** | PostgreSQL 17 en contenedor Docker                                          |
| **Correo (dev)**  | Mailpit (SMTP local, interfaz en el puerto 8025)                            |
| **Pruebas**       | pytest + httpx (backend), Vitest + Testing Library (frontend), Playwright   |
| **Calidad**       | ruff (Python), ESLint + Prettier (TypeScript)                               |
| **Contenedores**  | Docker Compose: `db`, `db-test`, `be`, `fe`, `mailpit`                      |
| **CI**            | GitHub Actions en cada pull request                                         |

---

## 3. Reglas de idioma — obligatorias

- **Inglés** para todo lo técnico: variables, funciones, clases, archivos de código, endpoints,
  tablas y columnas, mensajes de commit y nombres de ramas.
- **Español** para comentarios, docstrings, documentación (`.md`) y textos visibles de la
  interfaz en el idioma por defecto.
- Todo comentario significativo responde tres preguntas: **¿Qué? ¿Para qué? ¿Impacto?**
- Cada archivo nuevo empieza con una cabecera que explica el módulo.

```python
# ✅ Correcto
def get_election_by_id(election_id: UUID) -> Election: ...

# ❌ Incorrecto (nombres técnicos en español)
def obtener_eleccion_por_id(id_eleccion): ...
```

---

## 4. Herramientas y dependencias — obligatorias

- **Python:** entorno con `venv` gestionado por **`uv`** (`uv sync`, `uv add "paquete==X.Y.Z"`).
  Nunca `pip install` directo ni conda, pipenv o poetry.
- **Node.js:** siempre **`pnpm`**. Nunca `npm` ni `yarn` (genera locks que rompen el repo).
- **Versiones exactas siempre.** Sin `^`, `~`, `>=` ni `*` en `pyproject.toml` ni `package.json`.
  Los locks (`uv.lock`, `pnpm-lock.yaml`) se commitean.
- Al agregar una dependencia: auditar (`uv run pip-audit`, `pnpm audit`).
- **Variables de entorno:** nunca hardcodear URLs, claves ni orígenes CORS. Se leen de `.env`
  (no versionado) y se valida su presencia al arrancar. Siempre hay un `.env.example` al día.

---

## 5. Estructura del repositorio

```
SGV-V2/
├── .github/            # reglas, plantillas de issue y PR, workflows de CI
├── docs/               # requisitos, referencia técnica, setup, colaboración, testing
├── be/                 # backend FastAPI
│   ├── app/            # routers, services, models, schemas, utils, tests
│   └── alembic/        # migraciones
├── fe/                 # frontend React
│   └── src/            # api, components, pages, hooks, context, locales, types
├── e2e/                # pruebas Playwright
├── docker-compose.yml
└── README.md
```

---

## 6. Convenciones de código

| Aspecto            | Regla                                                           |
| ------------------ | --------------------------------------------------------------- |
| Python             | PEP 8, type hints obligatorios, docstrings en español, ruff     |
| TypeScript         | `strict: true`, componentes funcionales, ESLint + Prettier      |
| Capas del backend  | router (HTTP) → service (lógica) → model (datos); sin SQL crudo |
| Base de datos      | tablas en plural `snake_case`, PK UUID, `created_at`/`updated_at` |
| Migraciones        | siempre con Alembic; nunca alterar la base a mano               |
| API                | prefijo `/api/v1/`, recursos en inglés y en plural              |
| Errores            | excepciones de dominio con su código HTTP en la clase           |
| Registros (logs)   | `logging`, nunca `print`; nunca contraseñas ni tokens           |

---

## 7. Commits y ramas

Formato Conventional Commits, en inglés, con cuerpo What / For / Impact:

```
feat(election): add status transition rules

What: Elections start as "pending" and only move pending → active → finished
For: Requirement RF-009 forbids invalid state changes
Impact: Editing or deleting an active election now returns 409
```

- Tipos: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`, `perf`.
- Ramas: `<tipo>/<issue>-<slug-en-ingles>`, por ejemplo `feat/12-election-states`.
- Nunca se commitea directo a `main`: issue → rama → pull request con `Closes #N` → revisión
  de la otra persona del equipo → squash merge con la CI en verde.

---

## 8. Calidad — obligatoria

- Código que se genera, código que se prueba.
- Cobertura mínima de **80 %** en la lógica de negocio del backend y en los módulos críticos:
  voto, autenticación y resultados.
- La concurrencia del voto (doble envío simultáneo) tiene una prueba propia.
- `ruff check`, `ruff format --check`, `pnpm lint`, `pnpm format:check`, `pnpm build` y las
  pruebas deben pasar antes de pedir revisión.

---

## 9. Reglas del dominio de votación — no negociables

1. **Aislamiento por institución.** Toda operación sobre una elección, candidatura, voto o
   resultado compara la institución del usuario con la de la elección, desde **una sola función
   compartida**. Un administrador o estudiante nunca actúa sobre otra institución.
2. **Un voto por persona y por cargo**, garantizado con una restricción `UNIQUE(user_id,
   position_id)` en `vote_records` y manejando `IntegrityError` (responde 409). La consulta
   previa no basta: dos peticiones simultáneas pasarían ambas.
3. **Voto secreto.** La tabla `votes` no guarda usuario ni fecha, y sus ids son UUID aleatorios.
   La participación se guarda aparte en `vote_records`, ambas en una sola transacción.
4. **Estados.** Elección: `pending → active → finished`. Candidatura: `pending`, `approved`,
   `rejected`, `withdrawn`. Una elección nueva nace en `pending`; no se edita ni se elimina si
   está activa o tiene votos; solo se vota por candidaturas aprobadas.
5. **Tiempo.** Fechas con zona horaria (`TIMESTAMPTZ`) y `datetime.now(timezone.utc)`; el
   frontend las muestra en hora local de Colombia.
6. **Resultados.** Solo con la elección finalizada, de la misma institución y según la
   visibilidad configurada.
7. **Códigos de invitación.** Aleatorios, con rol, vigencia y número de usos; nunca valores
   fijos en el código ni en los seeds.
8. **Errores de base de datos.** Nunca se tratan como "no hay datos": se registran y responden
   500. Nunca se decide el código HTTP buscando texto en un mensaje.
9. **Contraseñas** con bcrypt; nunca en texto plano en código, seeds ni logs. Mensajes de login
   genéricos y límite de intentos.

---

## 10. Diseño de la interfaz

| Aspecto           | Regla                                                              |
| ----------------- | ------------------------------------------------------------------ |
| Temas             | Claro y oscuro con selector                                        |
| Tipografía        | Solo sans-serif                                                    |
| Colores           | Planos, sin degradados; acento **esmeralda** mediante el token `accent-*` |
| Botones de acción | Siempre alineados a la derecha                                     |
| Iconos            | Solo `lucide-react`                                                |
| Responsive        | Mobile-first                                                       |
| Accesibilidad     | Labels en inputs, atributos `aria-*`, contraste WCAG AA            |
| Idiomas           | Español (por defecto) e inglés con `react-i18next`                 |

Los estados de éxito, error, información y advertencia usan sus colores semánticos
(verde, rojo, azul y amarillo), no el de acento.

---

## 11. Reglas para quien genere código con IA

1. Dividir el trabajo en pasos pequeños y verificables.
2. Todo código generado incluye sus pruebas.
3. Respetar idioma, estructura y herramientas de este documento.
4. No inventar requisitos: cada cambio referencia un RF o una HU de `docs/requisitos/`.
5. Cada integrante debe poder explicar el código que presenta como suyo.
