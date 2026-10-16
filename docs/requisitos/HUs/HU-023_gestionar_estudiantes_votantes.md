# HU-023 — Gestionar estudiantes votantes

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-023.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-023                          |
| **Requisito** | [RF-023](../RFs/RF-023_gestionar_estudiantes_votantes.md) |
| **Rol**       | Docente                           |

## Historia

Como docente quiero gestionar a los estudiantes con respecto a sus cursos inscritos.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Panel de gestión de estudiantes con la lista cargada | Seleccionar un estudiante y elegir el nuevo curso en el desplegable disponible | Registro actualizado con el nuevo curso asignado y cambio reflejado en la lista |
| 2 | Estudiante activo visible en el listado del docente | Seleccionar el estudiante y activar la opción 'Inhabilitar' | Estudiante marcado como inactivo, impedido de votar hasta ser habilitado nuevamente |
| 3 | Perfil de estudiante abierto en el panel de gestión | Seleccionar el campo de observaciones, ingresar el texto y guardar | Observación almacenada y visible en el perfil del estudiante para consulta posterior |
| 4 | Módulo de gestión con múltiples cursos disponibles | Seleccionar un curso en el filtro para ver solo sus estudiantes inscritos | Lista filtrada mostrando únicamente los estudiantes del curso seleccionado |
