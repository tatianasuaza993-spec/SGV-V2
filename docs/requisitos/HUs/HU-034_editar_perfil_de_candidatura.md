# HU-034 — Editar perfil de candidatura

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-034.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-034                          |
| **Requisito** | [RF-034](../RFs/RF-034_editar_perfil_de_candidatura.md) |
| **Rol**       | Candidato                           |

## Historia

Como Candidato Necestio Editar mi perfil de Candidatura.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | El candidato necesita cambiar datos | Presiona "Editar perfil" y modifica | Los cambios se guardan correctamente |
| 2 | Desea incluir imagen de campaña | Carga imagen y presiona "Guardar" | La imagen se guarda y se muestra en su perfil |
| 3 | Quiere mejorar sus propuestas | Accede a sección de propuestas y edita | Las propuestas se actualizan (si aún está en plazo) |
| 4 | Pasó la fecha límite | Intenta editar después de cerrada la convocatoria | Sistema muestra "Plazo de edición cerrado" |
