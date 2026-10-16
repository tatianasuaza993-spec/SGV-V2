# HU-017 — Gestionar candidatos (administrador)

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-017.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-017                          |
| **Requisito** | [RF-017](../RFs/RF-017_gestionar_candidatos_administrador.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador necesito Gestionar los candidatos en el sistema con la finalidad de habilitar su participación en las elecciones.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | los datos sean válidos | el administrador guarde la información | debe registrar el candidato |
| 2 | falte información obligatoria | intente registrar | debe solicitar completar los campos |
| 3 | el candidato ya exista | intente registrarlo nuevamente | debe impedir el registro duplicado |
| 4 | se cargue una foto válida | se guarde el formulario | debe almacenar la imagen correctamente |
