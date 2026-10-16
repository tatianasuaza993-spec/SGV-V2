# HU-030 — Recibir notificaciones (estudiante)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-030.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-030                          |
| **Requisito** | [RF-030](../RFs/RF-030_recibir_notificaciones_estudiante.md) |
| **Rol**       | Estudiante                           |

## Historia

Como Estudiante Quiero Recibir notificaciones del Sistema, Administrador o Docente.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Una votación es abierta | Sistema notifica automáticamente | Recibe alerta en el sistema y por correo |
| 2 | Falta poco para cerrar | A 1 hora del cierre | Recibe notificación de urgencia |
| 3 | Los resultados están listos | Admin publica resultados | Recibe notificación con enlace a resultados |
| 4 | Quiere personalizar avisos | Accede a configuración | Puede elegir qué notificaciones recibir |
