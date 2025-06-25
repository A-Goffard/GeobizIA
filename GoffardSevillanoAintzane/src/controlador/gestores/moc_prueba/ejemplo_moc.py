from ...dominios.usuario import Usuario
from ...dominios.proyecto import Proyecto
from ...dominios.rol import Rol
from ...dominios.empresa import Empresa
from ...dominios.actividad import Actividad
from ...dominios.participante import Participante
from ...dominios.publicacion import Publicacion
from ...dominios.generadoria import GeneradorIA
from ...dominios.cliente import Cliente
from ...dominios.documento import Documento
from ...dominios.evento import Evento
from ...dominios.factura import Factura
from ...dominios.log_sistema import LogSistema
from ...dominios.auditoria_publicacion import AuditoriaPublicacion
from ...dominios.tags_palabras_clave import Tag
from ...dominios.redsocial import RedSocial
from ...dominios.programacion import Programacion
from ...dominios.recurso_multimedia import RecursoMultimedia
from ...dominios.tema_ambiental import TemaAmbiental
from ...dominios.plantilla import Plantilla

# Ejemplo de datos de persona para los mocks
personas_cargadas = [
    # id_persona, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais
    (1, "Ana", "García", "ana@mail.com", "123456789", "12345678A", "Calle Falsa 123", "28080", "Madrid", "España"),
    (2, "Marta", "López", "marta@mail.com", "33445566D", "33445566D", "Calle Sol 5", "29090", "Málaga", "España"),
    (3, "Carlos", "Ruiz", "carlos@mail.com", "44556677E", "44556677E", "Avenida Paz 10", "50001", "Zaragoza", "España"),
    # ...otros ejemplos...
]

# Usuarios
usuarios_cargados = [
    Usuario.crear_usuario(1, 1, "1990-01-01", "admin", "ninguna", "pass123", "Ana", "García", "ana@mail.com", "123456789", "12345678A", "Calle Falsa 123", "28080", "Madrid", "España"),
    Usuario.crear_usuario(2, 2, "1992-03-15", "user", "viajes", "pass321", "Marta", "López", "marta@mail.com", "33445566D", "33445566D", "Calle Sol 5", "29090", "Málaga", "España"),
    Usuario.crear_usuario(3, 3, "1988-07-21", "admin", "lectura", "pass654", "Carlos", "Ruiz", "carlos@mail.com", "44556677E", "44556677E", "Avenida Paz 10", "50001", "Zaragoza", "España"),
]
usuarios_no_cargados = [
    Usuario.crear_usuario(4, 4, "", "", "", "", "", "", "", "", "", "", "", "", ""),  # datos vacíos
    # ...otros ejemplos...
]

# Roles
roles_cargados = [
    Rol.crear_rol(1, "admin", "Administrador del sistema"),
    Rol.crear_rol(2, "editor", "Puede editar contenidos"),
]
roles_no_cargados = [
    Rol.crear_rol(None, "", ""),  # id_rol vacío, nombre vacío
]
roles_cargados += [
    Rol.crear_rol(3, "supervisor", "Supervisa procesos"),
    Rol.crear_rol(4, "lector", "Solo puede leer"),
]
roles_no_cargados += [
    Rol.crear_rol(5, "", ""),  # nombre vacío
    # Falta argumento (deja fuera descripcion)
    # Rol.crear_rol(6, "visitante"),
    Rol.crear_rol(7, "visitante", "Solo visita"),
    Rol.crear_rol(8, "analista", "Analiza datos"),
]

# Empresas
empresas_cargadas = [
    Empresa.crear_empresa(1, "EcoSolutions", "Energía", "logo.png", "Madrid"),
]
empresas_no_cargadas = [
    Empresa.crear_empresa(None, "", "", "", ""),  # id_empresa vacío
]
empresas_cargadas += [
    Empresa.crear_empresa(2, "GreenTech", "Tecnología", "logo2.png", "Valencia"),
    Empresa.crear_empresa(3, "AgroLife", "Agricultura", "logo3.png", "Sevilla"),
]
empresas_no_cargadas += [
    Empresa.crear_empresa(4, "", "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera ubicacion)
    # Empresa.crear_empresa(5, "BioCorp", "Biotecnología", "logo4.png"),
    Empresa.crear_empresa(6, "BioCorp", "Biotecnología", "logo4.png", "Bilbao"),
    Empresa.crear_empresa(7, "SolarNow", "Energía", "logo5.png", "Alicante"),
]

# Actividades
actividades_cargadas = [
    Actividad.crear_actividad(1, "Reforestación", "Plantación", "2023-06-01", "Plantación de árboles", "Ana", "2h", 100.0, 2.0, 0.0, "100 árboles", "Buena", "Ninguna"),
]
actividades_no_cargadas = [
    Actividad.crear_actividad(None, "", "", "", "", "", "", "", "", "", "", "", ""),  # id_actividad vacío
]
actividades_cargadas += [
    Actividad.crear_actividad(2, "Limpieza", "Limpieza de playa", "2023-07-10", "Recogida de residuos", "Carlos", "3h", 200.0, 3.0, 0.0, "Playa limpia", "Excelente", "Ninguna"),
    Actividad.crear_actividad(3, "Charla", "Charla educativa", "2023-08-15", "Concienciación ambiental", "Marta", "1h", 0.0, 1.0, 0.0, "50 asistentes", "Buena", "Ninguna"),
]
actividades_no_cargadas += [
    Actividad.crear_actividad(4, "", "", "", "", "", "", "", "", "", "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera observaciones)
    # Actividad.crear_actividad(5, "Taller", "Taller reciclaje", "2023-09-01", "Reciclaje práctico", "Elena", "2h", 50.0, 2.0, 0.0, "30 asistentes", "Muy buena"),
    Actividad.crear_actividad(6, "Taller", "Taller reciclaje", "2023-09-01", "Reciclaje práctico", "Elena", "2h", 50.0, 2.0, 0.0, "30 asistentes", "Muy buena", "Ninguna"),
    Actividad.crear_actividad(7, "Seminario", "Seminario agua", "2023-10-05", "Uso responsable del agua", "Luis", "2h", 0.0, 2.0, 0.0, "100 asistentes", "Excelente", "Ninguna"),
]

# Participantes
participantes_cargados = [
    Participante.crear_participante(1, 1, 2, "voluntario", "internet", 1, "2023-06-01", "Ana", "García", "ana@mail.com", "123456789", "12345678A", "Calle Falsa 123", "28080", "Madrid", "España"),
]
participantes_no_cargados = [
    Participante.crear_participante(2, 2, None, "", "", None, "", "", "", "", "", "", "", "", "", ""),  # datos vacíos (16 args)
    # ...otros ejemplos...
]
participantes_cargados += [
    Participante.crear_participante(2, "Ana", "Serrano", "ana.s@mail.com", "222111333", 1, "ponente", "web", 2, "2023-07-10", "", "", "", "", "", ""),  # 16 args
    Participante.crear_participante(3, "Pedro", "Gómez", "pedro@mail.com", "333444555", 3, "asistente", "amigo", 3, "2023-08-15", "", "", "", "", "", ""),  # 16 args
]
participantes_no_cargados += [
    Participante.crear_participante(4, "", "", "", "", None, "", "", None, "", "", "", "", "", "", ""),  # 16 args
    # Falta argumento (deja fuera fecha_registro)
    # Participante.crear_participante(5, "Lucía", "Vega", "lucia@mail.com", "555444333", 2, "asistente", "redes", 4),
    Participante.crear_participante(6, "Lucía", "Vega", "lucia@mail.com", "555444333", 2, "asistente", "redes", 4, "2023-09-01", "", "", "", "", "", ""),  # 16 args
    Participante.crear_participante(7, "Mario", "Díaz", "mario@mail.com", "666555444", 1, "asistente", "web", 5, "2023-10-10", "", "", "", "", "", ""),  # 16 args
]

# Proyectos
proyectos_cargados = [
    Proyecto(1, "Proyecto Verde", "Reforestación urbana", "2023-01-01", "2023-12-31", "Madrid", "Ana", "activo", "plantar árboles", "", 10000),
]
proyectos_no_cargados = [
    Proyecto(None, "", "", "", "", "", "", "", "", "", None),  # id_proyecto vacío
]
proyectos_cargados += [
    Proyecto(2, "Proyecto Azul", "Protección de ríos", "2023-02-01", "2023-11-30", "Valencia", "Carlos", "activo", "limpiar ríos", "", 20000),
    Proyecto(3, "Proyecto Solar", "Energía renovable", "2023-03-01", "2023-12-31", "Sevilla", "Marta", "planificado", "paneles solares", "", 30000),
]
proyectos_no_cargados += [
    Proyecto(4, "", "", "", "", "", "", "", "", "", None),  # todos vacíos
    # Falta argumento (deja fuera presupuesto)
    # Proyecto(5, "Proyecto Mar", "Protección marina", "2023-04-01", "2023-10-31", "Alicante", "Elena", "activo", "limpiar playas", ""),
    Proyecto(6, "Proyecto Mar", "Protección marina", "2023-04-01", "2023-10-31", "Alicante", "Elena", "activo", "limpiar playas", "", 15000),
    Proyecto(7, "Proyecto Bosque", "Reforestación", "2023-05-01", "2023-09-30", "Bilbao", "Luis", "finalizado", "plantar árboles", "", 12000),
]

# Publicaciones
publicaciones_cargadas = [
    Publicacion.crear_publicacion(1, "Título", "Contenido", "Ana", "2023-01-01", "publicado", "tag1", "palabra1", False, None, ""),
]
publicaciones_no_cargadas = [
    Publicacion.crear_publicacion(None, "", "", "", "", "", "", "", False, None, ""),  # id_publicacion vacío
]
publicaciones_cargadas += [
    Publicacion.crear_publicacion(2, "Noticia", "Texto noticia", "Carlos", "2023-02-01", "borrador", "tag2", "palabra2", False, None, ""),
    Publicacion.crear_publicacion(3, "Informe", "Texto informe", "Marta", "2023-03-01", "publicado", "tag3", "palabra3", True, 1, "Feedback positivo"),
]
publicaciones_no_cargadas += [
    Publicacion.crear_publicacion(4, "", "", "", "", "", "", "", False, None, ""),  # todos vacíos
    # Falta argumento (deja fuera feedback_empresa)
    # Publicacion.crear_publicacion(5, "Blog", "Texto blog", "Elena", "2023-04-01", "publicado", "tag4", "palabra4", False, None),
    Publicacion.crear_publicacion(6, "Blog", "Texto blog", "Elena", "2023-04-01", "publicado", "tag4", "palabra4", False, None, "Feedback blog"),
    Publicacion.crear_publicacion(7, "Reporte", "Texto reporte", "Luis", "2023-05-01", "borrador", "tag5", "palabra5", False, None, ""),
]

# Generadores IA
generadores_ia_cargados = [
    GeneradorIA.crear_generador_ia(1, "GenAI", "Generador IA", 1, "{}", "ejemplo", "2023-01-01"),
]
generadores_ia_no_cargados = [
    GeneradorIA.crear_generador_ia(None, "", "", None, "", "", ""),  # id_generador_ia vacío
]
generadores_ia_cargados += [
    GeneradorIA.crear_generador_ia(2, "EcoGen", "Generador IA", 2, "{}", "ejemplo2", "2023-02-01"),
    GeneradorIA.crear_generador_ia(3, "BioGen", "Generador IA", 3, "{}", "ejemplo3", "2023-03-01"),
]
generadores_ia_no_cargados += [
    GeneradorIA.crear_generador_ia(4, "", "", None, "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera ultima_generacion)
    # GeneradorIA.crear_generador_ia(5, "SunGen", "Generador IA", 4, "{}", "ejemplo4"),
    GeneradorIA.crear_generador_ia(6, "SunGen", "Generador IA", 4, "{}", "ejemplo4", "2023-04-01"),
    GeneradorIA.crear_generador_ia(7, "WindGen", "Generador IA", 5, "{}", "ejemplo5", "2023-05-01"),
]

# Tag
tags_cargados = [
    Tag.crear_tag(1, "palabra", "cat", 5),
    Tag.crear_tag(2, "reciclaje", "medioambiente", 10),
    Tag.crear_tag(3, "agua", "recursos", 8),
]
tags_no_cargados = [
    Tag.crear_tag(None, "", "", None),
    Tag.crear_tag(4, "", "", None),
    Tag.crear_tag(6, "energía", "recursos", 7),
    Tag.crear_tag(7, "biodiversidad", "naturaleza", 12),
]

# TemaAmbiental
temas_ambientales_cargados = [
    TemaAmbiental.crear_tema_ambiental(1, "Cambio climático", "Impacto global", 10),
    TemaAmbiental.crear_tema_ambiental(2, "Residuos", "Gestión de residuos", 8),
    TemaAmbiental.crear_tema_ambiental(3, "Agua", "Gestión del agua", 9),
]
temas_ambientales_no_cargados = [
    TemaAmbiental.crear_tema_ambiental(None, "", "", None),
    TemaAmbiental.crear_tema_ambiental(4, "", "", None),
]

# RecursoMultimedia
recursos_multimedia_cargados = [
    RecursoMultimedia.crear_recurso_multimedia(1, "imagen", "titulo", "2023-01-01", "Ana"),
    RecursoMultimedia.crear_recurso_multimedia(2, "video", "titulo2", "2023-02-01", "Carlos"),
    RecursoMultimedia.crear_recurso_multimedia(3, "audio", "titulo3", "2023-03-01", "Marta"),
]
recursos_multimedia_no_cargados = [
    RecursoMultimedia.crear_recurso_multimedia(None, "", "", "", ""),
    RecursoMultimedia.crear_recurso_multimedia(4, "", "", "", ""),
]

# Plantilla
plantillas_cargadas = [
    Plantilla.crear_plantilla(1, "Plantilla1", "tipo1", "contenido", "2023-01-01", "2023-01-02"),
    Plantilla.crear_plantilla(2, "Plantilla2", "tipo2", "contenido2", "2023-02-01", "2023-02-02"),
    Plantilla.crear_plantilla(3, "Plantilla3", "tipo3", "contenido3", "2023-03-01", "2023-03-02"),
]
plantillas_no_cargadas = [
    Plantilla.crear_plantilla(None, "", "", "", "", ""),
    Plantilla.crear_plantilla(4, "", "", "", "", ""),
]

# Clientes
clientes_cargados = [
    Cliente.crear_cliente(1, 1, "empresa", "EcoSolutions S.A.", "NIF123", "2023-01-01", "Ana", "García", "ana@mail.com", "123456789", "12345678A", "Calle Falsa 123", "28080", "Madrid", "España"),
]
clientes_no_cargados = [
    Cliente.crear_cliente(2, 2, "", "", "", "", "", "", "", "", "", "", "", "", "", ""),  # datos vacíos
]
clientes_cargados += [
    Cliente.crear_cliente(2, "empresa", "Empresa2", "Apellido2", "Razon2", "NIF2", "DNI2", "empresa2@mail.com", "222333444", "Calle 2", "29090", "Valencia", "España", "2023-02-01"),
    Cliente.crear_cliente(3, "asociacion", "Asociacion3", "Apellido3", "Razon3", "NIF3", "DNI3", "asociacion3@mail.com", "333444555", "Calle 3", "50001", "Zaragoza", "España", "2023-03-01"),
]
clientes_no_cargados += [
    Cliente.crear_cliente(4, "", "", "", "", "", "", "", "", "", "", "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera fecha_registro)
    # Cliente.crear_cliente(5, "particular", "Nombre5", "Apellido5", "Razon5", "NIF5", "DNI5", "mail5@mail.com", "555666777", "Calle 5", "33001", "Oviedo", "España"),
    Cliente.crear_cliente(6, "particular", "Nombre6", "Apellido6", "Razon6", "NIF6", "DNI6", "mail6@mail.com", "666777888", "Calle 6", "28001", "Madrid", "España", "2023-06-01"),
    Cliente.crear_cliente(7, "empresa", "Empresa7", "Apellido7", "Razon7", "NIF7", "DNI7", "empresa7@mail.com", "777888999", "Calle 7", "41010", "Sevilla", "España", "2023-07-01"),
]

# Documentos
documentos_cargados = [
    Documento.crear_documento(1, "Doc1", "desc", "2023-01-01", "pdf", "tematica1"),
]
documentos_no_cargados = [
    Documento.crear_documento(None, "", "", "", "", ""),  # id_documento vacío
]
documentos_cargados += [
    Documento.crear_documento(2, "Doc2", "desc2", "2023-02-01", "docx", "tematica2"),
    Documento.crear_documento(3, "Doc3", "desc3", "2023-03-01", "pdf", "tematica3"),
]
documentos_no_cargados += [
    Documento.crear_documento(4, "", "", "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera tematica)
    # Documento.crear_documento(5, "Doc5", "desc5", "2023-05-01", "pdf"),
    Documento.crear_documento(6, "Doc6", "desc6", "2023-06-01", "pdf", "tematica6"),
    Documento.crear_documento(7, "Doc7", "desc7", "2023-07-01", "docx", "tematica7"),
]

# Eventos
eventos_cargados = [
    Evento.crear_evento(1, "Evento1", "tipo1", "lugar1", "2023-01-01", "2023-01-02", "Madrid", "tematica1"),
]
eventos_no_cargados = [
    Evento.crear_evento(None, "", "", "", "", "", "", ""),  # id_evento vacío
]
eventos_cargados += [
    Evento.crear_evento(2, "Evento2", "tipo2", "lugar2", "2023-02-01", "2023-02-02", "Valencia", "tematica2"),
    Evento.crear_evento(3, "Evento3", "tipo3", "lugar3", "2023-03-01", "2023-03-02", "Zaragoza", "tematica3"),
]
eventos_no_cargados += [
    Evento.crear_evento(4, "", "", "", "", "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera tematica)
    # Evento.crear_evento(5, "Evento5", "tipo5", "lugar5", "2023-05-01", "2023-05-02", "Madrid"),
    Evento.crear_evento(6, "Evento6", "tipo6", "lugar6", "2023-06-01", "2023-06-02", "Sevilla", "tematica6"),
    Evento.crear_evento(7, "Evento7", "tipo7", "lugar7", "2023-07-01", "2023-07-02", "Bilbao", "tematica7"),
]

# Facturas
facturas_cargadas = [
    Factura.crear_factura(1, 1, "2023-01-01", "2023-01-10", "concepto", "Ana", 21.0, 100.0, 82.64, "F001", "transferencia", 15.0),
]
facturas_no_cargadas = [
    Factura.crear_factura(None, None, "", "", "", "", None, None, None, "", "", None),  # id_factura vacío
]
facturas_cargadas += [
    Factura.crear_factura(2, 2, "2023-02-01", "2023-02-10", "concepto2", "Carlos", 10.0, 200.0, 180.0, "F002", "efectivo", 5.0),
    Factura.crear_factura(3, 3, "2023-03-01", "2023-03-10", "concepto3", "Marta", 21.0, 300.0, 248.76, "F003", "tarjeta", 15.0),
]
facturas_no_cargadas += [
    Factura.crear_factura(4, None, "", "", "", "", None, None, None, "", "", None),  # todos vacíos
    # Falta argumento (deja fuera irpf)
    # Factura.crear_factura(5, 4, "2023-05-01", "2023-05-10", "concepto5", "Elena", 21.0, 500.0, 413.22, "F005", "transferencia"),
    Factura.crear_factura(6, 4, "2023-06-01", "2023-06-10", "concepto6", "Luis", 21.0, 600.0, 495.04, "F006", "transferencia", 21.0),
    Factura.crear_factura(7, 5, "2023-07-01", "2023-07-10", "concepto7", "Ana", 10.0, 700.0, 630.0, "F007", "efectivo", 10.0),
]

# LogSistema
logsistema_cargados = [
    LogSistema(1, "2023-01-01", 1, "login", "Inicio de sesión", "INFO"),
]
logsistema_no_cargados = [
    LogSistema(None, "", None, "", "", ""),  # id_log_sistema vacío
]
logsistema_cargados += [
    LogSistema(2, "2023-02-01", 2, "logout", "Cierre de sesión", "INFO"),
    LogSistema(3, "2023-03-01", 3, "update", "Actualización de datos", "WARNING"),
]
logsistema_no_cargados += [
    LogSistema(4, "", None, "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera nivel)
    # LogSistema(5, "2023-05-01", 4, "delete", "Eliminación de usuario"),
    LogSistema(6, "2023-06-01", 4, "login", "Inicio de sesión", "INFO"),
    LogSistema(7, "2023-07-01", 5, "update", "Actualización de datos", "ERROR"),
]

# AuditoriaPublicacion
auditorias_cargadas = [
    AuditoriaPublicacion.crear_auditoria_publicacion(1, 1, 1, "2023-01-01", 1, "{}", "ok", ""),
]
auditorias_no_cargadas = [
    AuditoriaPublicacion.crear_auditoria_publicacion(None, None, None, "", None, "", "", ""),  # id_auditoria_publicacion vacío
]
auditorias_cargadas += [
    AuditoriaPublicacion.crear_auditoria_publicacion(2, 2, 2, "2023-02-01", 2, "{}", "ok", ""),
    AuditoriaPublicacion.crear_auditoria_publicacion(3, 3, 3, "2023-03-01", 3, "{}", "error", "Fallo de IA"),
]
auditorias_no_cargadas += [
    AuditoriaPublicacion.crear_auditoria_publicacion(4, None, None, "", None, "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera observaciones)
    # AuditoriaPublicacion.crear_auditoria_publicacion(5, 4, 4, "2023-05-01", 4, "{}", "ok"),
    AuditoriaPublicacion.crear_auditoria_publicacion(6, 4, 4, "2023-06-01", 4, "{}", "ok", ""),
    AuditoriaPublicacion.crear_auditoria_publicacion(7, 5, 5, "2023-07-01", 5, "{}", "error", "Error de usuario"),
]
Tag.crear_tag(None, "", "", None, ""),  # id_tag vacío
tags_cargados += [
    Tag.crear_tag(2, "reciclaje", "medioambiente", 10, "relacion2"),
    Tag.crear_tag(3, "agua", "recursos", 8, "relacion3"),
]
tags_no_cargados += [
    Tag.crear_tag(4, "", "", None, ""),  # todos vacíos
    # Falta argumento (deja fuera relaciones)
    # Tag.crear_tag(5, "energía", "recursos", 7),
    Tag.crear_tag(6, "energía", "recursos", 7, "relacion4"),
    Tag.crear_tag(7, "biodiversidad", "naturaleza", 12, "relacion5"),
]

# RedSocial
redes_sociales_cargadas = [
    RedSocial.crear_red_social(1, "Twitter", "cuenta1", "cred", "pref", "conectado", "2023-01-01"),
]
redes_sociales_no_cargadas = [
    RedSocial.crear_red_social(None, "", "", "", "", "", ""),  # id_red_social vacío
]
redes_sociales_cargadas += [
    RedSocial.crear_red_social(2, "Facebook", "cuenta2", "cred2", "pref2", "desconectado", "2023-02-01"),
    RedSocial.crear_red_social(3, "Instagram", "cuenta3", "cred3", "pref3", "conectado", "2023-03-01"),
]
redes_sociales_no_cargadas += [
    RedSocial.crear_red_social(4, "", "", "", "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera ultima_publicacion)
    # RedSocial.crear_red_social(5, "LinkedIn", "cuenta5", "cred5", "pref5", "conectado"),
    RedSocial.crear_red_social(6, "LinkedIn", "cuenta5", "cred5", "pref5", "conectado", "2023-04-01"),
    RedSocial.crear_red_social(7, "TikTok", "cuenta6", "cred6", "pref6", "desconectado", "2023-05-01"),
]

# Programacion
programaciones_cargadas = [
    Programacion.crear_programacion(1, 1, 1, "2023-01-01", "pendiente", "noti", "Ana"),
]
programaciones_no_cargadas = [
    Programacion.crear_programacion(None, None, None, "", "", "", ""),  # id_programacion vacío
]
programaciones_cargadas += [
    Programacion.crear_programacion(2, 2, 2, "2023-02-01", "realizada", "noti2", "Carlos"),
    Programacion.crear_programacion(3, 3, 3, "2023-03-01", "pendiente", "noti3", "Marta"),
]
programaciones_no_cargadas += [
    Programacion.crear_programacion(4, None, None, "", "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera responsable)
    # Programacion.crear_programacion(5, 4, 4, "2023-05-01", "pendiente", "noti5"),
    Programacion.crear_programacion(6, 4, 4, "2023-06-01", "realizada", "noti6", "Elena"),
    Programacion.crear_programacion(7, 5, 5, "2023-07-01", "pendiente", "noti7", "Luis"),
]

# RecursoMultimedia
recursos_multimedia_cargados = [
    RecursoMultimedia.crear_recurso_multimedia(1, "imagen", "titulo", "2023-01-01", "Ana", "relacion1"),
]
recursos_multimedia_no_cargados = [
    RecursoMultimedia.crear_recurso_multimedia(None, "", "", "", "", ""),  # id_recurso_multimedia vacío
]
recursos_multimedia_cargados += [
    RecursoMultimedia.crear_recurso_multimedia(2, "video", "titulo2", "2023-02-01", "Carlos", "relacion2"),
    RecursoMultimedia.crear_recurso_multimedia(3, "audio", "titulo3", "2023-03-01", "Marta", "relacion3"),
]
recursos_multimedia_no_cargados += [
    RecursoMultimedia.crear_recurso_multimedia(4, "", "", "", "", ""),  # todos vacíos
    # Falta argumento (deja fuera relaciones)
    # RecursoMultimedia.crear_recurso_multimedia(5, "imagen", "titulo5", "2023-05-01", "Elena"),
    RecursoMultimedia.crear_recurso_multimedia(6, "imagen", "titulo5", "2023-05-01", "Elena", "relacion5"),
    RecursoMultimedia.crear_recurso_multimedia(7, "video", "titulo6", "2023-06-01", "Luis", "relacion6"),
]

