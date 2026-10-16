# RF-022 — Gestionar candidaturas (docente)

<!--
  ¿Qué? Requisito funcional RF-022 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-022                       |
| **Nombre**    | Gestionar candidaturas (docente) |
| **Módulo**    | Docente |
| **Prioridad** | Media (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-022](../HUs/HU-022_gestionar_candidaturas_docente.md) |

---

## Descripción

El sistema debe permitir al docente revisar, agregar, editar, aprobar o rechazar las candidaturas inscritas en una elección, validando que cumplan los requisitos y notificando al candidato el estado actualizado de su postulación.

---

## Reglas de negocio

- Comparte el modelo de estados de candidatura del RF-017 (H12).
- El docente solo actúa sobre elecciones de su institución (H1).
