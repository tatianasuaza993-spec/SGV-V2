# HU-021 — Ver resultados (docente)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-021.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-021                          |
| **Requisito** | [RF-021](../RFs/RF-021_ver_resultados_docente.md) |
| **Rol**       | Docente                           |

## Historia

Como Docente necesito visualizar los resultados y obtener certificados y consolidados.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | accede al módulo de resultados durante una votación en curso | selecciona la opción 'Ver resultados en tiempo real' | muestra un dashboard actualizado con los votos acumulados por candidato en tiempo real |
| 2 | La votación ha finalizado y el docente necesita un informe oficial del proceso | selecciona 'Exportar consolidado' y elige el formato PDF | generar y descargar un archivo PDF con las estadísticas completas, totales y resultados finales |
| 3 | necesita analizar o archivar los datos de la votación en una hoja de cálculo | selecciona 'Exportar consolidado' y elige el formato Excel (.xlsx) | genera y descarga un archivo Excel con todos los datos estadísticos del proceso electoral |
| 4 | El proceso electoral ha concluido y la institución requiere un documento certificado | selecciona la opción 'Generar certificado' al finalizar la votación | genera un certificado descargable con los resultados oficiales, fecha, institución y firma digital del proceso |
