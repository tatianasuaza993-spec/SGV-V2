# HU-035 — Retirar candidatura

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-035.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-035                          |
| **Requisito** | [RF-035](../RFs/RF-035_retirar_candidatura.md) |
| **Rol**       | Candidato                           |

## Historia

Como Candidato Deseo Retirarme de mi candidatura.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Desiste de participar | Presiona "Retirarme" y confirma | Su candidatura se cancela y se notifica al admin |
| 2 | Debe confirmar la acción | Confirma retiro en diálogo | El retiro es irreversible, candidatura eliminada |
| 3 | Pasó la fecha de retiro | Intenta retirarse después del cierre | Sistema muestra "No se puede retirar a esta hora" |
| 4 | Admin y docentes deben saber | Se procesa el retiro | Se notifica automáticamente a admin y docentes |
