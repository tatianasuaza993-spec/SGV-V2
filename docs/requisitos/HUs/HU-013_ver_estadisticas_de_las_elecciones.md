# HU-013 — Ver estadísticas de las Elecciones

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-013.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-013                          |
| **Requisito** | [RF-013](../RFs/RF-013_ver_estadisticas_de_las_elecciones.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador necesito consultar los resultados de las elecciones con la finalidad de conocer el número de votos obtenidos por cada candidato.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | la votación haya finalizado | el administrador consulte resultados | debe mostrar el conteo de votos |
| 2 | existan empates | se visualicen los resultados | debe indicarlo claramente |
| 3 | no existan votos | se consulte el reporte | debe mostrar valores en cero |
| 4 | el administrador exporte resultados | presione descargar | debe generar el archivo correctamente |
