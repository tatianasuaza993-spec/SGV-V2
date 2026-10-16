# HU-003 — Iniciar sesión

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-003.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-003                          |
| **Requisito** | [RF-003](../RFs/RF-003_iniciar_sesion.md) |
| **Rol**       | Usuario                           |

## Historia

Como Usuario necesito iniciar sesión en la plataforma con la finalidad de acceder a las funciones del sistema según mi rol.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | las credenciales sean correctas | el usuario inicie sesión | debe permitir el acceso |
| 2 | la contraseña sea incorrecta | intente ingresar | debe mostrar mensaje de error |
| 3 | el usuario no exista | intente ingresar | debe informar que no está registrado |
| 4 | el usuario cierre sesión | presione salir | debe finalizar la sesión correctamente |
