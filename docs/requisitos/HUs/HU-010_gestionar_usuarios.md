# HU-010 — Gestionar usuarios

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-010.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-010                          |
| **Requisito** | [RF-010](../RFs/RF-010_gestionar_usuarios.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador necesito gestionar los datos de los usuarios vinculados a la plataforma con el fin de ejercer una administracion de los usuarios dentro de la institucion.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | accede al módulo de gestión de usuarios | selecciona la opción 'Ver usuarios' | mostrar la lista de todos los usuarios vinculados a la institución con sus roles |
| 2 | visualiza un usuario existente en el sistema | selecciona 'Editar' sobre el usuario y modifica sus datos | actualizar la información del usuario y muestra confirmación del cambio |
| 3 | identifica un usuario que debe ser removido de la plataforma | selecciona 'Eliminar' sobre el usuario y confirma la acción | eliminar al usuario, revoca su acceso y notifica la operación exitosa |
| 4 | necesita encontrar un usuario específico entre muchos registros | ingresa el nombre o selecciona un filtro por rol en el buscador | filtrar y mostrar únicamente los usuarios que coinciden con el criterio ingresado |
