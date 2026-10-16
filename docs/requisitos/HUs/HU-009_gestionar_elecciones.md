# HU-009 — Gestionar elecciones

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-009.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-009                          |
| **Requisito** | [RF-009](../RFs/RF-009_gestionar_elecciones.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador necesito crear y configurar elecciones con la finalidad de administrar los procesos electorales del sistema.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | los datos sean válidos | el administrador guarde la información | debe guardar la información |
| 2 | la fecha final sea menor a la inicial | intente guardar | debe mostrar error |
| 3 | la elección esté activa | los usuarios ingresen | debe permitir votaciones |
| 4 | la elección finalice | llegue la fecha límite | debe cerrar las votaciones automáticamente |
