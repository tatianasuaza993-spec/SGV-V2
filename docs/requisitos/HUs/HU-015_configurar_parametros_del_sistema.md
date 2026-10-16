# HU-015 — Configurar parámetros del sistema

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-015.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-015                          |
| **Requisito** | [RF-015](../RFs/RF-015_configurar_parametros_del_sistema.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador quiero personalizar el Panel de mi organizacion (aspecto, detalles, informacion).

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | accede a la sección de personalización del panel de su organización | sube una imagen como logo oficial de la institución | almacena el logo y lo muestra en el encabezado del panel y en las pantallas de votación |
| 2 | Al ingresar a personalización visual | selecciona los colores primario y secundario de la institución mediante un selector de color | aplica la paleta de colores elegida en toda la interfaz del panel de la organización |
| 3 | deseo enriquecer visualmente la pantalla de inicio del panel | sube una o más imágenes de banner y define su posición en el panel | despliega las imágenes cargadas en la sección correspondiente del panel institucional |
| 4 | Necesita reflejar datos actualizados de la institución en el panel | edita campos como nombre de la institución, descripción y datos de contacto, luego guarda | actualiza la información y la muestra correctamente en el panel público e interno |
