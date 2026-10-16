# RF-033 — Registrar candidatura

<!--
  ¿Qué? Requisito funcional RF-033 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-033                       |
| **Nombre**    | Registrar candidatura |
| **Módulo**    | Candidato |
| **Prioridad** | Alta (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-033](../HUs/HU-033_registrar_candidatura.md) |

---

## Descripción

El sistema debe permitir al candidato inscribirse a un cargo (personero, contralor, representante, etc.) en una elección abierta, diligenciando sus datos y propuestas, y dejando la candidatura en estado pendiente de aprobación.

---

## Reglas de negocio

- La candidatura nace en estado «pendiente» (H12).
- Solo se puede inscribir en una elección que aún no ha iniciado y es de su institución.
