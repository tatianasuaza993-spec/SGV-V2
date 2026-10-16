# Restricciones del proyecto — SGV

<!--
  ¿Qué? Restricciones técnicas, de herramientas, de diseño y organizacionales del SGV.
  ¿Para qué? Fijar los límites no negociables bajo los que se desarrolla el sistema.
  ¿Impacto? Violar una restricción compromete la calidad, la seguridad o la coherencia.
-->

---

## 1. Tecnológicas

| ID     | Restricción                                                                                   |
| ------ | --------------------------------------------------------------------------------------------- |
| RT-001 | Backend solo con Python 3.12+, FastAPI, SQLAlchemy 2.0+, Alembic y Pydantic 2+.                |
| RT-002 | Frontend solo con React, TypeScript en modo estricto, Vite, TailwindCSS 4+ y React Router 7+.  |
| RT-003 | Base de datos PostgreSQL 17+, en contenedor Docker durante el desarrollo.                     |
| RT-004 | Autenticación solo con JWT sin estado (token de acceso corto y token de renovación).           |
| RT-005 | Contraseñas solo con bcrypt.                                                                  |

## 2. Herramientas y entorno

| ID     | Restricción                                                                                    |
| ------ | ---------------------------------------------------------------------------------------------- |
| RH-001 | Python con `venv` gestionado por `uv`. Prohibido conda, pipenv y poetry.                        |
| RH-002 | Node.js solo con `pnpm`. Prohibido `npm` y `yarn`.                                              |
| RH-003 | Python se valida con `ruff` (lint y formato).                                                   |
| RH-004 | TypeScript se valida con ESLint y Prettier.                                                     |
| RH-005 | Dependencias con versión exacta y lock commiteado. Prohibido `^`, `~`, `>=` y `*`.              |

## 3. Diseño visual

| ID     | Restricción                                                          |
| ------ | -------------------------------------------------------------------- |
| RD-001 | Sin degradados: colores sólidos y planos.                            |
| RD-002 | Solo tipografías sans-serif.                                         |
| RD-003 | Botones de acción siempre alineados a la derecha.                    |
| RD-004 | Iconos solo con `lucide-react`.                                      |
| RD-005 | Color de acento esmeralda mediante el token `accent-*`; nunca una clase de color concreta para elementos de marca. |

## 4. Idioma

| ID     | Restricción                                                                                        |
| ------ | -------------------------------------------------------------------------------------------------- |
| RI-001 | Código, endpoints, tablas, columnas, commits y ramas en inglés.                                     |
| RI-002 | Comentarios, docstrings y documentación en español con el formato ¿Qué? ¿Para qué? ¿Impacto?       |

## 5. Organizacionales

| ID     | Restricción                                                                                          |
| ------ | ---------------------------------------------------------------------------------------------------- |
| RO-001 | Proyecto educativo del SENA: cada decisión técnica se explica y cada integrante la puede sustentar.   |
| RO-002 | Commits con Conventional Commits y cuerpo What / For / Impact.                                        |
| RO-003 | API bajo el prefijo `/api/v1/`.                                                                       |
| RO-004 | Nadie sube directo a `main`: issue → rama → pull request → revisión de la otra persona → merge.       |
| RO-005 | **Despliegue: por confirmar con el instructor.** La referencia lo excluye, pero la lista de chequeo T7 (ítem 7) pide una versión desplegada fuera del equipo local. Mientras tanto la configuración se mantiene por variables de entorno para poder desplegar. |

## 6. Seguridad

| ID     | Restricción                                                                                   |
| ------ | --------------------------------------------------------------------------------------------- |
| RS-001 | Credenciales y configuración sensible solo en `.env` (no versionado).                          |
| RS-002 | `.env.example` siempre actualizado y sin valores reales.                                       |
| RS-003 | Las contraseñas nunca aparecen en respuestas, logs ni mensajes de error.                       |
| RS-004 | El voto es secreto: la base de datos no permite vincular un voto con quien lo emitió.          |
| RS-005 | Ningún usuario actúa sobre datos de otra institución.                                          |
