# HU-028 — Obtener certificado electoral

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-028.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-028                          |
| **Requisito** | [RF-028](../RFs/RF-028_obtener_certificado_electoral.md) |
| **Rol**       | Estudiante                           |

## Historia

Como Estudiante Necesito Obtener mi certificado Electoral.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Mensaje de confirmación 'Su votación fue enviada exitosamente' visible en pantalla | Presionar el botón 'Imprimir certificado electoral' | Generado y descargado un PDF con el comprobante oficial de participación electoral |
| 2 | Confirmación de voto exitosa en pantalla | Seleccionar la opción de vista previa antes de descargar | Desplegada una previsualización del certificado con los datos del votante y la elección |
| 3 | PDF del certificado descargado exitosamente | Abrir el archivo generado y revisar los datos | Certificado muestra nombre, fecha, institución y nombre de la elección sin errores |
| 4 | Mensaje de voto exitoso con botón de certificado visible | Cerrar la pantalla sin presionar el botón de imprimir | Sesión continúa normalmente sin generar el certificado; opción disponible desde el historial |
