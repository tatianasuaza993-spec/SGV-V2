# HU-018 — Gestionar códigos de invitación

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-018.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-018                          |
| **Requisito** | [RF-018](../RFs/RF-018_gestionar_codigos_de_invitacion.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador necesito generar codigos y enlaces de invitacion a la institucion de acuerdo con sus roles con el fin de que los usuarios ingresen a la institucion de acuerdo con su rol especifico.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | accede al módulo de generación de códigos y selecciona el rol 'Votante' | selecciona el curso e indica generar código | generar un código de 6 dígitos único asociado al curso |
| 2 | necesita vincular a un docente a la institución | selecciona el rol 'Docente' e indica generar código para esa persona | generar un código de 6 dígitos único e individual para que el docente ingrese con su rol específico |
| 3 | necesita agregar otro administrador a la plataforma | selecciona el rol 'Administrador' e indica generar código | genera un código de 6 dígitos único para ese administrador, garantizando acceso con privilegios completos |
| 4 | El administrador ha generado uno o varios códigos de invitación | accede al listado de códigos activos y selecciona 'Copiar' en el deseado | mostrar todos los códigos vigentes con su rol asociado y permite copiarlos o compartirlos fácilmente |
