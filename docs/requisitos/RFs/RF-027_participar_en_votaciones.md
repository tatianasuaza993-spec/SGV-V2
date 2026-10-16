# RF-027 — Participar en votaciones

<!--
  ¿Qué? Requisito funcional RF-027 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-027                       |
| **Nombre**    | Participar en votaciones |
| **Módulo**    | Estudiante |
| **Prioridad** | Alta (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-027](../HUs/HU-027_participar_en_votaciones.md) |

---

## Descripción

El sistema debe permitir al estudiante emitir su voto por un candidato o voto en blanco dentro de una votación activa, garantizando un solo voto por cargo, el secreto del sufragio y la confirmación del registro exitoso.

---

## Reglas de negocio

- Un voto por persona y por cargo, garantizado con una restricción única en la base de datos (H2).
- El voto no guarda usuario ni fecha; el registro de participación se guarda aparte (H3).
- Voto y registro de participación se escriben en una sola transacción.
- La ventana de votación se valida con la hora del servidor en UTC (H8).
- El estudiante solo vota en elecciones de su institución (H1).
- Un intento de voto repetido responde 409 mediante una excepción de dominio (H16).
