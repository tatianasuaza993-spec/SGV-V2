# HU-016 — Enviar notificaciones (administrador)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-016.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-016                          |
| **Requisito** | [RF-016](../RFs/RF-016_enviar_notificaciones_administrador.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador enviar notificaciones acerca de las elecciones, estados, y observaciones a los usuarios de la plataforma con la finalidad de informar y dar aviso sobre asuntos importantes de la eleccion y del sistema.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | El admin debe notificar sobre una elección | Redacta mensaje y selecciona "Enviar a todos" | Todos los usuarios reciben la notificación por correo y en el sistema |
| 2 | Solo docentes deben recibir una notificación | Selecciona rol "Docente" y envía | Solo los docentes reciben la notificación |
| 3 | Desea que se envíe en fecha específica | Selecciona fecha/hora y presiona "Programar" | La notificación se envía automáticamente en la fecha indicada |
| 4 | Necesita revisar qué se comunicó | Accede a "Historial de notificaciones" | Ve registro completo de todas las notificaciones enviadas |
