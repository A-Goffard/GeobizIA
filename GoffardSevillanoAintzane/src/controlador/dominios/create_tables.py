from db_connection import get_connection, close_connection

# Lista de consultas SQL para crear las tablas
sql_queries = [
    """
    CREATE TABLE Rol (
        id_rol INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(50),
        tareas_permitidas NVARCHAR(200)
    );
    """,
    """
    CREATE TABLE Empresa (
        id_empresa INT PRIMARY KEY,
        nombre NVARCHAR(100),
        sector NVARCHAR(100),
        valores NVARCHAR(200),
        objetivos NVARCHAR(200),
        redes_sociales NVARCHAR(200),
        logo NVARCHAR(200),
        ubicacion NVARCHAR(200)
    );
    """,
    """
    CREATE TABLE Cliente (
        id_cliente INT PRIMARY KEY,
        nombre NVARCHAR(100),
        apellido NVARCHAR(100),
        email NVARCHAR(150),
        telefono NVARCHAR(50),
        tipo NVARCHAR(50),
        direccion NVARCHAR(200),
        cp NVARCHAR(10),
        poblacion NVARCHAR(100),
        pais NVARCHAR(100),
        fecha_registro DATE
    );
    """,
    """
    CREATE TABLE Fisica (
        id_fisica INT PRIMARY KEY,
        nombre NVARCHAR(100),
        apellido NVARCHAR(100),
        email NVARCHAR(150),
        telefono NVARCHAR(50),
        tipo NVARCHAR(50),
        direccion NVARCHAR(200),
        cp NVARCHAR(10),
        poblacion NVARCHAR(100),
        pais NVARCHAR(100),
        fecha_registro DATE,
        dni NVARCHAR(20),
        fecha_nacimiento DATE,
        CONSTRAINT FK_Fisica_Cliente FOREIGN KEY (id_fisica) REFERENCES Cliente(id_cliente)
    );
    """,
    """
    CREATE TABLE Juridica (
        id_juridica INT PRIMARY KEY,
        nombre NVARCHAR(100),
        apellido NVARCHAR(100),
        email NVARCHAR(150),
        telefono NVARCHAR(50),
        tipo NVARCHAR(50),
        direccion NVARCHAR(200),
        cp NVARCHAR(10),
        poblacion NVARCHAR(100),
        pais NVARCHAR(100),
        fecha_registro DATE,
        nif NVARCHAR(20),
        CONSTRAINT FK_Juridica_Cliente FOREIGN KEY (id_juridica) REFERENCES Cliente(id_cliente)
    );
    """,
    """
    CREATE TABLE Persona (
        id_persona INT PRIMARY KEY,
        nombre NVARCHAR(100),
        apellido NVARCHAR(100),
        email NVARCHAR(150),
        telefono NVARCHAR(50)
    );
    """,
    """
    CREATE TABLE Usuario (
        id_usuario INT PRIMARY KEY,
        nombre NVARCHAR(100),
        apellido NVARCHAR(100),
        correo NVARCHAR(150),
        telefono NVARCHAR(50),
        fecha_nacimiento DATE,
        direccion NVARCHAR(200),
        dni NVARCHAR(20),
        cp NVARCHAR(10),
        poblacion NVARCHAR(100),
        pais NVARCHAR(100),
        rol_id INT,
        preferencias NVARCHAR(200),
        password NVARCHAR(200),
        CONSTRAINT FK_Usuario_Rol FOREIGN KEY (rol_id) REFERENCES Rol(id_rol)
    );
    """,
    """
    CREATE TABLE RedSocial (
        id_redsocial INT PRIMARY KEY,
        plataforma NVARCHAR(50),
        nombre_cuenta NVARCHAR(100),
        credenciales NVARCHAR(200),
        empresa_id INT,
        preferencias_publicacion NVARCHAR(200),
        estado_conexion NVARCHAR(50),
        ultima_publicacion DATE,
        relaciones NVARCHAR(200),
        CONSTRAINT FK_RedSocial_Empresa FOREIGN KEY (empresa_id) REFERENCES Empresa(id_empresa)
    );
    """,
    """
    CREATE TABLE GeneradorIA (
        id_generadoria INT PRIMARY KEY,
        nombre NVARCHAR(100),
        tipo_ia NVARCHAR(50),
        configuraciones NVARCHAR(200),
        empresa_id INT,
        plantillas NVARCHAR(200),
        tags NVARCHAR(200),
        temas_ambientales NVARCHAR(200),
        ultima_generacion DATE,
        CONSTRAINT FK_GeneradorIA_Empresa FOREIGN KEY (empresa_id) REFERENCES Empresa(id_empresa)
    );
    """,
    """
    CREATE TABLE Plantilla (
        id_plantilla INT PRIMARY KEY,
        titulo NVARCHAR(100),
        tipo NVARCHAR(50),
        contenido_base NVARCHAR(MAX),
        fecha_creacion DATE,
        ultima_modificacion DATE,
        relaciones NVARCHAR(200)
    );
    """,
    """
    CREATE TABLE Publicacion (
        id_publicacion INT PRIMARY KEY,
        titulo NVARCHAR(100),
        contenido NVARCHAR(MAX),
        autor NVARCHAR(100),
        fecha_creacion DATE,
        estado NVARCHAR(50),
        tags NVARCHAR(200),
        palabras_clave NVARCHAR(200),
        plantilla_id INT,
        CONSTRAINT FK_Publicacion_Plantilla FOREIGN KEY (plantilla_id) REFERENCES Plantilla(id_plantilla)
    );
    """,
    """
    CREATE TABLE Tag (
        id_tag INT PRIMARY KEY,
        palabra_clave NVARCHAR(100),
        categoria NVARCHAR(50),
        frecuencia_uso INT,
        relaciones NVARCHAR(200)
    );
    """,
    """
    CREATE TABLE TemaAmbiental (
        id_tema_ambiental INT PRIMARY KEY,
        nombre NVARCHAR(100),
        descripcion NVARCHAR(200),
        relevancia NVARCHAR(50),
        relacion_actividades NVARCHAR(200),
        relacion_publicaciones NVARCHAR(200)
    );
    """,
    """
    CREATE TABLE AuditoriaPublicacion (
        id_auditoria_publicacion INT PRIMARY KEY,
        publicacion_id INT,
        generador_ia_id INT,
        fecha_generacion DATE,
        usuario_id INT,
        parametros_entrada NVARCHAR(200),
        resultado NVARCHAR(200),
        observaciones NVARCHAR(200),
        CONSTRAINT FK_AuditoriaPublicacion_Publicacion FOREIGN KEY (publicacion_id) REFERENCES Publicacion(id_publicacion),
        CONSTRAINT FK_AuditoriaPublicacion_GeneradorIA FOREIGN KEY (generador_ia_id) REFERENCES GeneradorIA(id_generadoria),
        CONSTRAINT FK_AuditoriaPublicacion_Usuario FOREIGN KEY (usuario_id) REFERENCES Usuario(id_usuario)
    );
    """,
    """
    CREATE TABLE Programacion (
        id_programacion INT PRIMARY KEY,
        publicacion_id INT,
        red_social_id INT,
        fecha_programada DATE,
        estado NVARCHAR(50),
        notificaciones NVARCHAR(200),
        responsable NVARCHAR(100),
        CONSTRAINT FK_Programacion_Publicacion FOREIGN KEY (publicacion_id) REFERENCES Publicacion(id_publicacion),
        CONSTRAINT FK_Programacion_RedSocial FOREIGN KEY (red_social_id) REFERENCES RedSocial(id_redsocial)
    );
    """,
    """
    CREATE TABLE Proyecto (
        id_proyecto INT PRIMARY KEY,
        nombre NVARCHAR(100),
        descripcion NVARCHAR(200),
        fecha_inicio DATE,
        fecha_fin DATE,
        poblacion NVARCHAR(100),
        responsable NVARCHAR(100),
        estado NVARCHAR(50),
        objetivos NVARCHAR(200),
        actividades NVARCHAR(200),
        presupuesto DECIMAL(18,2)
    );
    """,
    """
    CREATE TABLE Actividad (
        id_actividad INT PRIMARY KEY,
        tipo NVARCHAR(50),
        nombre NVARCHAR(100),
        fecha_ejecucion DATE,
        descripcion NVARCHAR(200),
        responsable NVARCHAR(100),
        duracion INT,
        coste_economico DECIMAL(18,2),
        coste_horas INT,
        facturacion DECIMAL(18,2),
        resultados NVARCHAR(200),
        valoracion NVARCHAR(100),
        modificaciones NVARCHAR(200),
        proyecto_id INT,
        CONSTRAINT FK_Actividad_Proyecto FOREIGN KEY (proyecto_id) REFERENCES Proyecto(id_proyecto)
    );
    """,
    """
    CREATE TABLE Participante (
        id_participante INT PRIMARY KEY,
        nombre NVARCHAR(100),
        apellido NVARCHAR(100),
        correo NVARCHAR(150),
        telefono NVARCHAR(50),
        numero_personas_juntas INT,
        rol NVARCHAR(50),
        como_conocer NVARCHAR(100),
        actividad_id INT,
        fecha_registro DATE,
        CONSTRAINT FK_Participante_Actividad FOREIGN KEY (actividad_id) REFERENCES Actividad(id_actividad)
    );
    """,
    """
    CREATE TABLE Factura (
        id_factura INT PRIMARY KEY,
        tipo NVARCHAR(50),
        nombre NVARCHAR(100),
        direccion NVARCHAR(200),
        nif NVARCHAR(20),
        fecha_facturacion DATE,
        fecha_vencimiento DATE,
        concepto NVARCHAR(200),
        responsable NVARCHAR(100),
        iva DECIMAL(5,2),
        coste_total DECIMAL(18,2),
        base_imponible DECIMAL(18,2),
        numero_factura NVARCHAR(50),
        tipo_pago NVARCHAR(50),
        irpf DECIMAL(5,2),
        cliente_id INT,
        CONSTRAINT FK_Factura_Cliente FOREIGN KEY (cliente_id) REFERENCES Cliente(id_cliente)
    );
    """,
    """
    CREATE TABLE Documento (
        id_documento INT PRIMARY KEY,
        titulo NVARCHAR(100),
        descripcion NVARCHAR(200),
        fecha_subida DATE,
        tipo NVARCHAR(50),
        tematica NVARCHAR(100),
        tema_ambiental_id INT,
        CONSTRAINT FK_Documento_TemaAmbiental FOREIGN KEY (tema_ambiental_id) REFERENCES TemaAmbiental(id_tema_ambiental)
    );
    """,
    """
    CREATE TABLE Evento (
        id_evento INT PRIMARY KEY,
        nombre NVARCHAR(100),
        tipo NVARCHAR(50),
        lugar NVARCHAR(100),
        fecha_comienzo DATE,
        fecha_final DATE,
        poblacion NVARCHAR(100),
        tematica NVARCHAR(100),
        tema_ambiental_id INT,
        CONSTRAINT FK_Evento_TemaAmbiental FOREIGN KEY (tema_ambiental_id) REFERENCES TemaAmbiental(id_tema_ambiental)
    );
    """,
    """
    CREATE TABLE RecursoMultimedia (
        id_recurso_multimedia INT PRIMARY KEY,
        tipo NVARCHAR(50),
        titulo NVARCHAR(100),
        fecha_subida DATE,
        autor NVARCHAR(100),
        relaciones NVARCHAR(200)
    );
    """,
    """
    CREATE TABLE LogSistema (
        id_log_sistema INT PRIMARY KEY,
        fecha DATETIME,
        usuario_id INT,
        accion NVARCHAR(100),
        descripcion NVARCHAR(200),
        nivel NVARCHAR(20),
        CONSTRAINT FK_LogSistema_Usuario FOREIGN KEY (usuario_id) REFERENCES Usuario(id_usuario)
    );
    """,
    """
    CREATE TABLE Publicacion_TemaAmbiental (
        id_publicacion INT,
        id_tema_ambiental INT,
        PRIMARY KEY (id_publicacion, id_tema_ambiental),
        CONSTRAINT FK_PublicacionTema_Publicacion FOREIGN KEY (id_publicacion) REFERENCES Publicacion(id_publicacion),
        CONSTRAINT FK_PublicacionTema_TemaAmbiental FOREIGN KEY (id_tema_ambiental) REFERENCES TemaAmbiental(id_tema_ambiental)
    );
    """,
    """
    CREATE TABLE Actividad_TemaAmbiental (
        id_actividad INT,
        id_tema_ambiental INT,
        PRIMARY KEY (id_actividad, id_tema_ambiental),
        CONSTRAINT FK_ActividadTema_Actividad FOREIGN KEY (id_actividad) REFERENCES Actividad(id_actividad),
        CONSTRAINT FK_ActividadTema_TemaAmbiental FOREIGN KEY (id_tema_ambiental) REFERENCES TemaAmbiental(id_tema_ambiental)
    );
    """,
    """
    CREATE TABLE Publicacion_RecursoMultimedia (
        id_publicacion INT,
        id_recurso_multimedia INT,
        PRIMARY KEY (id_publicacion, id_recurso_multimedia),
        CONSTRAINT FK_PublicacionRecurso_Publicacion FOREIGN KEY (id_publicacion) REFERENCES Publicacion(id_publicacion),
        CONSTRAINT FK_PublicacionRecurso_RecursoMultimedia FOREIGN KEY (id_recurso_multimedia) REFERENCES RecursoMultimedia(id_recurso_multimedia)
    );
    """,
    """
    CREATE TABLE Publicacion_Tag (
        id_publicacion INT,
        id_tag INT,
        PRIMARY KEY (id_publicacion, id_tag),
        CONSTRAINT FK_PublicacionTag_Publicacion FOREIGN KEY (id_publicacion) REFERENCES Publicacion(id_publicacion),
        CONSTRAINT FK_PublicacionTag_Tag FOREIGN KEY (id_tag) REFERENCES Tag(id_tag)
    );
    """,
    """
    CREATE TABLE GeneradorIA_Plantilla (
        id_generadoria INT,
        id_plantilla INT,
        PRIMARY KEY (id_generadoria, id_plantilla),
        CONSTRAINT FK_GeneradorIAPlantilla_GeneradorIA FOREIGN KEY (id_generadoria) REFERENCES GeneradorIA(id_generadoria),
        CONSTRAINT FK_GeneradorIAPlantilla_Plantilla FOREIGN KEY (id_plantilla) REFERENCES Plantilla(id_plantilla)
    );
    """
]

def create_tables():
    """
    Crea las tablas en la base de datos utilizando las consultas definidas.
    """
    conn = None
    cursor = None
    try:
        # Obtener conexión
        conn = get_connection()
        cursor = conn.cursor()
        
        # Ejecutar cada consulta
        for query in sql_queries:
            cursor.execute(query)
            print(f"Ejecutada consulta: {query[:50]}...")
        
        # Confirmar los cambios
        conn.commit()
        print("Tablas creadas exitosamente.")
        
    except pyodbc.Error as e:
        print(f"Error al ejecutar consultas: {e}")
        sys.exit(1)
    
    finally:
        # Cerrar la conexión
        close_connection(conn, cursor)

if __name__ == "__main__":
    create_tables()