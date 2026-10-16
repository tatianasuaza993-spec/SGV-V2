# HU-004 — Recuperar contraseña

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-004.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-004                          |
| **Requisito** | [RF-004](../RFs/RF-004_recuperar_contrasena.md) |
| **Rol**       | Usuario                           |

## Historia

Como Usuario necesito recuperar mi contraseña con la finalidad de volver a ingresar al sistema en caso de olvidarla.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | el correo exista | solicite recuperación | debe enviar enlace de recuperación |
| 2 | el correo no exista | intente recuperar contraseña | debe mostrar mensaje de error |
| 3 | la nueva contraseña sea válida | el usuario la confirme | debe actualizarla |
| 4 | el enlace expire | el usuario intente usarlo | debe solicitar una nueva solicitud |
