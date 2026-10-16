# HU-025 — Enviar y recibir notificaciones (docente)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-025.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-025                          |
| **Requisito** | [RF-025](../RFs/RF-025_enviar_y_recibir_notificaciones_docente.md) |
| **Rol**       | Docente                           |

## Historia

Como docente Enviar y Recibir notificaciones acerca de las elecciones y observaciones a los usuarios de la plataforma.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Debe comunicar sobre una votación | Redacta mensaje y presiona "Enviar" | Todos los estudiantes del curso reciben la notificación |
| 2 | El admin envía una circular | El sistema recibe la notificación | Se muestra en la bandeja de notificaciones del docente |
| 3 | Necesita revisar lo enviado | Accede a historial | Ve registro de todas las notificaciones enviadas y recibidas |
| 4 | Leer una notificación recibida | Abre y lee la notificación | Se marca como leída automáticamente |
