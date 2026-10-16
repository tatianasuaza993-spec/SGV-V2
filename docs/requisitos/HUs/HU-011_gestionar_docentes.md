# HU-011 — Gestionar docentes

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-011.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-011                          |
| **Requisito** | [RF-011](../RFs/RF-011_gestionar_docentes.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador necesito gestionar la informacion del Personal Docente con el fin de asegurar los permisos y accesos de modificacion dentro de la plataforma.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | accede al perfil de un docente registrado en la plataforma | selecciona los permisos que desea habilitar (ej: gestionar votaciones, ver resultados) | guarda la configuración y el docente obtiene acceso a las funciones asignadas |
| 2 | detecta que un docente ya no debe tener ciertos privilegios de moderación | desmarca los permisos correspondientes y confirma el cambio | actualiza el perfil del docente y restringe las funciones revocadas de forma inmediata |
| 3 | corregir o actualizar datos del perfil de un docente | selecciona 'Editar' en el perfil del docente y modifica los campos necesarios | actualiza los datos del docente y confirma los cambios realizados |
| 4 | remover a un docente que ya no pertenece a la institución | selecciona la opción 'Eliminar' en el perfil del docente y confirma la acción | elimina al docente, revoca todos sus permisos y accesos |
