# RF-002 — Registrar administradores y docentes

<!--
  ¿Qué? Requisito funcional RF-002 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-002                       |
| **Nombre**    | Registrar administradores y docentes |
| **Módulo**    | Visitante y cuenta |
| **Prioridad** | Alta (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-002](../HUs/HU-002_registrar_administradores_y_docentes.md) |

---

## Descripción

El sistema debe ofrecer un formulario de registro para administradores y docentes que solicite nombres, correo, documento y contraseña, valide los datos, evite correos duplicados y cree la cuenta con el rol correspondiente.

---

## Reglas de negocio

- Los roles administrador y docente no se asignan con un código fijo; se vinculan con el RF-006 (H6).
