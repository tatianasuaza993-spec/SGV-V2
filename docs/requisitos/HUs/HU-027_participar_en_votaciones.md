# HU-027 — Participar en votaciones

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-027.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-027                          |
| **Requisito** | [RF-027](../RFs/RF-027_participar_en_votaciones.md) |
| **Rol**       | Estudiante                           |

## Historia

Como Estudiante Necesito realizar mi voto de manera digital.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | el usuario seleccione un candidato | confirme su voto | debe registrar el voto correctamente |
| 2 | el usuario ya haya votado | intente votar nuevamente | debe impedir un segundo voto |
| 3 | el voto sea exitoso | finalice el proceso | debe mostrar mensaje de confirmación |
| 4 | envíe el voto | envíe el voto | debe informar el problema |
