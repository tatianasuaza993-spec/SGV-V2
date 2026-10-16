# RF-017 — Gestionar candidatos (administrador)

<!--
  ¿Qué? Requisito funcional RF-017 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-017                       |
| **Nombre**    | Gestionar candidatos (administrador) |
| **Módulo**    | Administrador |
| **Prioridad** | Alta (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-017](../HUs/HU-017_gestionar_candidatos_administrador.md) |

---

## Descripción

El sistema debe permitir al administrador revisar, aprobar, rechazar, editar o retirar candidaturas de una elección, consultando sus propuestas y datos, y notificando al candidato el resultado de cada decisión tomada.

---

## Reglas de negocio

- Una candidatura tiene estado: pendiente, aprobada, rechazada o retirada (H12).
- Solo se puede votar por candidaturas aprobadas.
- El rechazo exige observaciones para que el candidato pueda corregir.
