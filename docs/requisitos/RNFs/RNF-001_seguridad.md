# RNF-001 — Seguridad

<!--
  ¿Qué? Requisito no funcional de seguridad del SGV.
  ¿Para qué? Definir las garantías mínimas que debe cumplir un sistema de votación.
  ¿Impacto? Una falla aquí invalida la confianza en todo el proceso electoral.
-->

| Campo      | Valor                                                  |
| ---------- | ------------------------------------------------------ |
| **ID**     | RNF-001                                                |
| **Estado** | Propuesto — pendiente de validar con el instructor     |
| **Origen** | Hallazgos H1, H2, H3, H6 y H10 de la revisión formativa |

## Criterios

1. **Secreto del voto:** con acceso de lectura a la base de datos no se puede unir un voto con su votante (sin usuario, sin fecha y con ids aleatorios en `votes`).
2. **Un voto por cargo:** garantizado por una restricción única en la base de datos, no solo por código.
3. **Aislamiento por institución:** toda operación compara la institución del usuario con la del recurso.
4. **Autenticación:** JWT de corta duración, mensajes de error genéricos y límite de intentos.
5. **Códigos de invitación:** aleatorios, con vigencia y número de usos.
6. **Contraseñas:** bcrypt; nunca en texto plano en seeds, código ni logs.
7. **Configuración:** secretos y orígenes permitidos solo por variables de entorno.
8. **Dependencias:** versiones exactas y auditadas contra vulnerabilidades conocidas.
