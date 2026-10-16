# RF-009 — Gestionar elecciones

<!--
  ¿Qué? Requisito funcional RF-009 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-009                       |
| **Nombre**    | Gestionar elecciones |
| **Módulo**    | Administrador |
| **Prioridad** | Alta (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-009](../HUs/HU-009_gestionar_elecciones.md) |

---

## Descripción

El sistema debe permitir al administrador crear, editar y eliminar elecciones definiendo nombre, cargos, fechas de inicio y cierre y estado, impidiendo modificaciones críticas o eliminaciones cuando la elección ya esté en curso o tenga votos registrados.

---

## Reglas de negocio

- Una elección nueva nace en estado «Pendiente».
- Las transiciones de estado válidas son Pendiente → Activa → Finalizada.
- No se puede editar ni eliminar una elección activa o con votos registrados (H4).
- Solo el administrador de la misma institución puede actuar sobre la elección (H1).
- Las fechas se guardan con zona horaria en UTC y se muestran en hora local (H8).
