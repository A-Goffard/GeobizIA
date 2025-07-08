-- Consultas SQL para inserción inteligente de datos
-- Este archivo contiene todas las consultas organizadas para usar con insertar_datos_inteligente.py

-- ======================================================
-- 1. TABLAS BASE (sin dependencias de claves foráneas)
-- ======================================================

-- ROL (tabla base, IDs explícitos)
INSERT INTO rol (id_rol, nombre, descripcion) VALUES
(1, 'Administrador', 'Usuario con permisos completos'),
(2, 'Editor', 'Usuario editor de contenido'),
(3, 'Participante', 'Usuario participante en actividades');

-- PERSONA (IDENTITY - autoincremental)
INSERT INTO persona (nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) VALUES
('Juan', 'Pérez', 'juan.perez@email.com', '123456789', '12345678A', 'Calle Mayor 1', '28001', 'Madrid', 'España'),
('María', 'Gómez', 'maria.gomez@email.com', '987654321', '87654321B', 'Avenida Libertad 10', '08001', 'Barcelona', 'España'),
('Carlos', 'López', 'carlos.lopez@email.com', '555555555', '11223344C', 'Plaza España 5', '41001', 'Sevilla', 'España'),
('Ana', 'Martínez', 'ana.martinez@email.com', '666777888', '55566677D', 'Calle Verde 15', '46001', 'Valencia', 'España');

-- EMPRESA (IDENTITY - autoincremental)
INSERT INTO empresa (nombre, sector, logo, ubicacion) VALUES
('GreenTech', 'Tecnología Verde', 'logo_greentech.png', 'Madrid, España'),
('EcoConsulting', 'Consultoría Ambiental', 'logo_ecoconsulting.png', 'Barcelona, España');

-- TIPO_PUBLICACION (IDENTITY - autoincremental)
INSERT INTO tipo_publicacion (nombre) VALUES
('Artículo'),
('Post Redes Sociales'),
('Informe'),
('Newsletter');

-- PLANTILLA (IDENTITY - autoincremental)
INSERT INTO plantilla (titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion) VALUES
('Plantilla Artículo Sostenibilidad', 'Artículo', 'Introducción sobre sostenibilidad...', '2025-01-01', '2025-06-15'),
('Plantilla Post Redes', 'Post', '¡Únete al cambio! #Sostenibilidad', '2025-02-01', '2025-06-20');

-- ACTIVIDAD (IDENTITY - autoincremental)
INSERT INTO actividad (tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones) VALUES
('Taller', 'Bombas de Semillas', 'Creación de bombas de semillas para reforestación natural', 'Ane Garmendia', '2 horas', 300.00, 8.0, 600.00, '40 participantes, 95% satisfacción', 'Excelente', 'Muy buena acogida por familias'),
('Ruta Guiada', 'Flysch de Sopela', 'Ruta interpretativa sobre geología costera', 'Unai Zubizarreta', '3 horas', 0.00, 10.0, 0.00, '15 personas, 100% satisfacción', 'Excelente', 'Tiempo soleado y sin incidencias'),
('Taller', 'Casas para Insectos', 'Taller para construir hoteles de insectos', 'Jon Ander Etxeberria', '2.5 horas', 450.00, 9.0, 700.00, '25 personas, 93% satisfacción', 'Muy buena', 'Faltaron martillos'),
('Taller', 'Arteterapia Natural', 'Expresión artística con elementos naturales', 'Nerea Bilbao', '2 horas', 320.00, 8.0, 550.00, '15 personas, 92% satisfacción', 'Excelente', 'Actividad relajante y creativa'),
('Taller', 'Compostaje Doméstico', 'Taller sobre gestión de residuos orgánicos', 'Ane Garmendia', '2.5 horas', 400.00, 8.0, 600.00, '30 personas, 95% satisfacción', 'Excelente', 'Muy participativo'),
('Charla', 'Movilidad Sostenible', 'Charla sobre transporte sostenible rural', 'Unai Zubizarreta', '1 hora', 200.00, 4.0, 300.00, '35 asistentes, 83% satisfacción', 'Buena', 'Interés en crear grupo de trabajo'),
('Taller', 'Taller Científico Infantil', 'Experimentos sobre medio ambiente para niños', 'Ane Garmendia', '1.5 horas', 350.00, 6.0, 650.00, '30 niños, 98% satisfacción', 'Excelente', 'Muy buena experiencia'),
('Charla', 'Cambio Climático Local', 'Charla sobre impacto local del cambio climático', 'Jon Ander Etxeberria', '1.5 horas', 250.00, 6.0, 400.00, '40 asistentes, 80% satisfacción', 'Buena', 'Poco tiempo para preguntas'),
('Taller', 'Reciclaje Creativo', 'Manualidades con materiales reciclados', 'Nerea Bilbao', '2 horas', 300.00, 7.0, 550.00, '22 personas, 90% satisfacción', 'Muy buena', 'Algunos materiales escasos'),
('Charla', 'Biodiversidad Local', 'Importancia de la biodiversidad en entornos urbanos', 'Jon Ander Etxeberria', '1 hora', 180.00, 5.0, 300.00, '25 asistentes, 85% satisfacción', 'Buena', 'Interesante para escolares');

-- PROYECTO (IDENTITY - autoincremental)
INSERT INTO proyecto (nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto) VALUES
('Proyecto Reciclaje Urbano', 'Implementar puntos de reciclaje en Madrid', '2025-01-01', '2025-12-31', 'Madrid', 'Juan Pérez', 'En curso', 'Reducir residuos en un 20%', 10000.00),
('Campaña Sostenibilidad', 'Promover prácticas sostenibles', '2025-03-01', '2025-09-30', 'Barcelona', 'María Gómez', 'Planificado', 'Concienciar a 1000 personas', 5000.00);

-- EVENTO (IDENTITY - autoincremental)
INSERT INTO evento (nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica) VALUES
('Feria Eco 2025', 'Feria', 'Recinto Ferial', '2025-07-10', '2025-07-12', 'Madrid', 'Sostenibilidad'),
('Congreso Verde', 'Congreso', 'Palacio de Congresos', '2025-08-20', '2025-08-22', 'Barcelona', 'Medioambiente');

-- FECHA_ACTIVIDAD (IDENTITY - autoincremental)
INSERT INTO fecha_actividad (fecha) VALUES
('2025-07-01'),
('2025-08-15'),
('2025-09-10');

-- TEMA_AMBIENTAL (IDENTITY - autoincremental)
INSERT INTO tema_ambiental (nombre, descripcion, relevancia) VALUES
('Reciclaje', 'Procesos de reciclaje de materiales', 'Alta'),
('Energía Renovable', 'Uso de energías renovables', 'Media'),
('Biodiversidad', 'Conservación de especies', 'Alta');

-- TAG (IDENTITY - autoincremental)
INSERT INTO tag (palabra_clave, categoria, frecuencia_uso) VALUES
('reciclaje', 'Medioambiente', 10),
('sostenibilidad', 'Medioambiente', 15),
('biodiversidad', 'Medioambiente', 8),
('energía', 'Tecnología', 12);

-- REDSOCIAL (IDENTITY - autoincremental)
INSERT INTO redsocial (plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion) VALUES
('Facebook', 'EcoMadrid', '{"token": "xyz"}', '{"hora": "10:00"}', 'Conectado', '2025-06-15'),
('Instagram', 'GreenBCN', '{"token": "abc"}', '{"hora": "12:00"}', 'Conectado', '2025-06-20');

-- RECURSO_MULTIMEDIA (IDENTITY - autoincremental)
INSERT INTO recurso_multimedia (tipo, titulo, fecha_subida, autor) VALUES
('Imagen', 'Foto Reciclaje', '2025-06-01', 'Carlos López'),
('Video', 'Video Sostenibilidad', '2025-06-10', 'María Gómez');

-- DOCUMENTO (IDENTITY - autoincremental)
INSERT INTO documento (titulo, descripcion, fecha_subida, tipo, tematica) VALUES
('Guía de Reciclaje', 'Manual para clasificar residuos', '2025-06-01', 'PDF', 'Reciclaje'),
('Informe Sostenibilidad', 'Reporte anual de sostenibilidad', '2025-06-15', 'PDF', 'Sostenibilidad');

-- =======================================================
-- 2. TABLAS DEPENDIENTES (usan IDs generados dinámicamente)
-- =======================================================

-- CLIENTE (depende de persona - usar IDs generados)
INSERT INTO cliente (id_persona, tipo, razon_social, nif, fecha_registro)
SELECT TOP 2 id_persona, 
       CASE WHEN ROW_NUMBER() OVER (ORDER BY id_persona) = 1 THEN 'Empresa' ELSE 'Autónomo' END,
       CASE WHEN ROW_NUMBER() OVER (ORDER BY id_persona) = 1 THEN 'EcoSolutions S.L.' ELSE 'María Gómez Consulting' END,
       CASE WHEN ROW_NUMBER() OVER (ORDER BY id_persona) = 1 THEN 'B12345678' ELSE '87654321B' END,
       CASE WHEN ROW_NUMBER() OVER (ORDER BY id_persona) = 1 THEN '2025-01-15' ELSE '2025-02-20' END
FROM persona;

-- USUARIO (depende de persona - usar IDs generados)
INSERT INTO usuario (id_persona, fecha_nacimiento, rol, preferencias, password)
SELECT id_persona, 
       CASE WHEN ROW_NUMBER() OVER (ORDER BY id_persona) = 1 THEN '1985-03-10' ELSE '1990-07-22' END,
       CASE WHEN ROW_NUMBER() OVER (ORDER BY id_persona) = 1 THEN 'Administrador' ELSE 'Editor' END,
       CASE WHEN ROW_NUMBER() OVER (ORDER BY id_persona) = 1 THEN '{"idioma": "es", "notificaciones": true}' ELSE '{"idioma": "es", "notificaciones": false}' END,
       CASE WHEN ROW_NUMBER() OVER (ORDER BY id_persona) = 1 THEN 'hashed_pass_123' ELSE 'hashed_pass_456' END
FROM persona
WHERE id_persona IN (SELECT TOP 2 id_persona FROM persona ORDER BY id_persona);

-- GENERADORIA (depende de empresa - usar IDs generados)
INSERT INTO generadoria (nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion)
SELECT 
    CASE WHEN ROW_NUMBER() OVER (ORDER BY id_empresa) = 1 THEN 'EcoBot' ELSE 'GreenWriter' END,
    CASE WHEN ROW_NUMBER() OVER (ORDER BY id_empresa) = 1 THEN 'Generador de contenido sobre sostenibilidad' ELSE 'Generador de informes ambientales' END,
    id_empresa,
    CASE WHEN ROW_NUMBER() OVER (ORDER BY id_empresa) = 1 THEN '{"modelo": "GPT-4", "idioma": "es"}' ELSE '{"modelo": "BERT", "idioma": "es"}' END,
    CASE WHEN ROW_NUMBER() OVER (ORDER BY id_empresa) = 1 THEN 'Post sobre reciclaje' ELSE 'Informe climático' END,
    CASE WHEN ROW_NUMBER() OVER (ORDER BY id_empresa) = 1 THEN '2025-06-20' ELSE '2025-06-25' END
FROM empresa;

-- PUBLICACION (depende de generadoria, tipo_publicacion, plantilla - usar IDs generados)
INSERT INTO publicacion (titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia, id_generador_ia, feedback_empresa, id_tipo_publicacion, id_plantilla)
SELECT 
    'El Futuro del Reciclaje', 
    'Artículo sobre nuevas tecnologías de reciclaje', 
    'Carlos López', 
    '2025-06-10', 
    'Publicado', 
    'reciclaje, tecnología', 
    'reciclaje, sostenibilidad', 
    1, 
    (SELECT TOP 1 id_generador_ia FROM generadoria ORDER BY id_generador_ia),
    'Buen enfoque, añadir más ejemplos', 
    (SELECT TOP 1 id_tipo_publicacion FROM tipo_publicacion ORDER BY id_tipo_publicacion),
    (SELECT TOP 1 id_plantilla FROM plantilla ORDER BY id_plantilla)

UNION ALL

SELECT 
    'Post Sostenibilidad', 
    '¡Cuidemos el planeta! #Eco', 
    'María Gómez', 
    '2025-06-15', 
    'Programado', 
    'sostenibilidad, medioambiente', 
    'eco, verde', 
    1, 
    (SELECT TOP 1 id_generador_ia FROM generadoria ORDER BY id_generador_ia DESC),
    'Perfecto para redes', 
    (SELECT TOP 1 id_tipo_publicacion FROM tipo_publicacion WHERE nombre = 'Post Redes Sociales'),
    (SELECT TOP 1 id_plantilla FROM plantilla ORDER BY id_plantilla DESC);

-- PARTICIPANTE (depende de persona y actividad - usar IDs generados)
INSERT INTO participante (id_persona, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro)
SELECT 
    p.id_persona,
    1,
    'Asistente',
    CASE WHEN ROW_NUMBER() OVER (ORDER BY p.id_persona) = 1 THEN 'Redes sociales' 
         WHEN ROW_NUMBER() OVER (ORDER BY p.id_persona) = 2 THEN 'Recomendación' 
         ELSE 'Amigos' END,
    (SELECT TOP 1 id_actividad FROM actividad ORDER BY id_actividad),
    '2025-01-10'
FROM persona p
WHERE p.id_persona IN (SELECT TOP 3 id_persona FROM persona ORDER BY id_persona DESC);

-- ACTIVIDAD_REALIZADA (depende de actividad - usar IDs generados dinámicamente) - 34 actividades realizadas
-- Insertar múltiples actividades realizadas para cada actividad existente
INSERT INTO actividad_realizada (id_actividad, fecha, asistentes, coste_economico, facturacion, observaciones)
SELECT 
    a.id_actividad,
    CASE 
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 1 THEN '2025-01-15'
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 2 THEN '2025-02-22'
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 3 THEN '2025-03-18'
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 4 THEN '2025-04-25'
        
        WHEN a.nombre = 'Flysch de Sopela' AND realizacion.num = 1 THEN '2025-01-28'
        WHEN a.nombre = 'Flysch de Sopela' AND realizacion.num = 2 THEN '2025-03-08'
        WHEN a.nombre = 'Flysch de Sopela' AND realizacion.num = 3 THEN '2025-04-15'
        
        WHEN a.nombre = 'Casas para Insectos' AND realizacion.num = 1 THEN '2025-01-12'
        WHEN a.nombre = 'Casas para Insectos' AND realizacion.num = 2 THEN '2025-02-16'
        WHEN a.nombre = 'Casas para Insectos' AND realizacion.num = 3 THEN '2025-03-22'
        WHEN a.nombre = 'Casas para Insectos' AND realizacion.num = 4 THEN '2025-04-28'
        
        WHEN a.nombre = 'Arteterapia Natural' AND realizacion.num = 1 THEN '2025-02-05'
        WHEN a.nombre = 'Arteterapia Natural' AND realizacion.num = 2 THEN '2025-03-12'
        WHEN a.nombre = 'Arteterapia Natural' AND realizacion.num = 3 THEN '2025-04-18'
        
        WHEN a.nombre = 'Compostaje Doméstico' AND realizacion.num = 1 THEN '2025-01-20'
        WHEN a.nombre = 'Compostaje Doméstico' AND realizacion.num = 2 THEN '2025-02-25'
        WHEN a.nombre = 'Compostaje Doméstico' AND realizacion.num = 3 THEN '2025-03-25'
        WHEN a.nombre = 'Compostaje Doméstico' AND realizacion.num = 4 THEN '2025-04-22'
        
        WHEN a.nombre = 'Movilidad Sostenible' AND realizacion.num = 1 THEN '2025-02-10'
        WHEN a.nombre = 'Movilidad Sostenible' AND realizacion.num = 2 THEN '2025-03-15'
        WHEN a.nombre = 'Movilidad Sostenible' AND realizacion.num = 3 THEN '2025-04-20'
        
        WHEN a.nombre = 'Taller Científico Infantil' AND realizacion.num = 1 THEN '2025-01-25'
        WHEN a.nombre = 'Taller Científico Infantil' AND realizacion.num = 2 THEN '2025-02-28'
        WHEN a.nombre = 'Taller Científico Infantil' AND realizacion.num = 3 THEN '2025-03-28'
        WHEN a.nombre = 'Taller Científico Infantil' AND realizacion.num = 4 THEN '2025-04-30'
        
        WHEN a.nombre = 'Cambio Climático Local' AND realizacion.num = 1 THEN '2025-02-12'
        WHEN a.nombre = 'Cambio Climático Local' AND realizacion.num = 2 THEN '2025-03-18'
        WHEN a.nombre = 'Cambio Climático Local' AND realizacion.num = 3 THEN '2025-04-25'
        
        WHEN a.nombre = 'Reciclaje Creativo' AND realizacion.num = 1 THEN '2025-01-30'
        WHEN a.nombre = 'Reciclaje Creativo' AND realizacion.num = 2 THEN '2025-03-05'
        WHEN a.nombre = 'Reciclaje Creativo' AND realizacion.num = 3 THEN '2025-04-10'
        
        WHEN a.nombre = 'Biodiversidad Local' AND realizacion.num = 1 THEN '2025-02-08'
        WHEN a.nombre = 'Biodiversidad Local' AND realizacion.num = 2 THEN '2025-03-20'
        WHEN a.nombre = 'Biodiversidad Local' AND realizacion.num = 3 THEN '2025-04-15'
    END as fecha,
    
    CASE 
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 1 THEN 38
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 2 THEN 42
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 3 THEN 35
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 4 THEN 45
        
        WHEN a.nombre = 'Flysch de Sopela' THEN 15 + realizacion.num * 2
        
        WHEN a.nombre = 'Casas para Insectos' AND realizacion.num = 1 THEN 22
        WHEN a.nombre = 'Casas para Insectos' AND realizacion.num = 2 THEN 28
        WHEN a.nombre = 'Casas para Insectos' AND realizacion.num = 3 THEN 24
        WHEN a.nombre = 'Casas para Insectos' AND realizacion.num = 4 THEN 30
        
        WHEN a.nombre = 'Arteterapia Natural' THEN 14 + realizacion.num * 2
        WHEN a.nombre = 'Compostaje Doméstico' THEN 25 + realizacion.num * 3
        WHEN a.nombre = 'Movilidad Sostenible' THEN 32 + realizacion.num * 4
        WHEN a.nombre = 'Taller Científico Infantil' THEN 28 + realizacion.num * 2
        WHEN a.nombre = 'Cambio Climático Local' THEN 38 + realizacion.num * 3
        WHEN a.nombre = 'Reciclaje Creativo' THEN 18 + realizacion.num * 3
        WHEN a.nombre = 'Biodiversidad Local' THEN 23 + realizacion.num * 3
    END as asistentes,
    
    CASE 
        WHEN a.nombre = 'Bombas de Semillas' THEN a.coste_economico * (0.9 + realizacion.num * 0.03)
        WHEN a.nombre = 'Flysch de Sopela' THEN 0.00
        WHEN a.nombre = 'Casas para Insectos' THEN a.coste_economico * (0.95 + realizacion.num * 0.02)
        WHEN a.nombre = 'Arteterapia Natural' THEN a.coste_economico * (0.92 + realizacion.num * 0.03)
        WHEN a.nombre = 'Compostaje Doméstico' THEN a.coste_economico * (0.91 + realizacion.num * 0.04)
        WHEN a.nombre = 'Movilidad Sostenible' THEN a.coste_economico * (0.92 + realizacion.num * 0.03)
        WHEN a.nombre = 'Taller Científico Infantil' THEN a.coste_economico * (0.93 + realizacion.num * 0.03)
        WHEN a.nombre = 'Cambio Climático Local' THEN a.coste_economico * (0.94 + realizacion.num * 0.02)
        WHEN a.nombre = 'Reciclaje Creativo' THEN a.coste_economico * (0.90 + realizacion.num * 0.05)
        WHEN a.nombre = 'Biodiversidad Local' THEN a.coste_economico * (0.92 + realizacion.num * 0.03)
    END as coste_economico,
    
    CASE 
        WHEN a.nombre = 'Bombas de Semillas' THEN a.facturacion * (0.93 + realizacion.num * 0.02)
        WHEN a.nombre = 'Flysch de Sopela' THEN 0.00
        WHEN a.nombre = 'Casas para Insectos' THEN a.facturacion * (0.97 + realizacion.num * 0.01)
        WHEN a.nombre = 'Arteterapia Natural' THEN a.facturacion * (0.94 + realizacion.num * 0.03)
        WHEN a.nombre = 'Compostaje Doméstico' THEN a.facturacion * (0.95 + realizacion.num * 0.02)
        WHEN a.nombre = 'Movilidad Sostenible' THEN a.facturacion * (0.93 + realizacion.num * 0.03)
        WHEN a.nombre = 'Taller Científico Infantil' THEN a.facturacion * (0.95 + realizacion.num * 0.02)
        WHEN a.nombre = 'Cambio Climático Local' THEN a.facturacion * (0.96 + realizacion.num * 0.02)
        WHEN a.nombre = 'Reciclaje Creativo' THEN a.facturacion * (0.94 + realizacion.num * 0.03)
        WHEN a.nombre = 'Biodiversidad Local' THEN a.facturacion * (0.93 + realizacion.num * 0.03)
    END as facturacion,
    
    CASE 
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 1 THEN 'Excelente participación de familias'
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 2 THEN 'Gran acogida, tiempo perfecto'
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 3 THEN 'Buen ambiente, niños muy participativos'
        WHEN a.nombre = 'Bombas de Semillas' AND realizacion.num = 4 THEN 'Récord de asistencia, muy exitoso'
        WHEN a.nombre = 'Flysch de Sopela' THEN 'Ruta interpretativa perfecta, condiciones ideales'
        WHEN a.nombre = 'Casas para Insectos' THEN 'Construcción exitosa, buen trabajo en equipo'
        WHEN a.nombre = 'Arteterapia Natural' THEN 'Muy relajante, buena conexión con naturaleza'
        WHEN a.nombre = 'Compostaje Doméstico' THEN 'Muy participativo, interés real en implementar'
        WHEN a.nombre = 'Movilidad Sostenible' THEN 'Gran interés en alternativas de transporte'
        WHEN a.nombre = 'Taller Científico Infantil' THEN 'Niños muy emocionados con experimentos'
        WHEN a.nombre = 'Cambio Climático Local' THEN 'Tema muy actual, gran participación'
        WHEN a.nombre = 'Reciclaje Creativo' THEN 'Resultados muy creativos y originales'
        WHEN a.nombre = 'Biodiversidad Local' THEN 'Muy educativo, descubrimientos interesantes'
    END as observaciones

FROM actividad a
CROSS JOIN (
    SELECT 1 as num UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
) realizacion
WHERE 
    (a.nombre = 'Bombas de Semillas' AND realizacion.num <= 4) OR
    (a.nombre = 'Flysch de Sopela' AND realizacion.num <= 3) OR
    (a.nombre = 'Casas para Insectos' AND realizacion.num <= 4) OR
    (a.nombre = 'Arteterapia Natural' AND realizacion.num <= 3) OR
    (a.nombre = 'Compostaje Doméstico' AND realizacion.num <= 4) OR
    (a.nombre = 'Movilidad Sostenible' AND realizacion.num <= 3) OR
    (a.nombre = 'Taller Científico Infantil' AND realizacion.num <= 4) OR
    (a.nombre = 'Cambio Climático Local' AND realizacion.num <= 3) OR
    (a.nombre = 'Reciclaje Creativo' AND realizacion.num <= 3) OR
    (a.nombre = 'Biodiversidad Local' AND realizacion.num <= 3);

-- ===============================================================
-- 3. TABLAS DE RELACIÓN N:M (usan IDs generados dinámicamente)
-- ===============================================================

-- FACTURA (depende de cliente - usar IDs generados)
INSERT INTO factura (id_cliente, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf)
SELECT 
    id_cliente,
    'Servicio',
    'Factura de servicios',
    'Dirección cliente',
    'B12345678',
    '2025-06-20',
    '2025-07-20',
    'Servicios ambientales',
    'Responsable',
    21.0,
    750.00,
    619.83,
    'F2025-00' + CAST(id_cliente AS VARCHAR),
    'Transferencia',
    0.0
FROM cliente;

-- LOG_SISTEMA (depende de usuario - usar IDs generados)
INSERT INTO log_sistema (fecha, usuario_id, accion, descripcion, nivel)
SELECT 
    '2025-06-20 10:00:00',
    id_usuario,
    'Acción de sistema',
    'Log generado automáticamente',
    'INFO'
FROM usuario;

-- AUDITORIA_PUBLICACION (depende de publicacion y generadoria)
INSERT INTO auditoria_publicacion (publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones)
SELECT 
    p.id_publicacion,
    g.id_generador_ia,
    '2025-06-15',
    (SELECT TOP 1 id_usuario FROM usuario),
    '{"tema": "sostenibilidad"}',
    'Contenido generado',
    'Generación exitosa'
FROM publicacion p
CROSS JOIN generadoria g
WHERE p.id_publicacion <= 2 AND g.id_generador_ia <= 2;

-- PROGRAMACION (depende de publicacion y redsocial)
INSERT INTO programacion (publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable)
SELECT 
    p.id_publicacion,
    r.id_red_social,
    DATEADD(day, p.id_publicacion, '2025-07-01'),
    'Programado',
    'Notificar al responsable',
    'Gestor de contenido'
FROM publicacion p
CROSS JOIN redsocial r
WHERE p.id_publicacion <= 2 AND r.id_red_social <= 2;

-- Relaciones N:M básicas
INSERT INTO actividad_fecha (id_actividad, id_fecha)
SELECT TOP 3 a.id_actividad, f.id_fecha
FROM actividad a
CROSS JOIN fecha_actividad f
WHERE a.id_actividad <= 3 AND f.id_fecha <= 3;

INSERT INTO proyecto_actividad (id_proyecto, id_actividad)
SELECT p.id_proyecto, a.id_actividad
FROM proyecto p
CROSS JOIN actividad a
WHERE p.id_proyecto <= 2 AND a.id_actividad <= 3;

INSERT INTO actividad_evento (id_actividad, id_evento)
SELECT a.id_actividad, e.id_evento
FROM actividad a
CROSS JOIN evento e
WHERE a.id_actividad <= 2 AND e.id_evento <= 2;

INSERT INTO factura_actividad (id_factura, id_actividad)
SELECT f.id_factura, a.id_actividad
FROM factura f
CROSS JOIN actividad a
WHERE f.id_factura <= 2 AND a.id_actividad <= 2;

INSERT INTO publicacion_tag (id_publicacion, id_tag)
SELECT p.id_publicacion, t.id_tag
FROM publicacion p
CROSS JOIN tag t
WHERE p.id_publicacion <= 2 AND t.id_tag <= 2;

INSERT INTO tema_ambiental_tag (id_tema_ambiental, id_tag)
SELECT ta.id_tema_ambiental, t.id_tag
FROM tema_ambiental ta
CROSS JOIN tag t
WHERE ta.id_tema_ambiental <= 2 AND t.id_tag <= 2;

INSERT INTO recurso_multimedia_tag (id_recurso_multimedia, id_tag)
SELECT rm.id_recurso_multimedia, t.id_tag
FROM recurso_multimedia rm
CROSS JOIN tag t
WHERE rm.id_recurso_multimedia <= 2 AND t.id_tag <= 2;

INSERT INTO documento_tag (id_documento, id_tag)
SELECT d.id_documento, t.id_tag
FROM documento d
CROSS JOIN tag t
WHERE d.id_documento <= 2 AND t.id_tag <= 2;

INSERT INTO plantilla_tipo_publicacion (id_plantilla, id_tipo_publicacion)
SELECT pl.id_plantilla, tp.id_tipo_publicacion
FROM plantilla pl
CROSS JOIN tipo_publicacion tp
WHERE pl.id_plantilla <= 2 AND tp.id_tipo_publicacion <= 2;

INSERT INTO tipo_publicacion_redsocial (id_tipo_publicacion, id_red_social)
SELECT tp.id_tipo_publicacion, rs.id_red_social
FROM tipo_publicacion tp
CROSS JOIN redsocial rs
WHERE tp.id_tipo_publicacion <= 2 AND rs.id_red_social <= 2;

-- ===========================================
-- Resumen de datos que se insertarán:
-- ===========================================
-- ✅ 4 personas, 2 empresas, 10 actividades
-- ✅ 2 proyectos, 2 eventos, 3 fechas actividad
-- ✅ 4 tipos publicación, 2 plantillas, 2 publicaciones
-- ✅ 3 temas ambientales, 4 tags, 2 redes sociales
-- ✅ 2 recursos multimedia, 2 documentos
-- ✅ 2 clientes, 2 usuarios, 2 generadores IA
-- ✅ 10 actividades realizadas, 3 participantes
-- ✅ Todas las relaciones N:M pobladas
-- ✅ TOTAL: 34 tablas con datos completos
