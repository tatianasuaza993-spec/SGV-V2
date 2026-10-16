# RF-038 — Consultar resultados (candidato)

<!--
  ¿Qué? Requisito funcional RF-038 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-038                       |
| **Nombre**    | Consultar resultados (candidato) |
| **Módulo**    | Candidato |
| **Prioridad** | Media (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-038](../HUs/HU-038_consultar_resultados_candidato.md) |

---

## Descripción

El sistema debe permitir al candidato ver los resultados de la elección en la que participó, incluyendo votos obtenidos y posición, solo cuando la institución haya habilitado la visibilidad de resultados.

---

## Reglas de negocio

- Los resultados solo se muestran con la elección finalizada y según la visibilidad definida (H5).
