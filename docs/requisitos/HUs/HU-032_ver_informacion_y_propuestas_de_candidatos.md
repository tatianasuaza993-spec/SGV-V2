# HU-032 — Ver información y propuestas de candidatos

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-032.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-032                          |
| **Requisito** | [RF-032](../RFs/RF-032_ver_informacion_y_propuestas_de_candidatos.md) |
| **Rol**       | Estudiante                           |

## Historia

Como Estudiante Necesito visualizar la información de los candidatos.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | existan candidatos registrados | el usuario ingrese al módulo | debe mostrar la lista de candidatos |
| 2 | el usuario seleccione un candidato | abra el perfil | debe mostrar información detallada |
| 3 | no existan candidatos | ingrese al módulo | debe mostrar un mensaje informativo |
| 4 | la información sea actualizada | el usuario consulte nuevamente | debe reflejar los cambios |
