# HU-039 — Ver calendario electoral

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-039.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-039                          |
| **Requisito** | [RF-039](../RFs/RF-039_ver_calendario_electoral.md) |
| **Rol**       | Candidato                           |

## Historia

Como Candidato necesito Vizualizar mi Calendario electoral.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | El candidato accede | Selecciona "Ver calendario electoral" | Muestra calendario con todas las fechas importantes |
| 2 | Solo elecciones en que participa | Filtra "Mis elecciones" | Muestra solo fechas de sus candidaturas |
| 3 | No olvide fechas importantes | Sistema envía recordatorios | Recibe notificaciones antes de fechas clave |
| 4 | Quiere tener en su dispositivo | Presiona "Descargar calendario" | Se descarga archivo .ics compatible con calendarios |
