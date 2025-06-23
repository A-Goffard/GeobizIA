-- Crear la base de datos
CREATE DATABASE GeobizIA;
GO

USE GeobizIA;
GO


-- Tabla: usuarios
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY,
    nombre NVARCHAR(100),
    apellido NVARCHAR(100),
    email NVARCHAR(150),
    telefono NVARCHAR(50),
    dni NVARCHAR(20),
    direccion NVARCHAR(200),
    cp NVARCHAR(20),
    poblacion NVARCHAR(100),
    pais NVARCHAR(100),
    fecha_nacimiento DATE,
    preferencias NVARCHAR(MAX),
    rol NVARCHAR(50),
    password NVARCHAR(200)
);

-- Tabla: actividades
CREATE TABLE actividades (
    id_actividad INT PRIMARY KEY,
    tipo NVARCHAR(50),
    nombre NVARCHAR(100),
    fecha_ejecucion DATE,
    descripcion NVARCHAR(MAX),
    responsable NVARCHAR(100),
    duracion NVARCHAR(50),
    coste_economico DECIMAL(18,2),
    coste_horas DECIMAL(18,2),
    facturacion DECIMAL(18,2),
    resultados NVARCHAR(MAX),
    valoracion NVARCHAR(MAX),
    modificaciones NVARCHAR(MAX)
);

-- Tabla: participantes
CREATE TABLE participantes (
    id_participante INT PRIMARY KEY,
    nombre NVARCHAR(100),
    apellido NVARCHAR(100),
    email NVARCHAR(150),
    telefono NVARCHAR(50),
    numero_personas_juntas INT,
    rol NVARCHAR(50),
    como_conocer NVARCHAR(200),
    actividad_id INT,
    fecha_registro DATE,
    FOREIGN KEY (actividad_id) REFERENCES actividades(id_actividad)
);

-- Tabla: publicaciones
CREATE TABLE publicaciones (
    id_publicacion INT PRIMARY KEY,
    titulo NVARCHAR(200),
    contenido NVARCHAR(MAX),
    autor NVARCHAR(100),
    fecha_creacion DATE,
    estado NVARCHAR(50),
    tags NVARCHAR(MAX),
    palabras_clave NVARCHAR(MAX)
);

-- Tabla: clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre NVARCHAR(100),
    apellido NVARCHAR(100),
    email NVARCHAR(150),
    telefono NVARCHAR(50),
    tipo NVARCHAR(50),
    direccion NVARCHAR(200),
    cp NVARCHAR(20),
    poblacion NVARCHAR(100),
    pais NVARCHAR(100),
    fecha_registro DATE
);

-- Tabla: documentos
CREATE TABLE documentos (
    id_documento INT PRIMARY KEY,
    titulo NVARCHAR(200),
    descripcion NVARCHAR(MAX),
    fecha_subida DATE,
    tipo NVARCHAR(50),
    tematica NVARCHAR(100)
);

-- Tabla: facturas
CREATE TABLE facturas (
    id_factura INT PRIMARY KEY,
    tipo NVARCHAR(50),
    nombre NVARCHAR(100),
    direccion NVARCHAR(200),
    nif NVARCHAR(20),
    fecha_facturacion DATE,
    fecha_vencimiento DATE,
    concepto NVARCHAR(MAX),
    responsable NVARCHAR(100),
    iva DECIMAL(5,2),
    coste_total DECIMAL(18,2),
    base_imponible DECIMAL(18,2),
    numero_factura NVARCHAR(50),
    tipo_pago NVARCHAR(50),
    irpf DECIMAL(5,2)
);

-- Tabla: proyectos
CREATE TABLE proyectos (
    id_proyecto INT PRIMARY KEY,
    nombre NVARCHAR(200),
    descripcion NVARCHAR(MAX),
    fecha_inicio DATE,
    fecha_fin DATE,
    poblacion NVARCHAR(100),
    responsable NVARCHAR(100),
    estado NVARCHAR(50),
    objetivos NVARCHAR(MAX),
    actividades NVARCHAR(MAX),
    presupuesto DECIMAL(18,2)
);

-- Tabla: roles
CREATE TABLE roles (
    nombre NVARCHAR(50) PRIMARY KEY,
    tareas_permitidas NVARCHAR(MAX)
);

-- Tabla: empresas
CREATE TABLE empresas (
    id_empresa INT PRIMARY KEY,
    nombre NVARCHAR(200),
    sector NVARCHAR(100),
    valores NVARCHAR(MAX),
    objetivos NVARCHAR(MAX),
    redes_sociales NVARCHAR(MAX),
    logo NVARCHAR(200),
    ubicacion NVARCHAR(200)
);

-- Tabla: redes_sociales
CREATE TABLE redes_sociales (
    id_red_social INT PRIMARY KEY,
    plataforma NVARCHAR(100),
    nombre_cuenta NVARCHAR(100),
    credenciales NVARCHAR(MAX),
    empresa_id INT,
    preferencias_publicacion NVARCHAR(MAX),
    estado_conexion NVARCHAR(50),
    ultima_publicacion DATE,
    relaciones NVARCHAR(MAX),
    FOREIGN KEY (empresa_id) REFERENCES empresas(id_empresa)
);

-- Tabla: temas_ambientales
CREATE TABLE temas_ambientales (
    id_tema_ambiental INT PRIMARY KEY,
    nombre NVARCHAR(100),
    descripcion NVARCHAR(MAX),
    relevancia NVARCHAR(50),
    relacion_actividades NVARCHAR(MAX),
    relacion_publicaciones NVARCHAR(MAX)
);

-- Tabla: tags_palabras_clave
CREATE TABLE tags_palabras_clave (
    id_tag INT PRIMARY KEY,
    palabra_clave NVARCHAR(100),
    categoria NVARCHAR(100),
    frecuencia_uso INT,
    relaciones NVARCHAR(MAX)
);

-- Tabla: recursos_multimedia
CREATE TABLE recursos_multimedia (
    id_recurso_multimedia INT PRIMARY KEY,
    tipo NVARCHAR(50),
    titulo NVARCHAR(200),
    fecha_subida DATE,
    autor NVARCHAR(100),
    relaciones NVARCHAR(MAX)
);

-- Tabla: plantillas
CREATE TABLE plantillas (
    id_plantilla INT PRIMARY KEY,
    titulo NVARCHAR(200),
    tipo NVARCHAR(50),
    contenido_base NVARCHAR(MAX),
    fecha_creacion DATE,
    ultima_modificacion DATE,
    relaciones NVARCHAR(MAX)
);

-- Tabla: programaciones
CREATE TABLE programaciones (
    id_programacion INT PRIMARY KEY,
    publicacion_id INT,
    red_social_id INT,
    fecha_programada DATE,
    estado NVARCHAR(50),
    notificaciones NVARCHAR(MAX),
    responsable NVARCHAR(100),
    FOREIGN KEY (publicacion_id) REFERENCES publicaciones(id_publicacion),
    FOREIGN KEY (red_social_id) REFERENCES redes_sociales(id_red_social)
);

-- Tabla: eventos
CREATE TABLE eventos (
    id_evento INT PRIMARY KEY,
    nombre NVARCHAR(200),
    tipo NVARCHAR(50),
    lugar NVARCHAR(200),
    fecha_comienzo DATE,
    fecha_final DATE,
    poblacion NVARCHAR(100),
    tematica NVARCHAR(100)
);

-- Tabla: generadores_ia
CREATE TABLE generadores_ia (
    id_generador_ia INT PRIMARY KEY,
    nombre NVARCHAR(100),
    tipo_ia NVARCHAR(100),
    configuraciones NVARCHAR(MAX),
    empresa_id INT,
    plantillas NVARCHAR(MAX),
    tags NVARCHAR(MAX),
    temas_ambientales NVARCHAR(MAX),
    ultima_generacion DATE,
    FOREIGN KEY (empresa_id) REFERENCES empresas(id_empresa)
);

-- Tabla: log_sistema
CREATE TABLE log_sistema (
    id_log_sistema INT PRIMARY KEY,
    fecha DATE,
    usuario_id INT,
    accion NVARCHAR(100),
    descripcion NVARCHAR(MAX),
    nivel NVARCHAR(20),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario)
);

-- Tabla: auditoria_publicacion
CREATE TABLE auditoria_publicacion (
    id_auditoria_publicacion INT PRIMARY KEY,
    publicacion_id INT,
    generador_ia_id INT,
    fecha_generacion DATE,
    usuario_id INT,
    parametros_entrada NVARCHAR(MAX),
    resultado NVARCHAR(MAX),
    observaciones NVARCHAR(MAX),
    FOREIGN KEY (publicacion_id) REFERENCES publicaciones(id_publicacion),
    FOREIGN KEY (generador_ia_id) REFERENCES generadores_ia(id_generador_ia),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario)
);

-- Tabla: tema_ambiental
CREATE TABLE tema_ambiental (
    id_tema_ambiental INT PRIMARY KEY,
    nombre NVARCHAR(100),
    descripcion NVARCHAR(MAX),
    relevancia NVARCHAR(50),
    relacion_actividades NVARCHAR(MAX),
    relacion_publicaciones NVARCHAR(MAX)
);

-- Tabla: tag
CREATE TABLE tag (
    id_tag INT PRIMARY KEY,
    palabra_clave NVARCHAR(100),
    categoria NVARCHAR(100),
    frecuencia_uso INT,
    relaciones NVARCHAR(MAX)
);

-- Tabla: redsocial
CREATE TABLE redsocial (
    id_red_social INT PRIMARY KEY,
    plataforma NVARCHAR(100),
    nombre_cuenta NVARCHAR(100),
    credenciales NVARCHAR(MAX),
    empresa_id INT,
    preferencias_publicacion NVARCHAR(MAX),
    estado_conexion NVARCHAR(50),
    ultima_publicacion DATE,
    relaciones NVARCHAR(MAX),
    FOREIGN KEY (empresa_id) REFERENCES empresas(id_empresa)
);

-- Tabla: recurso_multimedia
CREATE TABLE recurso_multimedia (
    id_recurso_multimedia INT PRIMARY KEY,
    tipo NVARCHAR(50),
    titulo NVARCHAR(200),
    fecha_subida DATE,
    autor NVARCHAR(100),
    relaciones NVARCHAR(MAX)
);

-- Agrega más relaciones y tablas según tus necesidades.
