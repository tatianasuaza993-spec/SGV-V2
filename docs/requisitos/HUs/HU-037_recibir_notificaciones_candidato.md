# HU-037 — Recibir notificaciones (candidato)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-037.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-037                          |
| **Requisito** | [RF-037](../RFs/RF-037_recibir_notificaciones_candidato.md) |
| **Rol**       | Candidato                           |

## Historia

Como Candidato Quiero Recibir notificaciones del Sistema, Administrador o Docente.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Su candidatura fue aprobada | Sistema envía notificación | Recibe aviso de aprobación por correo y en el sistema |
| 2 | Su candidatura fue rechazada | Sistema envía notificación | Recibe aviso con motivo del rechazo |
| 3 | Admin cambió fechas o datos | Sistema notifica | Recibe alerta de cambios importantes |
| 4 | Quiere personalizar | Accede a configuración | Puede elegir qué notificaciones recibir |
