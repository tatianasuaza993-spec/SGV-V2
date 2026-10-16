# RF-035 — Retirar candidatura

<!--
  ¿Qué? Requisito funcional RF-035 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-035                       |
| **Nombre**    | Retirar candidatura |
| **Módulo**    | Candidato |
| **Prioridad** | Media (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-035](../HUs/HU-035_retirar_candidatura.md) |

---

## Descripción

El sistema debe permitir al candidato retirarse voluntariamente de una elección antes de su inicio, solicitando confirmación, cambiando el estado de la candidatura a retirada y notificando a los administradores y docentes responsables.

---

## Reglas de negocio

- Retirar cambia el estado a «retirada» y no ejecuta un borrado (H12).
