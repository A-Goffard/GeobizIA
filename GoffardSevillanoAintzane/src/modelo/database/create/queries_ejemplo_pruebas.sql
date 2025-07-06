INSERT INTO rol (id_rol, nombre, descripcion) VALUES
(1, 'Administrador', 'Usuario con permisos completos para gestionar el sistema'),
(2, 'Editor', 'Usuario con permisos para crear y editar contenido'),
(3, 'Participante', 'Usuario registrado para participar en actividades');

INSERT INTO persona (nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) VALUES
('Juan', 'Pérez', 'juan.perez@email.com', '123456789', '12345678A', 'Calle Mayor 1', '28001', 'Madrid', 'España'),
('María', 'Gómez', 'maria.gomez@email.com', '987654321', '87654321B', 'Avenida Libertad 10', '08001', 'Barcelona', 'España'),
('Carlos', 'López', 'carlos.lopez@email.com', '555555555', '11223344C', 'Plaza España 5', '41001', 'Sevilla', 'España');

INSERT INTO cliente (id_persona, tipo, razon_social, nif, fecha_registro) VALUES
(1, 'Empresa', 'EcoSolutions S.L.', 'B12345678', '2025-01-15'),
(2, 'Autónomo', 'María Gómez Consulting', '87654321B', '2025-02-20');

INSERT INTO usuario (id_persona, fecha_nacimiento, rol, preferencias, password) VALUES
(1, '1985-03-10', 'Administrador', '{"idioma": "es", "notificaciones": true}', 'hashed_pass_123'),
(3, '1990-07-22', 'Editor', '{"idioma": "es", "notificaciones": false}', 'hashed_pass_456');

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

-- NO pongas id_participante (IDENTITY)
INSERT INTO participante (id_persona, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro) VALUES
(2, 1, 'Asistente', 'Redes sociales', 1, '2025-01-10'),
(3, 2, 'Asistente', 'Recomendación', 2, '2025-02-15');

-- NO pongas id_empresa (IDENTITY)
INSERT INTO empresa (nombre, sector, logo, ubicacion) VALUES
('GreenTech', 'Tecnología Verde', 'logo_greentech.png', 'Madrid, España'),
('EcoConsulting', 'Consultoría Ambiental', 'logo_ecoconsulting.png', 'Barcelona, España');

-- NO pongas id_generador_ia (IDENTITY)
INSERT INTO generadoria (nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion) VALUES
('EcoBot', 'Generador de contenido sobre sostenibilidad', 1, '{"modelo": "GPT-4", "idioma": "es"}', 'Post sobre reciclaje', '2025-06-20'),
('GreenWriter', 'Generador de informes ambientales', 2, '{"modelo": "BERT", "idioma": "es"}', 'Informe climático', '2025-06-25');

INSERT INTO tipo_publicacion (nombre) VALUES
('Artículo'),
('Post Redes Sociales');

-- NO pongas id_plantilla (IDENTITY)
INSERT INTO plantilla (titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion) VALUES
('Plantilla Artículo Sostenibilidad', 'Artículo', 'Introducción sobre sostenibilidad...', '2025-01-01', '2025-06-15'),
('Plantilla Post Redes', 'Post', '¡Únete al cambio! #Sostenibilidad', '2025-02-01', '2025-06-20');

-- NO pongas id_publicacion (IDENTITY)
INSERT INTO publicacion (titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia, id_generador_ia, feedback_empresa, id_tipo_publicacion, id_plantilla) VALUES
('El Futuro del Reciclaje', 'Artículo sobre nuevas tecnologías de reciclaje', 'Carlos López', '2025-06-10', 'Publicado', 'reciclaje, tecnología', 'reciclaje, sostenibilidad', 1, 1, 'Buen enfoque, añadir más ejemplos', 1, 1),
('Post Sostenibilidad', '¡Cuidemos el planeta! #Eco', 'María Gómez', '2025-06-15', 'Programado', 'sostenibilidad, medioambiente', 'eco, verde', 1, 2, 'Perfecto para redes', 2, 2);

-- NO pongas id_proyecto (IDENTITY)
INSERT INTO proyecto (nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto) VALUES
('Proyecto Reciclaje Urbano', 'Implementar puntos de reciclaje en Madrid', '2025-01-01', '2025-12-31', 'Madrid', 'Juan Pérez', 'En curso', 'Reducir residuos en un 20%', 10000.00),
('Campaña Sostenibilidad', 'Promover prácticas sostenibles', '2025-03-01', '2025-09-30', 'Barcelona', 'María Gómez', 'Planificado', 'Concienciar a 1000 personas', 5000.00);

INSERT INTO fecha_actividad (fecha) VALUES
('2025-07-01'),
('2025-08-15');

INSERT INTO actividad_fecha (id_actividad, id_fecha) VALUES
(1, 1),
(2, 2);

INSERT INTO proyecto_actividad (id_proyecto, id_actividad) VALUES
(1, 1),
(2, 2);

-- NO pongas id_documento (IDENTITY)
INSERT INTO documento (titulo, descripcion, fecha_subida, tipo, tematica) VALUES
('Guía de Reciclaje', 'Manual para clasificar residuos', '2025-06-01', 'PDF', 'Reciclaje'),
('Informe Sostenibilidad', 'Reporte anual de sostenibilidad', '2025-06-15', 'PDF', 'Sostenibilidad');

-- NO pongas id_evento (IDENTITY)
INSERT INTO evento (nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica) VALUES
('Feria Eco 2025', 'Feria', 'Recinto Ferial', '2025-07-10', '2025-07-12', 'Madrid', 'Sostenibilidad'),
('Congreso Verde', 'Congreso', 'Palacio de Congresos', '2025-08-20', '2025-08-22', 'Barcelona', 'Medioambiente');

INSERT INTO actividad_evento (id_actividad, id_evento) VALUES
(1, 1),
(2, 2);

-- NO pongas id_factura (IDENTITY)
INSERT INTO factura (id_cliente, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf) VALUES
(1, 'Servicio', 'EcoSolutions S.L.', 'Calle Mayor 1', 'B12345678', '2025-06-20', '2025-07-20', 'Taller de Reciclaje', 'Juan Pérez', 21.0, 750.00, 619.83, 'F2025-001', 'Transferencia', 0.0),
(2, 'Servicio', 'María Gómez Consulting', 'Avenida Libertad 10', '87654321B', '2025-06-25', '2025-07-25', 'Conferencia Sostenibilidad', 'María Gómez', 21.0, 450.00, 371.90, 'F2025-002', 'Tarjeta', 0.0);

-- NO pongas id_log_sistema (IDENTITY)
INSERT INTO log_sistema (fecha, usuario_id, accion, descripcion, nivel) VALUES
('2025-06-20 10:00:00', 1, 'Creación Publicación', 'Creada publicación ID 1', 'INFO'),
('2025-06-25 12:00:00', 2, 'Edición Plantilla', 'Editada plantilla ID 2', 'INFO');

-- NO pongas id_auditoria_publicacion (IDENTITY)
INSERT INTO auditoria_publicacion (publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones) VALUES
(1, 1, '2025-06-10', 1, '{"tema": "reciclaje"}', 'Artículo generado', 'Buen resultado'),
(2, 2, '2025-06-15', 2, '{"tema": "sostenibilidad"}', 'Post generado', 'Revisar tono');

INSERT INTO tema_ambiental (nombre, descripcion, relevancia) VALUES
('Reciclaje', 'Procesos de reciclaje de materiales', 'Alta'),
('Energía Renovable', 'Uso de energías renovables', 'Media');

INSERT INTO tag (palabra_clave, categoria, frecuencia_uso) VALUES
('reciclaje', 'Medioambiente', 10),
('sostenibilidad', 'Medioambiente', 15);

-- NO pongas id_red_social (IDENTITY)
INSERT INTO redsocial (plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion) VALUES
('Twitter', 'EcoMadrid', '{"token": "xyz"}', '{"hora": "10:00"}', 'Conectado', '2025-06-15'),
('Instagram', 'GreenBCN', '{"token": "abc"}', '{"hora": "12:00"}', 'Conectado', '2025-06-20');

-- NO pongas id_programacion (IDENTITY)
INSERT INTO programacion (publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable) VALUES
(1, 1, '2025-07-01 10:00:00', 'Programado', 'Notificar al responsable', 'Juan Pérez'),
(2, 2, '2025-07-05 12:00:00', 'Programado', 'Notificar al equipo', 'María Gómez');

-- NO pongas id_recurso_multimedia (IDENTITY)
INSERT INTO recurso_multimedia (tipo, titulo, fecha_subida, autor) VALUES
('Imagen', 'Foto Reciclaje', '2025-06-01', 'Carlos López'),
('Video', 'Video Sostenibilidad', '2025-06-10', 'María Gómez');

INSERT INTO publicacion_tag (id_publicacion, id_tag) VALUES
(1, 1),
(2, 2);

INSERT INTO tema_ambiental_tag (id_tema_ambiental, id_tag) VALUES
(1, 1),
(2, 2);

INSERT INTO recurso_multimedia_tag (id_recurso_multimedia, id_tag) VALUES
(1, 1),
(2, 2);

INSERT INTO documento_tag (id_documento, id_tag) VALUES
(1, 1),
(2, 2);

INSERT INTO plantilla_tipo_publicacion (id_plantilla, id_tipo_publicacion) VALUES
(1, 1),
(2, 2);

INSERT INTO tipo_publicacion_redsocial (id_tipo_publicacion, id_red_social) VALUES
(1, 1),
(2, 2);

INSERT INTO actividad_realizada (id_actividad, fecha, asistentes, coste_economico, facturacion, observaciones) VALUES
-- Bombas de Semillas (1)
(1, '2025-03-15', 30, 280.00, 580.00, 'Buena asistencia pese al mal tiempo'),
(1, '2025-05-10', 40, 300.00, 600.00, 'Muy buena acogida por familias'),
(1, '2025-06-20', 45, 320.00, 700.00, 'Gran interés de los centros escolares'),

-- Flysch de Sopela (2)
(2, '2025-04-01', 12, 0.00, 0.00, 'Ruta sin coste con muy buena participación'),
(2, '2025-05-12', 15, 0.00, 0.00, 'Excelente participación, sin incidencias'),

-- Casas para Insectos (3)
(3, '2025-03-22', 20, 400.00, 600.00, 'Grupo reducido por lluvia'),
(3, '2025-05-15', 25, 450.00, 700.00, 'Actividad muy práctica, algunas herramientas escasas'),
(3, '2025-06-18', 30, 480.00, 750.00, 'Muy buena respuesta del público'),

-- Arteterapia Natural (4)
(4, '2025-05-20', 15, 320.00, 550.00, 'Ambiente relajado y creativo'),
(4, '2025-06-22', 10, 300.00, 500.00, 'Sesión más íntima y reflexiva'),

-- Compostaje Doméstico (5)
(5, '2025-05-28', 30, 400.00, 600.00, 'Muy valorado por el público'),
(5, '2025-07-02', 28, 420.00, 650.00, 'Gran interacción y preguntas del público'),

-- Movilidad Sostenible (6)
(6, '2025-06-03', 35, 200.00, 300.00, 'Se propone crear un grupo de trabajo'),
(6, '2025-07-05', 40, 220.00, 320.00, 'Buena asistencia, muchas propuestas'),

-- Taller Científico Infantil (7)
(7, '2025-06-06', 30, 350.00, 650.00, 'Excelente interacción con niños'),
(7, '2025-06-25', 32, 360.00, 670.00, 'Muy buena energía del grupo'),

-- Cambio Climático Local (8)
(8, '2025-06-10', 40, 250.00, 400.00, 'Demasiado ajustado de tiempo'),
(8, '2025-07-01', 38, 260.00, 420.00, 'Buena recepción, muchas preguntas'),

-- Reciclaje Creativo (9)
(9, '2025-06-12', 22, 300.00, 550.00, 'Muy participativo, material justo'),
(9, '2025-06-29', 25, 320.00, 600.00, 'Alta participación y creatividad'),

-- Biodiversidad Local (10)
(10, '2025-06-14', 25, 180.00, 300.00, 'Muy interesante, buena dinámica'),
(10, '2025-07-04', 30, 190.00, 330.00, 'Mayor participación escolar');
