# RF-029 — Ver estados y resultados (estudiante)

<!--
  ¿Qué? Requisito funcional RF-029 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-029                       |
| **Nombre**    | Ver estados y resultados (estudiante) |
| **Módulo**    | Estudiante |
| **Prioridad** | Media (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-029](../HUs/HU-029_ver_estados_y_resultados_estudiante.md) |

---

## Descripción

El sistema debe permitir al estudiante consultar el estado de las votaciones (programada, activa o finalizada) y sus resultados, únicamente cuando el administrador o la institución hayan habilitado la visibilidad de resultados.

---

## Reglas de negocio

- Los resultados solo se muestran con la elección finalizada y según la visibilidad definida (H5).
