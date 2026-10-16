# RF-018 — Gestionar códigos de invitación

<!--
  ¿Qué? Requisito funcional RF-018 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-018                       |
| **Nombre**    | Gestionar códigos de invitación |
| **Módulo**    | Administrador |
| **Prioridad** | Alta (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-018](../HUs/HU-018_gestionar_codigos_de_invitacion.md) |

---

## Descripción

El sistema debe permitir al administrador generar, consultar, desactivar y renovar códigos de invitación únicos para vincular docentes y administradores a la institución, definiendo rol, vigencia y número de usos permitidos.

---

## Reglas de negocio

- Los códigos son aleatorios, únicos, con rol, vigencia y número de usos (H6).
- Un código se puede desactivar y renovar sin borrar su historial de uso.
