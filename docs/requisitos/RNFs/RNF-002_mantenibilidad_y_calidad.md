# RNF-002 — Mantenibilidad y calidad

<!--
  ¿Qué? Requisito no funcional de mantenibilidad y calidad del SGV.
  ¿Para qué? Que el código sea entendible, probado y verificable de forma automática.
  ¿Impacto? Sin calidad medible, nadie puede demostrar que el sistema funciona ni cambiarlo sin romperlo.
-->

| Campo      | Valor                                                       |
| ---------- | ----------------------------------------------------------- |
| **ID**     | RNF-002                                                     |
| **Estado** | Propuesto — pendiente de validar con el instructor          |
| **Origen** | Ítems 10 a 13 de la lista de chequeo T7                     |

## Criterios

1. Cobertura mínima de 80 % en la lógica de negocio del backend y en voto, autenticación y resultados.
2. Una prueba de concurrencia que intenta emitir dos votos simultáneos y verifica que solo uno se registra.
3. Lint y formato en verde (`ruff`, ESLint, Prettier) en cada pull request.
4. Pipeline de CI que ejecuta lint, build y pruebas en cada pull request.
5. Informe de verificación de calidad con defectos resueltos y pendientes.
6. Una sola fuente de verdad para el número de requisitos y la documentación de instalación.
