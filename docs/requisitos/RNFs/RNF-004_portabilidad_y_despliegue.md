# RNF-004 — Portabilidad y despliegue

<!--
  ¿Qué? Requisito no funcional de portabilidad y despliegue.
  ¿Para qué? Que el sistema arranque igual en cualquier computador y se pueda desplegar.
  ¿Impacto? Sin contenedores ni configuración por ambiente, "en mi máquina funciona" invalida la entrega.
-->

| Campo      | Valor                                              |
| ---------- | -------------------------------------------------- |
| **ID**     | RNF-004                                            |
| **Estado** | Propuesto — pendiente de validar con el instructor |
| **Origen** | Ítems 7 a 9 de la lista de chequeo T7              |

## Criterios

1. `docker compose up` levanta base de datos, API y frontend en un computador limpio.
2. La URL de la API, los orígenes CORS y las claves se configuran por variables de entorno.
3. Fechas en UTC con zona horaria, para que el servidor de despliegue no desfase las votaciones.
4. Manual de instalación técnico y manual de usuario con capturas.
5. Estrategia de copias de seguridad (`pg_dump` programado) y procedimiento de restauración.
6. Restricción RO-005: el despliegue fuera del equipo local está por confirmar con el instructor.
