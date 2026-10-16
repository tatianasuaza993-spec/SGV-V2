# HU-014 — Exportar resultados (administrador)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-014.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-014                          |
| **Requisito** | [RF-014](../RFs/RF-014_exportar_resultados_administrador.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador necesito Exportar los resultados de las elecciones con la finalidad de descargar y generar consolidados de las elecciones.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | El admin desea resultados en formato Excel | Selecciona formato Excel y presiona "Descargar" | Se descarga archivo .xlsx con todos los datos |
| 2 | Se requiere formato PDF para acta oficial | Selecciona PDF y presiona "Exportar" | Se genera PDF con formato profesional y datos completos |
| 3 | Se necesita certeza de los resultados | Marca opción "Incluir certificados" | El documento incluye códigos de verificación de votos |
| 4 | El admin desea customizar el reporte | Marca/desmarca datos (nombres, votos, porcentajes) | El reporte incluye solo los datos seleccionados |
