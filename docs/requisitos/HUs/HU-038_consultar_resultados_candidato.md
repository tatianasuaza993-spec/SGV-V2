# HU-038 — Consultar resultados (candidato)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-038.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-038                          |
| **Requisito** | [RF-038](../RFs/RF-038_consultar_resultados_candidato.md) |
| **Rol**       | Candidato                           |

## Historia

Como Candidato Necesito ver Resultados de las Elecciones (cuando finalicen).

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | La votación finalizó | Accede a "Ver resultados" | Muestra votos obtenidos y posición en el ranking |
| 2 | Quiere conocer el total | Consulta sus resultados | Muestra número exacto de votos recibidos |
| 3 | Analiza representatividad | Ve estadísticas | Muestra % de votos respecto al total de votantes |
| 4 | Análisis competitivo | Ve ranking completo | Muestra posición y votos de todos los candidatos |
