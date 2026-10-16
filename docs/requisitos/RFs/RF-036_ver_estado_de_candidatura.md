# RF-036 — Ver estado de candidatura

<!--
  ¿Qué? Requisito funcional RF-036 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-036                       |
| **Nombre**    | Ver estado de candidatura |
| **Módulo**    | Candidato |
| **Prioridad** | Alta (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-036](../HUs/HU-036_ver_estado_de_candidatura.md) |

---

## Descripción

El sistema debe mostrar al candidato el estado actual de su candidatura (pendiente, aprobada o rechazada), junto con las observaciones del administrador o docente en caso de rechazo, para que pueda corregirla.

---

## Reglas de negocio

- Muestra el estado y las observaciones del revisor (H12).
