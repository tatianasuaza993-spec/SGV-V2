# HU-036 — Ver estado de candidatura

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-036.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-036                          |
| **Requisito** | [RF-036](../RFs/RF-036_ver_estado_de_candidatura.md) |
| **Rol**       | Candidato                           |

## Historia

Como Candidato Deseo vizualizar el estado de mi candidatura.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | Acaba de postularse | Accede a su perfil de candidato | Muestra estado "Pendiente de revisión" |
| 2 | El admin aprobó | Accede a su perfil | Muestra estado "Aprobado" en color verde |
| 3 | El admin rechazó | Accede a su perfil | Muestra estado "Rechazado" con motivo del rechazo |
| 4 | Quiere ver cambios | Ve sección de historial | Muestra registro de cambios de estado con fechas |
