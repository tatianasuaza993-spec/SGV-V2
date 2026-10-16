# Requisitos del SGV

<!--
  ¿Qué? Índice de los 39 requisitos funcionales y sus historias de usuario.
  ¿Para qué? Tener una sola fuente de verdad del alcance del proyecto.
  ¿Impacto? Sin un índice único, el README y los demás documentos se contradicen (hallazgo H14).
-->

Total: **39 requisitos funcionales**. Las prioridades son una propuesta del equipo y orientan el orden de construcción.

| ID | Requisito | Módulo | Prioridad | Estado | Historia |
| -- | --------- | ------ | --------- | ------ | -------- |
| [RF-001](RFs/RF-001_consultar_informacion_general_del_sistema.md) | Consultar información general del sistema | Visitante y cuenta | Media | Pendiente | [HU-001](HUs/HU-001_consultar_informacion_general_del_sistema.md) |
| [RF-002](RFs/RF-002_registrar_administradores_y_docentes.md) | Registrar administradores y docentes | Visitante y cuenta | Alta | Pendiente | [HU-002](HUs/HU-002_registrar_administradores_y_docentes.md) |
| [RF-003](RFs/RF-003_iniciar_sesion.md) | Iniciar sesión | Visitante y cuenta | Alta | Pendiente | [HU-003](HUs/HU-003_iniciar_sesion.md) |
| [RF-004](RFs/RF-004_recuperar_contrasena.md) | Recuperar contraseña | Visitante y cuenta | Media | Pendiente | [HU-004](HUs/HU-004_recuperar_contrasena.md) |
| [RF-005](RFs/RF-005_contactar_soporte.md) | Contactar soporte | Visitante y cuenta | Baja | Pendiente | [HU-005](HUs/HU-005_contactar_soporte.md) |
| [RF-006](RFs/RF-006_unirse_a_institucion_con_codigo.md) | Unirse a institución con código | Visitante y cuenta | Alta | Pendiente | [HU-006](HUs/HU-006_unirse_a_institucion_con_codigo.md) |
| [RF-007](RFs/RF-007_editar_perfil.md) | Editar perfil | Visitante y cuenta | Media | Pendiente | [HU-007](HUs/HU-007_editar_perfil.md) |
| [RF-008](RFs/RF-008_cerrar_sesion.md) | Cerrar Sesion | Visitante y cuenta | Alta | Pendiente | [HU-008](HUs/HU-008_cerrar_sesion.md) |
| [RF-009](RFs/RF-009_gestionar_elecciones.md) | Gestionar elecciones | Administrador | Alta | Pendiente | [HU-009](HUs/HU-009_gestionar_elecciones.md) |
| [RF-010](RFs/RF-010_gestionar_usuarios.md) | Gestionar usuarios | Administrador | Alta | Pendiente | [HU-010](HUs/HU-010_gestionar_usuarios.md) |
| [RF-011](RFs/RF-011_gestionar_docentes.md) | Gestionar docentes | Administrador | Baja | Pendiente | [HU-011](HUs/HU-011_gestionar_docentes.md) |
| [RF-012](RFs/RF-012_cargar_estudiantes_masivamente.md) | Cargar estudiantes masivamente | Administrador | Media | Pendiente | [HU-012](HUs/HU-012_cargar_estudiantes_masivamente.md) |
| [RF-013](RFs/RF-013_ver_estadisticas_de_las_elecciones.md) | Ver estadísticas de las Elecciones | Administrador | Media | Pendiente | [HU-013](HUs/HU-013_ver_estadisticas_de_las_elecciones.md) |
| [RF-014](RFs/RF-014_exportar_resultados_administrador.md) | Exportar resultados (administrador) | Administrador | Baja | Pendiente | [HU-014](HUs/HU-014_exportar_resultados_administrador.md) |
| [RF-015](RFs/RF-015_configurar_parametros_del_sistema.md) | Configurar parámetros del sistema | Administrador | Media | Pendiente | [HU-015](HUs/HU-015_configurar_parametros_del_sistema.md) |
| [RF-016](RFs/RF-016_enviar_notificaciones_administrador.md) | Enviar notificaciones (administrador) | Administrador | Baja | Pendiente | [HU-016](HUs/HU-016_enviar_notificaciones_administrador.md) |
| [RF-017](RFs/RF-017_gestionar_candidatos_administrador.md) | Gestionar candidatos (administrador) | Administrador | Alta | Pendiente | [HU-017](HUs/HU-017_gestionar_candidatos_administrador.md) |
| [RF-018](RFs/RF-018_gestionar_codigos_de_invitacion.md) | Gestionar códigos de invitación | Administrador | Alta | Pendiente | [HU-018](HUs/HU-018_gestionar_codigos_de_invitacion.md) |
| [RF-019](RFs/RF-019_gestionar_votaciones_docente.md) | Gestionar votaciones (docente) | Docente | Media | Pendiente | [HU-019](HUs/HU-019_gestionar_votaciones_docente.md) |
| [RF-020](RFs/RF-020_ver_votaciones_activas.md) | Ver votaciones activas | Docente | Media | Pendiente | [HU-020](HUs/HU-020_ver_votaciones_activas.md) |
| [RF-021](RFs/RF-021_ver_resultados_docente.md) | Ver resultados (docente) | Docente | Media | Pendiente | [HU-021](HUs/HU-021_ver_resultados_docente.md) |
| [RF-022](RFs/RF-022_gestionar_candidaturas_docente.md) | Gestionar candidaturas (docente) | Docente | Media | Pendiente | [HU-022](HUs/HU-022_gestionar_candidaturas_docente.md) |
| [RF-023](RFs/RF-023_gestionar_estudiantes_votantes.md) | Gestionar estudiantes votantes | Docente | Media | Pendiente | [HU-023](HUs/HU-023_gestionar_estudiantes_votantes.md) |
| [RF-024](RFs/RF-024_exportar_resultados_docente.md) | Exportar resultados (docente) | Docente | Baja | Pendiente | [HU-024](HUs/HU-024_exportar_resultados_docente.md) |
| [RF-025](RFs/RF-025_enviar_y_recibir_notificaciones_docente.md) | Enviar y recibir notificaciones (docente) | Docente | Baja | Pendiente | [HU-025](HUs/HU-025_enviar_y_recibir_notificaciones_docente.md) |
| [RF-026](RFs/RF-026_ver_votaciones_disponibles.md) | Ver votaciones disponibles | Estudiante | Alta | Pendiente | [HU-026](HUs/HU-026_ver_votaciones_disponibles.md) |
| [RF-027](RFs/RF-027_participar_en_votaciones.md) | Participar en votaciones | Estudiante | Alta | Pendiente | [HU-027](HUs/HU-027_participar_en_votaciones.md) |
| [RF-028](RFs/RF-028_obtener_certificado_electoral.md) | Obtener certificado electoral | Estudiante | Media | Pendiente | [HU-028](HUs/HU-028_obtener_certificado_electoral.md) |
| [RF-029](RFs/RF-029_ver_estados_y_resultados_estudiante.md) | Ver estados y resultados (estudiante) | Estudiante | Media | Pendiente | [HU-029](HUs/HU-029_ver_estados_y_resultados_estudiante.md) |
| [RF-030](RFs/RF-030_recibir_notificaciones_estudiante.md) | Recibir notificaciones (estudiante) | Estudiante | Baja | Pendiente | [HU-030](HUs/HU-030_recibir_notificaciones_estudiante.md) |
| [RF-031](RFs/RF-031_ver_historial_de_participacion.md) | Ver historial de participación | Estudiante | Media | Pendiente | [HU-031](HUs/HU-031_ver_historial_de_participacion.md) |
| [RF-032](RFs/RF-032_ver_informacion_y_propuestas_de_candidatos.md) | Ver información y propuestas de candidatos | Estudiante | Alta | Pendiente | [HU-032](HUs/HU-032_ver_informacion_y_propuestas_de_candidatos.md) |
| [RF-033](RFs/RF-033_registrar_candidatura.md) | Registrar candidatura | Candidato | Alta | Pendiente | [HU-033](HUs/HU-033_registrar_candidatura.md) |
| [RF-034](RFs/RF-034_editar_perfil_de_candidatura.md) | Editar perfil de candidatura | Candidato | Media | Pendiente | [HU-034](HUs/HU-034_editar_perfil_de_candidatura.md) |
| [RF-035](RFs/RF-035_retirar_candidatura.md) | Retirar candidatura | Candidato | Media | Pendiente | [HU-035](HUs/HU-035_retirar_candidatura.md) |
| [RF-036](RFs/RF-036_ver_estado_de_candidatura.md) | Ver estado de candidatura | Candidato | Alta | Pendiente | [HU-036](HUs/HU-036_ver_estado_de_candidatura.md) |
| [RF-037](RFs/RF-037_recibir_notificaciones_candidato.md) | Recibir notificaciones (candidato) | Candidato | Baja | Pendiente | [HU-037](HUs/HU-037_recibir_notificaciones_candidato.md) |
| [RF-038](RFs/RF-038_consultar_resultados_candidato.md) | Consultar resultados (candidato) | Candidato | Media | Pendiente | [HU-038](HUs/HU-038_consultar_resultados_candidato.md) |
| [RF-039](RFs/RF-039_ver_calendario_electoral.md) | Ver calendario electoral | Candidato | Media | Pendiente | [HU-039](HUs/HU-039_ver_calendario_electoral.md) |

Otros documentos: [restricciones](restricciones.md) y [requisitos no funcionales](RNFs/).
