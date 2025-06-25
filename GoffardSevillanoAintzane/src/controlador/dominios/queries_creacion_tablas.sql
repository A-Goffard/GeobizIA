CREATE TABLE rol (
    id_rol INT PRIMARY KEY,
    nombre NVARCHAR(50) UNIQUE,
    descripcion NVARCHAR(200),
    CONSTRAINT FK_usuario_rol FOREIGN KEY (id_rol) REFERENCES rol(id_rol)
);

CREATE TABLE persona (
    id_persona INT PRIMARY KEY,
    nombre NVARCHAR(100),
    apellido NVARCHAR(100),
    email NVARCHAR(100),
    telefono NVARCHAR(50),
    dni NVARCHAR(20),
    direccion NVARCHAR(200),
    cp NVARCHAR(10),
    poblacion NVARCHAR(100),
    pais NVARCHAR(100)
);

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    id_persona INT,
    tipo NVARCHAR(20),
    razon_social NVARCHAR(200),
    nif NVARCHAR(20),
    fecha_registro NVARCHAR(50),
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);

CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY,
    id_persona INT,
    fecha_nacimiento NVARCHAR(50),
    rol NVARCHAR(50),
    preferencias NVARCHAR(MAX),
    password NVARCHAR(100),
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);

CREATE TABLE participante (
    id_participante INT PRIMARY KEY,
    id_persona INT,
    numero_personas_juntas INT,
    rol NVARCHAR(50),
    como_conocer NVARCHAR(100),
    actividad_id INT,
    fecha_registro NVARCHAR(50),
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona),
    FOREIGN KEY (actividad_id) REFERENCES actividad(id_actividad)
);

CREATE TABLE empresa (
    id_empresa INT PRIMARY KEY,
    nombre NVARCHAR(200),
    sector NVARCHAR(100),
    logo NVARCHAR(200),
    ubicacion NVARCHAR(200)
);

CREATE TABLE actividad (
    id_actividad INT PRIMARY KEY,
    tipo NVARCHAR(50),
    nombre NVARCHAR(100),
    descripcion NVARCHAR(MAX),
    responsable NVARCHAR(100),
    duracion NVARCHAR(50),
    coste_economico FLOAT,
    coste_horas FLOAT,
    facturacion FLOAT,
    resultados NVARCHAR(MAX),
    valoracion NVARCHAR(MAX),
    observaciones NVARCHAR(MAX)
);

CREATE TABLE fecha_actividad (
    id_fecha INT PRIMARY KEY IDENTITY(1,1),
    fecha NVARCHAR(50)
);

CREATE TABLE actividad_fecha (
    id_actividad INT,
    id_fecha INT,
    PRIMARY KEY (id_actividad, id_fecha),
    CONSTRAINT FK_actividad_fecha_actividad FOREIGN KEY (id_actividad) REFERENCES actividad(id_actividad),
    CONSTRAINT FK_actividad_fecha_fecha FOREIGN KEY (id_fecha) REFERENCES fecha_actividad(id_fecha)
);

CREATE TABLE publicacion (
    id_publicacion INT PRIMARY KEY,
    titulo NVARCHAR(200),
    contenido NVARCHAR(MAX),
    autor NVARCHAR(100),
    fecha_creacion NVARCHAR(50),
    estado NVARCHAR(50),
    tags NVARCHAR(200),
    palabras_clave NVARCHAR(200),
    generada_por_ia BIT DEFAULT 0,
    id_generador_ia INT NULL,
    feedback_empresa NVARCHAR(MAX),
    id_tipo_publicacion INT,
    id_plantilla INT NULL,
    CONSTRAINT FK_publicacion_generador FOREIGN KEY (id_generador_ia) REFERENCES generadoria(id_generador_ia),
    CONSTRAINT FK_publicacion_tipo_publicacion FOREIGN KEY (id_tipo_publicacion) REFERENCES tipo_publicacion(id_tipo_publicacion),
    CONSTRAINT FK_publicacion_plantilla FOREIGN KEY (id_plantilla) REFERENCES plantilla(id_plantilla)
);

CREATE TABLE generadoria (
    id_generador_ia INT PRIMARY KEY,
    nombre NVARCHAR(100),
    descripcion NVARCHAR(MAX),
    empresa_id INT,
    configuraciones NVARCHAR(MAX), -- JSON o texto con parámetros de la IA
    ejemplos_estilo NVARCHAR(MAX), -- Ejemplos de textos de la empresa
    ultima_generacion NVARCHAR(50),
    CONSTRAINT FK_generadoria_empresa FOREIGN KEY (empresa_id) REFERENCES empresa(id_empresa)
);

CREATE TABLE proyecto (
    id_proyecto INT PRIMARY KEY,
    nombre NVARCHAR(200),
    descripcion NVARCHAR(MAX),
    fecha_inicio NVARCHAR(50),
    fecha_fin NVARCHAR(50),
    poblacion NVARCHAR(100),
    responsable NVARCHAR(100),
    estado NVARCHAR(50),
    objetivos NVARCHAR(MAX),
    presupuesto FLOAT
);

CREATE TABLE proyecto_actividad (
    id_proyecto INT,
    id_actividad INT,
    PRIMARY KEY (id_proyecto, id_actividad),
    CONSTRAINT FK_proyecto_actividad_proyecto FOREIGN KEY (id_proyecto) REFERENCES proyecto(id_proyecto),
    CONSTRAINT FK_proyecto_actividad_actividad FOREIGN KEY (id_actividad) REFERENCES actividad(id_actividad)
);

CREATE TABLE plantilla (
    id_plantilla INT PRIMARY KEY,
    titulo NVARCHAR(200),
    tipo NVARCHAR(50),
    contenido_base NVARCHAR(MAX),
    fecha_creacion NVARCHAR(50),
    ultima_modificacion NVARCHAR(50)
);

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    tipo NVARCHAR(20), -- 'particular', 'empresa', 'asociacion', 'ayuntamiento'
    nombre NVARCHAR(100),
    apellido NVARCHAR(100),
    razon_social NVARCHAR(200),
    nif NVARCHAR(20),
    dni NVARCHAR(20),
    email NVARCHAR(100),
    telefono NVARCHAR(50),
    direccion NVARCHAR(200),
    cp NVARCHAR(10),
    poblacion NVARCHAR(100),
    pais NVARCHAR(100),
    fecha_registro NVARCHAR(50)
);

CREATE TABLE documento (
    id_documento INT PRIMARY KEY,
    titulo NVARCHAR(200),
    descripcion NVARCHAR(MAX),
    fecha_subida NVARCHAR(50),
    tipo NVARCHAR(50),
    tematica NVARCHAR(100)
);

CREATE TABLE evento (
    id_evento INT PRIMARY KEY,
    nombre NVARCHAR(200),
    tipo NVARCHAR(50),
    lugar NVARCHAR(100),
    fecha_comienzo NVARCHAR(50),
    fecha_final NVARCHAR(50),
    poblacion NVARCHAR(100),
    tematica NVARCHAR(100)
);

CREATE TABLE actividad_evento (
    id_actividad INT,
    id_evento INT,
    PRIMARY KEY (id_actividad, id_evento),
    CONSTRAINT FK_actividad_evento_actividad FOREIGN KEY (id_actividad) REFERENCES actividad(id_actividad),
    CONSTRAINT FK_actividad_evento_evento FOREIGN KEY (id_evento) REFERENCES evento(id_evento)
);

CREATE TABLE factura (
    id_factura INT PRIMARY KEY,
    id_cliente INT,
    tipo NVARCHAR(50),
    nombre NVARCHAR(100),
    direccion NVARCHAR(200),
    nif NVARCHAR(20),
    fecha_facturacion NVARCHAR(50),
    fecha_vencimiento NVARCHAR(50),
    concepto NVARCHAR(MAX),
    responsable NVARCHAR(100),
    iva FLOAT,
    coste_total FLOAT,
    base_imponible FLOAT,
    numero_factura NVARCHAR(50),
    tipo_pago NVARCHAR(50),
    irpf FLOAT,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE factura_actividad (
    id_factura INT,
    id_actividad INT,
    PRIMARY KEY (id_factura, id_actividad),
    FOREIGN KEY (id_factura) REFERENCES factura(id_factura),
    FOREIGN KEY (id_actividad) REFERENCES actividad(id_actividad)
);

CREATE TABLE log_sistema (
    id_log_sistema INT PRIMARY KEY,
    fecha NVARCHAR(50),
    usuario_id INT,
    accion NVARCHAR(100),
    descripcion NVARCHAR(MAX),
    nivel NVARCHAR(50),
    CONSTRAINT FK_log_usuario FOREIGN KEY (usuario_id) REFERENCES usuario(id_usuario)
);

CREATE TABLE auditoria_publicacion (
    id_auditoria_publicacion INT PRIMARY KEY,
    publicacion_id INT,
    generador_ia_id INT,
    fecha_generacion NVARCHAR(50),
    usuario_id INT,
    parametros_entrada NVARCHAR(MAX),
    resultado NVARCHAR(MAX),
    observaciones NVARCHAR(MAX),
    CONSTRAINT FK_auditoria_publicacion FOREIGN KEY (publicacion_id) REFERENCES publicacion(id_publicacion),
    CONSTRAINT FK_auditoria_generador FOREIGN KEY (generador_ia_id) REFERENCES generadoria(id_generador_ia),
    CONSTRAINT FK_auditoria_usuario FOREIGN KEY (usuario_id) REFERENCES usuario(id_usuario)
);

CREATE TABLE tema_ambiental (
    id_tema_ambiental INT PRIMARY KEY,
    nombre NVARCHAR(100),
    descripcion NVARCHAR(MAX),
    relevancia NVARCHAR(50)
);

CREATE TABLE tag (
    id_tag INT PRIMARY KEY,
    palabra_clave NVARCHAR(100),
    categoria NVARCHAR(50),
    frecuencia_uso INT
);

CREATE TABLE redsocial (
    id_red_social INT PRIMARY KEY,
    plataforma NVARCHAR(100),
    nombre_cuenta NVARCHAR(100),
    credenciales NVARCHAR(MAX),
    preferencias_publicacion NVARCHAR(MAX),
    estado_conexion NVARCHAR(50),
    ultima_publicacion NVARCHAR(50)
);

CREATE TABLE programacion (
    id_programacion INT PRIMARY KEY,
    publicacion_id INT,
    red_social_id INT,
    fecha_programada NVARCHAR(50),
    estado NVARCHAR(50),
    notificaciones NVARCHAR(MAX),
    responsable NVARCHAR(100),
    CONSTRAINT FK_programacion_publicacion FOREIGN KEY (publicacion_id) REFERENCES publicacion(id_publicacion),
    CONSTRAINT FK_programacion_redsocial FOREIGN KEY (red_social_id) REFERENCES redsocial(id_red_social)
);

CREATE TABLE recurso_multimedia (
    id_recurso_multimedia INT PRIMARY KEY,
    tipo NVARCHAR(50),
    titulo NVARCHAR(200),
    fecha_subida NVARCHAR(50),
    autor NVARCHAR(100)
);

CREATE TABLE publicacion_tag (
    id_publicacion INT,
    id_tag INT,
    PRIMARY KEY (id_publicacion, id_tag),
    FOREIGN KEY (id_publicacion) REFERENCES publicacion(id_publicacion),
    FOREIGN KEY (id_tag) REFERENCES tag(id_tag)
);

CREATE TABLE tema_ambiental_tag (
    id_tema_ambiental INT,
    id_tag INT,
    PRIMARY KEY (id_tema_ambiental, id_tag),
    FOREIGN KEY (id_tema_ambiental) REFERENCES tema_ambiental(id_tema_ambiental),
    FOREIGN KEY (id_tag) REFERENCES tag(id_tag)
);

CREATE TABLE recurso_multimedia_tag (
    id_recurso_multimedia INT,
    id_tag INT,
    PRIMARY KEY (id_recurso_multimedia, id_tag),
    FOREIGN KEY (id_recurso_multimedia) REFERENCES recurso_multimedia(id_recurso_multimedia),
    FOREIGN KEY (id_tag) REFERENCES tag(id_tag)
);

CREATE TABLE documento_tag (
    id_documento INT,
    id_tag INT,
    PRIMARY KEY (id_documento, id_tag),
    FOREIGN KEY (id_documento) REFERENCES documento(id_documento),
    FOREIGN KEY (id_tag) REFERENCES tag(id_tag)
);

CREATE TABLE plantilla_tipo_publicacion (
    id_plantilla INT,
    id_tipo_publicacion INT,
    PRIMARY KEY (id_plantilla, id_tipo_publicacion),
    FOREIGN KEY (id_plantilla) REFERENCES plantilla(id_plantilla),
    FOREIGN KEY (id_tipo_publicacion) REFERENCES tipo_publicacion(id_tipo_publicacion)
);

CREATE TABLE tipo_publicacion_redsocial (
    id_tipo_publicacion INT,
    id_red_social INT,
    PRIMARY KEY (id_tipo_publicacion, id_red_social),
    FOREIGN KEY (id_tipo_publicacion) REFERENCES tipo_publicacion(id_tipo_publicacion),
    FOREIGN KEY (id_red_social) REFERENCES redsocial(id_red_social)
);