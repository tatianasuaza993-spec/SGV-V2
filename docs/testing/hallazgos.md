# Hallazgos de la revisión formativa y su resolución

<!--
  ¿Qué? Seguimiento de los 16 hallazgos (H1 a H16) de la revisión del repositorio anterior (SGV).
  ¿Para qué? Demostrar qué se corrigió, dónde y con qué prueba, y qué queda pendiente.
  ¿Impacto? Sin este registro no hay evidencia de que los defectos detectados se resolvieron
  (ítems 11 y 12 de la lista de chequeo T7).
-->

Origen: revisión formativa del 16 de octubre de 2026 al repositorio `Gironza/SGV`. Los
hallazgos H9, H10, H11 y H15 se resumen según lo visible en el informe; se amplían cuando se
complete su revisión.

Estados: **Pendiente**, **En curso**, **Resuelto** (con enlace al PR y a la prueba).

| ID  | Severidad | Hallazgo                                                              | Cómo se resuelve en SGV-V2                                                                | Estado    |
| --- | --------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------- |
| H1  | Crítico   | Una institución puede actuar sobre elecciones de otra                 | Función única `require_same_institution` usada por todos los servicios, con pruebas       | Pendiente |
| H2  | Crítico   | El doble voto solo se evita en código                                 | `UNIQUE(user_id, position_id)` en `vote_records`, `IntegrityError` → 409, prueba concurrente | Pendiente |
| H3  | Crítico   | El voto puede vincularse con el votante                               | `votes` sin usuario ni fecha, ids UUID aleatorios                                         | Pendiente |
| H4  | Alto      | Las reglas de RF-009 no están implementadas                           | Estados y transiciones válidas; bloqueo de edición y borrado con votos o elección activa  | Pendiente |
| H5  | Alto      | Resultados visibles para cualquiera y en plena votación               | Resultados solo con elección finalizada, misma institución y visibilidad configurada      | Pendiente |
| H6  | Alto      | Un código fijo convierte a cualquiera en administrador                | Tabla `invitation_codes` con rol, vigencia y usos; códigos aleatorios                     | Pendiente |
| H7  | Alto      | Errores de base de datos confundidos con «no hay datos»               | SQLAlchemy con pool, excepciones, `logging` y respuesta 500                               | Pendiente |
| H8  | Alto      | La ventana de votación depende de la zona horaria del servidor        | `TIMESTAMPTZ` y `datetime.now(timezone.utc)`; hora local solo en el frontend              | Pendiente |
| H9  | Medio     | Configuración escrita en el código (URL de API, CORS, clave JWT)      | Variables de entorno validadas al arrancar con `pydantic-settings`                        | Pendiente |
| H10 | Medio     | Mensajes de login que revelan información, sin límite de intentos     | Mensaje único, errores genéricos hacia el cliente y límite de intentos                    | Pendiente |
| H11 | Medio     | Seeds con contraseñas en texto plano y scripts de hash en el repo     | Seeds con hash ya calculado; pruebas con pytest en lugar de scripts sueltos               | Pendiente |
| H12 | Medio     | Candidaturas sin estados ni aprobación                                | Columna `status` (pendiente, aprobada, rechazada, retirada) y flujo de revisión           | Pendiente |
| H13 | Bajo      | Higiene del repositorio (`.pyc`, sin `.gitignore`, UTF-16)            | `.gitignore` desde el primer commit y archivos en UTF-8                                   | Resuelto  |
| H14 | Bajo      | Documentación que se contradice                                       | Una sola fuente de verdad: [`docs/requisitos/README.md`](../requisitos/README.md)         | En curso  |
| H15 | Bajo      | Piezas del frontend sin terminar (ruta de candidato, cierre de sesión) | Rutas protegidas por rol y cierre de sesión que limpia el estado                          | Pendiente |
| H16 | Bajo      | Códigos HTTP decididos buscando texto en el mensaje                   | Excepciones de dominio con su código HTTP en la clase                                     | Pendiente |
