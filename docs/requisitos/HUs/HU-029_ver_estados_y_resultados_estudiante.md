# HU-029 — Ver estados y resultados (estudiante)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-029.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-029                          |
| **Requisito** | [RF-029](../RFs/RF-029_ver_estados_y_resultados_estudiante.md) |
| **Rol**       | Estudiante                           |

## Historia

Como Estudiante Necesito ver Resultados de las Elecciones (cuando finalicen).

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | La elección ha cerrado | Accede a sección de resultados | Ve gráficos con resultados y porcentajes |
| 2 | Hay múltiples cargos en la elección | Selecciona un cargo | Muestra ganador/ganadora del cargo con mayor de votos |
| 3 | Quiere saber cantidad de votantes | Accede a estadísticas | Muestra total de votos, abstenciones y porcentaje de participación |
| 4 | El admin aún no ha publicado resultados | Intenta ver resultados antes del cierre | Muestra mensaje "Resultados no disponibles aún" |
