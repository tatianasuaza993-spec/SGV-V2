# HU-019 — Gestionar votaciones (docente)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-019.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-019                          |
| **Requisito** | [RF-019](../RFs/RF-019_gestionar_votaciones_docente.md) |
| **Rol**       | Docente                           |

## Historia

Como docente quiero editar y administrar las votaciones creadas de la institucion.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | El docente completa el formulario con datos válidos | Presiona "Crear elección" | Se crea la elección y aparece en el listado |
| 2 | El docente asigna fechas a la elección | Selecciona fecha y hora de inicio/cierre | Las fechas se guardan y el sistema respeta los límites |
| 3 | El docente desea modificar datos de la elección | Abre elección existente y modifica campos | Los cambios se guardan correctamente |
| 4 | El admin desea eliminar una elección | Presiona "Eliminar" y confirma la acción | La elección se elimina después de confirmación |
