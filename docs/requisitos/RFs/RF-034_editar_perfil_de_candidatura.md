# RF-034 — Editar perfil de candidatura

<!--
  ¿Qué? Requisito funcional RF-034 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-034                       |
| **Nombre**    | Editar perfil de candidatura |
| **Módulo**    | Candidato |
| **Prioridad** | Media (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-034](../HUs/HU-034_editar_perfil_de_candidatura.md) |

---

## Descripción

El sistema debe permitir al candidato modificar la información de su candidatura, como foto, lema y propuestas, mientras la elección no haya iniciado, y reiniciar la revisión si el cambio lo requiere.

---

## Reglas de negocio

- Solo se edita mientras la elección no haya iniciado; el cambio puede reiniciar la revisión.
