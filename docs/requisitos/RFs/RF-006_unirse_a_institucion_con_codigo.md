# RF-006 — Unirse a institución con código

<!--
  ¿Qué? Requisito funcional RF-006 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-006                       |
| **Nombre**    | Unirse a institución con código |
| **Módulo**    | Visitante y cuenta |
| **Prioridad** | Alta (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-006](../HUs/HU-006_unirse_a_institucion_con_codigo.md) |

---

## Descripción

El sistema debe permitir a administradores y docentes ingresar un código de invitación para vincularse a una institución, verificando que exista, no haya expirado ni sido usado, y asociando al usuario con dicha institución.

---

## Reglas de negocio

- El código debe existir, estar activo, no haber expirado y tener usos disponibles (H6).
- Al usarse el código se asocia el usuario a la institución con el rol del código.
