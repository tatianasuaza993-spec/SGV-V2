# HU-033 — Registrar candidatura

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-033.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-033                          |
| **Requisito** | [RF-033](../RFs/RF-033_registrar_candidatura.md) |
| **Rol**       | Candidato                           |

## Historia

Como Candidato Deseo postularme mi candidatura a una eleccion proxima.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Hay convocatoria abierta | Completa formulario y presiona "Postularme" | Su candidatura queda registrada en estado pendiente |
| 2 | Hay múltiples cargos disponibles | Elige cargo (personero, contralor, etc.) | Se asigna el cargo seleccionado a su candidatura |
| 3 | Se piden requisitos | Sube archivos solicitados | La documentación se adjunta a su candidatura |
| 4 | Sistema verifica cumplimiento | Sistema evalúa automáticamente | Se indica si cumple o le falta documentación |
