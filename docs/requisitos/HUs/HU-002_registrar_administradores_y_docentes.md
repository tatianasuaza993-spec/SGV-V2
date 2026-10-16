# HU-002 — Registrar administradores y docentes

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-002.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-002                          |
| **Requisito** | [RF-002](../RFs/RF-002_registrar_administradores_y_docentes.md) |
| **Rol**       | Usuario                           |

## Historia

Como usuario necesito registrarme en la plataforma de SGV con la finalidad de poder acceder al sistema y participar en las elecciones.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | el usuario ingrese datos válidos | presione el botón registrarse | debe crear la cuenta exitosamente |
| 2 | intente registrarse | intente registrarse | debe mostrar un mensaje de error |
| 3 | envíe el formulario | envíe el formulario | debe solicitar completar la información |
| 4 | intente continuar | intente continuar | debe pedir una contraseña más segura |
