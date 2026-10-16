# HU-022 — Gestionar candidaturas (docente)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-022.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-022                          |
| **Requisito** | [RF-022](../RFs/RF-022_gestionar_candidaturas_docente.md) |
| **Rol**       | Docente                           |

## Historia

Como Docente quiero administrar los candidatos registrados, asi como su informacion especifica con el fin de auditar y administrar el procesos electoral de la intitucion.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Accede al módulo de gestión de candidatos dentro del proceso electoral activo | completa el formulario con los datos del candidato (nombre, curso, propuesta, foto) y confirma | registra al candidato, lo hace visible en la lista y lo habilita para recibir votos |
| 2 | Detecta un error o cambio en los datos de un candidato ya registrado | selecciona el candidato, modifica los campos necesarios y guarda los cambios | actualiza la información del candidato y refleja los cambios de forma inmediata en la plataforma |
| 3 | El docente necesita retirar a un candidato que no cumple los requisitos del proceso electoral | selecciona la opción 'Eliminar' sobre el candidato y confirma la acción | elimina al candidato del proceso, remueve su perfil de la votación y registra la operación |
| 4 | Al revisar el estado y la información de todos los candidatos inscritos | accede al listado de candidatos y aplica filtros por curso, estado o nombre si lo necesita | muestra la lista actualizada de candidatos con su información y estado dentro del proceso |
