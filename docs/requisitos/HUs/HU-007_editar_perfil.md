# HU-007 — Editar perfil

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-007.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-007                          |
| **Requisito** | [RF-007](../RFs/RF-007_editar_perfil.md) |
| **Rol**       | Usuario                           |

## Historia

Como Usuario necesito administrar mis datos personales con la finalidad de tener mi perfil actualizado.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | el usuario desee visualizar su informacion personal | presione el icono de perfil | debe permitir el acceso a su informacion |
| 2 | seleccione un criterio a modificar | presionar un campo | debe permitir la modificacion de la misma y su actualizacion |
| 3 | intente cambiar su contraseña | Accione el campo de cambio de contraseña | debe realizar un mensaje de confirmacion y posteriormente efectuar su cambio |
| 4 | desea borrar su cuenta | Acciona el icono de borrar cuenta | El sistema elimina su cuenta con previa confirmacion y aceptaciom del admin |
