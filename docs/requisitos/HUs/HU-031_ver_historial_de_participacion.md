# HU-031 — Ver historial de participación

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-031.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-031                          |
| **Requisito** | [RF-031](../RFs/RF-031_ver_historial_de_participacion.md) |
| **Rol**       | Estudiante                           |

## Historia

Como Estudiante Necesito acceder a mi historias de Elecciones realizadas.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Usuario autenticado en la plataforma con elecciones previas registradas | Navegar a la sección 'Historial de elecciones' desde el menú | Listado de todas las elecciones anteriores en las que se participó, con fecha y nombre |
| 2 | Historial de elecciones cargado en pantalla | Seleccionar una elección del listado para ver su detalle | Vista detallada con los candidatos, resultados y datos del proceso electoral seleccionado |
| 3 | Detalle de una elección pasada abierto | Presionar 'Imprimir certificado electoral' de esa elección | PDF del certificado de participación de esa elección generado y descargado correctamente |
| 4 | Usuario sin elecciones previas registradas accede al historial | Ingresar a la sección de historial de elecciones | Mensaje indicando que aún no se ha participado en ninguna elección |
