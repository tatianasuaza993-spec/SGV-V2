# RF-003 — Iniciar sesión

<!--
  ¿Qué? Requisito funcional RF-003 del Sistema de Gestión de Votaciones (SGV).
  ¿Para qué? Dejar por escrito qué debe hacer el sistema y bajo qué reglas.
  ¿Impacto? Sin este requisito no habría criterio claro para construir ni verificar la función.
-->

---

## Identificación

| Campo         | Valor                        |
| ------------- | ---------------------------- |
| **ID**        | RF-003                       |
| **Nombre**    | Iniciar sesión |
| **Módulo**    | Visitante y cuenta |
| **Prioridad** | Alta (propuesta del equipo) |
| **Estado**    | Pendiente                    |
| **Historia**  | [HU-003](../HUs/HU-003_iniciar_sesion.md) |

---

## Descripción

El sistema debe permitir a los usuarios registrados autenticarse con su correo y contraseña, validar las credenciales, informar los errores de acceso de forma clara y redirigir al panel correspondiente según el rol del usuario.

---

## Reglas de negocio

- Los mensajes de error de autenticación son genéricos (H10).
- Hay un límite de intentos de inicio de sesión (H10).
