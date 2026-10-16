# HU-024 — Exportar resultados (docente)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-024.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-024                          |
| **Requisito** | [RF-024](../RFs/RF-024_exportar_resultados_docente.md) |
| **Rol**       | Docente                           |

## Historia

Como docente Necesito Exportar los resultados de las elecciones.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | El admin desea resultados en formato Excel | Selecciona formato Excel y presiona "Descargar" | Se descarga archivo .xlsx con todos los datos |
| 2 | Se requiere formato PDF para acta oficial | Selecciona PDF y presiona "Exportar" | Se genera PDF con formato profesional y datos completos |
| 3 | Se necesita certeza de los resultados | Marca opción "Incluir certificados" | El documento incluye códigos de verificación de votos |
| 4 | El admin desea customizar el reporte | Marca/desmarca datos (nombres, votos, porcentajes) | El reporte incluye solo los datos seleccionados |
