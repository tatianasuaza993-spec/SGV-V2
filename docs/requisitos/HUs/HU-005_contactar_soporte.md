# HU-005 — Contactar soporte

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-005.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-005                          |
| **Requisito** | [RF-005](../RFs/RF-005_contactar_soporte.md) |
| **Rol**       | Usuario                           |

## Historia

Como Usuario necesito establecer contacto con Soporte tecnico con la finalidad de obtener asistencia tecnica a los problemas que puedan ocurrir con el sistema.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | el usuario desea solicitar soporte | Accionar el icono de soporte | debe de redireccionarlo a la interfaz de soporte |
| 2 | Para digitar informacion basica y relacionada con el problema | llenar los campos necesarios | El sistema guardar la informacion del formulario |
| 3 | el usuario envia la solicitud | Accionar el boton de enviar | E sistema debe recibir la solicitud |
