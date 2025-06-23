from ...dominios.usuario import Usuario
from ...dominios.proyecto import Proyecto
from ...dominios.tema_ambiental import TemaAmbiental
from ...dominios.rol import Rol
from ...dominios.empresa import Empresa
from ...dominios.actividad import Actividad
from ...dominios.participante import Participante
from ...dominios.publicacion import Publicacion
from ...dominios.generadoria import GeneradorIA
from ...dominios.plantilla import Plantilla
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

# Usuarios
usuarios_cargados = [
    Usuario.crear_usuario(1, "Ana", "García", "ana@mail.com", "123456789", "1990-01-01", "Calle Falsa 123", "12345678A", "28080", "Madrid", "España", "admin", "ninguna", "pass123"),
]
usuarios_no_cargados = [
    Usuario.crear_usuario(2, "", "Pérez", "perez@mail.com", "987654321", "1985-05-05", "Avenida Real 45", "87654321B", "08080", "Barcelona", "España", "user", "deportes", "pass456"),  # nombre vacío
    Usuario.crear_usuario(3, "Luis", "Martín", "", "111222333", "1995-12-12", "Calle Luna 7", "11223344C", "41010", "Sevilla", "España", "user", "música", "pass789"),  # email vacío
]

# Roles
roles_cargados = [
    Rol.crear_rol(1, "admin", "Administrador del sistema"),
    Rol.crear_rol(2, "editor", "Puede editar contenidos"),
]
roles_no_cargados = [
    Rol.crear_rol(None, "", ""),  # id_rol vacío, nombre vacío
]

# Empresas
empresas_cargadas = [
    Empresa.crear_empresa(1, "EcoSolutions", "Energía", "logo.png", "Madrid"),
]
empresas_no_cargadas = [
    Empresa.crear_empresa(None, "", "", "", ""),  # id_empresa vacío
]

# Actividades
actividades_cargadas = [
    Actividad.crear_actividad(1, "Reforestación", "Plantación", "2023-06-01", "Plantación de árboles", "Ana", "2h", 100.0, 2.0, 0.0, "100 árboles", "Buena", "Ninguna"),
]
actividades_no_cargadas = [
    Actividad.crear_actividad(None, "", "", "", "", "", "", "", "", "", "", "", ""),  # id_actividad vacío
]

# Participantes
participantes_cargados = [
    Participante.crear_participante(1, "Luis", "Martín", "luis@mail.com", "111222333", 2, "voluntario", "internet", 1, "2023-06-01"),
]
participantes_no_cargados = [
    Participante.crear_participante(None, "", "", "", "", None, "", "", None, ""),  # id_participante vacío
]

# Proyectos
proyectos_cargados = [
    Proyecto(1, "Proyecto Verde", "Reforestación urbana", "2023-01-01", "2023-12-31", "Madrid", "Ana", "activo", "plantar árboles", "", 10000),
]
proyectos_no_cargados = [
    Proyecto(None, "", "", "", "", "", "", "", "", "", None),  # id_proyecto vacío
]

# Publicaciones
publicaciones_cargadas = [
    Publicacion.crear_publicacion(1, "Título", "Contenido", "Ana", "2023-01-01", "publicado", "tag1", "palabra1", False, None, ""),
]
publicaciones_no_cargadas = [
    Publicacion.crear_publicacion(None, "", "", "", "", "", "", "", False, None, ""),  # id_publicacion vacío
]

# Generadores IA
generadores_ia_cargados = [
    GeneradorIA.crear_generador_ia(1, "GenAI", "Generador IA", 1, "{}", "ejemplo", "2023-01-01"),
]
generadores_ia_no_cargados = [
    GeneradorIA.crear_generador_ia(None, "", "", None, "", "", ""),  # id_generador_ia vacío
]

# Plantillas
plantillas_cargadas = [
    Plantilla.crear_plantilla(1, "Plantilla1", "tipo1", "contenido", "2023-01-01", "2023-01-02", ""),
]
plantillas_no_cargadas = [
    Plantilla.crear_plantilla(None, "", "", "", "", "", ""),  # id_plantilla vacío
]

# Clientes
clientes_cargados = [
    Cliente.crear_cliente(1, "particular", "Juan", "Pérez", "", "", "12345678A", "juan@mail.com", "123456789", "Calle 1", "28080", "Madrid", "España", "2023-01-01"),
]
clientes_no_cargados = [
    Cliente.crear_cliente(None, "", "", "", "", "", "", "", "", "", "", "", "", ""),  # id_cliente vacío
]

# Documentos
documentos_cargados = [
    Documento.crear_documento(1, "Doc1", "desc", "2023-01-01", "pdf", "tematica1"),
]
documentos_no_cargados = [
    Documento.crear_documento(None, "", "", "", "", ""),  # id_documento vacío
]

# Eventos
eventos_cargados = [
    Evento.crear_evento(1, "Evento1", "tipo1", "lugar1", "2023-01-01", "2023-01-02", "Madrid", "tematica1"),
]
eventos_no_cargados = [
    Evento.crear_evento(None, "", "", "", "", "", "", ""),  # id_evento vacío
]

# Facturas
facturas_cargadas = [
    Factura.crear_factura(1, 1, "2023-01-01", "2023-01-10", "concepto", "Ana", 21.0, 100.0, 82.64, "F001", "transferencia", 15.0),
]
facturas_no_cargadas = [
    Factura.crear_factura(None, None, "", "", "", "", None, None, None, "", "", None),  # id_factura vacío
]

# LogSistema
logsistema_cargados = [
    LogSistema(1, "2023-01-01", 1, "login", "Inicio de sesión", "INFO"),
]
logsistema_no_cargados = [
    LogSistema(None, "", None, "", "", ""),  # id_log_sistema vacío
]

# AuditoriaPublicacion
auditorias_cargadas = [
    AuditoriaPublicacion.crear_auditoria_publicacion(1, 1, 1, "2023-01-01", 1, "{}", "ok", ""),
]
auditorias_no_cargadas = [
    AuditoriaPublicacion.crear_auditoria_publicacion(None, None, None, "", None, "", "", ""),  # id_auditoria_publicacion vacío
]

# TemaAmbiental
temas_ambientales_cargados = [
    TemaAmbiental.crear_tema_ambiental(1, "Cambio climático", "Impacto global", 10, ["actividad1"], ["pub1"]),
]
temas_ambientales_no_cargados = [
    TemaAmbiental.crear_tema_ambiental(None, "", "", None, [], []),  # id_tema_ambiental vacío
]

# Tag
tags_cargados = [
    Tag.crear_tag(1, "palabra", "cat", 5, "relacion1"),
]
tags_no_cargados = [
    Tag.crear_tag(None, "", "", None, ""),  # id_tag vacío
]

# RedSocial
redes_sociales_cargadas = [
    RedSocial.crear_red_social(1, "Twitter", "cuenta1", "cred", "pref", "conectado", "2023-01-01", "relacion1"),
]
redes_sociales_no_cargadas = [
    RedSocial.crear_red_social(None, "", "", "", "", "", "", ""),  # id_red_social vacío
]

# Programacion
programaciones_cargadas = [
    Programacion.crear_programacion(1, 1, 1, "2023-01-01", "pendiente", "noti", "Ana"),
]
programaciones_no_cargadas = [
    Programacion.crear_programacion(None, None, None, "", "", "", ""),  # id_programacion vacío
]

# RecursoMultimedia
recursos_multimedia_cargados = [
    RecursoMultimedia.crear_recurso_multimedia(1, "imagen", "titulo", "2023-01-01", "Ana", "relacion1"),
]
recursos_multimedia_no_cargados = [
    RecursoMultimedia.crear_recurso_multimedia(None, "", "", "", "", ""),  # id_recurso_multimedia vacío
]

