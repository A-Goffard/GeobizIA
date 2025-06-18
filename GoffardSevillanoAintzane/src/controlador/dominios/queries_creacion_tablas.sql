CREATE TABLE usuario (
    id_usuario INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    email TEXT,
    telefono TEXT,
    fecha_nacimiento TEXT,
    direccion TEXT,
    dni TEXT,
    cp TEXT,
    poblacion TEXT,
    pais TEXT,
    rol TEXT,
    preferencias TEXT,
    password TEXT
);

CREATE TABLE participante (
    id_participante INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    email TEXT,
    telefono TEXT,
    numero_personas_juntas INTEGER,
    rol TEXT,
    como_conocer TEXT,
    actividad_id INTEGER,
    fecha_registro TEXT
);

CREATE TABLE publicacion (
    id_publicacion INTEGER PRIMARY KEY,
    titulo TEXT,
    contenido TEXT,
    autor TEXT,
    fecha_creacion TEXT,
    estado TEXT,
    tags TEXT,
    palabras_clave TEXT
);

CREATE TABLE proyecto (
    id_proyecto INTEGER PRIMARY KEY,
    nombre TEXT,
    descripcion TEXT,
    fecha_inicio TEXT,
    fecha_fin TEXT,
    poblacion TEXT,
    responsable TEXT,
    estado TEXT,
    objetivos TEXT,
    actividades TEXT,
    presupuesto REAL
);

CREATE TABLE programacion (
    id_programacion INTEGER PRIMARY KEY,
    publicacion_id INTEGER,
    red_social_id INTEGER,
    fecha_programada TEXT,
    estado TEXT,
    notificaciones TEXT,
    responsable TEXT
);

CREATE TABLE plantilla (
    id_plantilla INTEGER PRIMARY KEY,
    titulo TEXT,
    tipo TEXT,
    contenido_base TEXT,
    fecha_creacion TEXT,
    ultima_modificacion TEXT,
    relaciones TEXT
);

CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    email TEXT,
    telefono TEXT,
    tipo TEXT,
    direccion TEXT,
    cp TEXT,
    poblacion TEXT,
    pais TEXT,
    fecha_registro TEXT
);

CREATE TABLE juridica (
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    email TEXT,
    telefono TEXT,
    tipo TEXT,
    direccion TEXT,
    cp TEXT,
    poblacion TEXT,
    pais TEXT,
    fecha_registro TEXT,
    nif TEXT
);

CREATE TABLE fisica (
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    email TEXT,
    telefono TEXT,
    tipo TEXT,
    direccion TEXT,
    cp TEXT,
    poblacion TEXT,
    pais TEXT,
    fecha_registro TEXT,
    dni TEXT,
    fecha_nacimiento TEXT
);

CREATE TABLE documento (
    id_documento INTEGER PRIMARY KEY,
    titulo TEXT,
    descripcion TEXT,
    fecha_subida TEXT,
    tipo TEXT,
    tematica TEXT
);

CREATE TABLE empresa (
    id_empresa INTEGER PRIMARY KEY,
    nombre TEXT,
    sector TEXT,
    valores TEXT,
    objetivos TEXT,
    redes_sociales TEXT,
    logo TEXT,
    ubicacion TEXT
);

CREATE TABLE evento (
    id_evento INTEGER PRIMARY KEY,
    nombre TEXT,
    tipo TEXT,
    lugar TEXT,
    fecha_comienzo TEXT,
    fecha_final TEXT,
    poblacion TEXT,
    tematica TEXT
);

CREATE TABLE factura (
    id_factura INTEGER PRIMARY KEY,
    tipo TEXT,
    nombre TEXT,
    direccion TEXT,
    nif TEXT,
    fecha_facturacion TEXT,
    fecha_vencimiento TEXT,
    concepto TEXT,
    responsable TEXT,
    iva REAL,
    coste_total REAL,
    base_imponible REAL,
    numero_factura TEXT,
    tipo_pago TEXT,
    irpf REAL
);

CREATE TABLE generadoria (
    id_generador_ia INTEGER PRIMARY KEY,
    nombre TEXT,
    tipo_ia TEXT,
    configuraciones TEXT,
    empresa_id INTEGER,
    plantillas TEXT,
    tags TEXT,
    temas_ambientales TEXT,
    ultima_generacion TEXT
);

CREATE TABLE log_sistema (
    id_log_sistema INTEGER PRIMARY KEY,
    fecha TEXT,
    usuario_id INTEGER,
    accion TEXT,
    descripcion TEXT,
    nivel TEXT
);

CREATE TABLE auditoria_publicacion (
    id_auditoria_publicacion INTEGER PRIMARY KEY,
    publicacion_id INTEGER,
    generador_ia_id INTEGER,
    fecha_generacion TEXT,
    usuario_id INTEGER,
    parametros_entrada TEXT,
    resultado TEXT,
    observaciones TEXT
);

CREATE TABLE actividad (
    id_actividad INTEGER PRIMARY KEY,
    tipo TEXT,
    nombre TEXT,
    fecha_ejecucion TEXT,
    descripcion TEXT,
    responsable TEXT,
    duracion TEXT,
    coste_economico REAL,
    coste_horas REAL,
    facturacion REAL,
    resultados TEXT,
    valoracion TEXT,
    modificaciones TEXT
);

CREATE TABLE tema_ambiental (
    id_tema_ambiental INTEGER PRIMARY KEY,
    nombre TEXT,
    descripcion TEXT,
    relevancia TEXT,
    relacion_actividades TEXT,
    relacion_publicaciones TEXT
);

CREATE TABLE tag (
    id_tag INTEGER PRIMARY KEY,
    palabra_clave TEXT,
    categoria TEXT,
    frecuencia_uso INTEGER,
    relaciones TEXT
);

CREATE TABLE redsocial (
    id_red_social INTEGER PRIMARY KEY,
    plataforma TEXT,
    nombre_cuenta TEXT,
    credenciales TEXT,
    empresa_id INTEGER,
    preferencias_publicacion TEXT,
    estado_conexion TEXT,
    ultima_publicacion TEXT,
    relaciones TEXT
);

CREATE TABLE recurso_multimedia (
    id_recurso_multimedia INTEGER PRIMARY KEY,
    tipo TEXT,
    titulo TEXT,
    fecha_subida TEXT,
    autor TEXT,
    relaciones TEXT
);

-- Agrega más tablas según los atributos exactos de tus modelos si es necesario.
