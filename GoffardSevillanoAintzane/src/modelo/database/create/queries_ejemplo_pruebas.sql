INSERT INTO rol (id_rol, nombre, descripcion) VALUES
(1, 'Administrador', 'Usuario con permisos completos para gestionar el sistema'),
(2, 'Editor', 'Usuario con permisos para crear y editar contenido'),
(3, 'Participante', 'Usuario registrado para participar en actividades');

INSERT INTO persona (id_persona, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) VALUES
(1, 'Juan', 'Pérez', 'juan.perez@email.com', '123456789', '12345678A', 'Calle Mayor 1', '28001', 'Madrid', 'España'),
(2, 'María', 'Gómez', 'maria.gomez@email.com', '987654321', '87654321B', 'Avenida Libertad 10', '08001', 'Barcelona', 'España'),
(3, 'Carlos', 'López', 'carlos.lopez@email.com', '555555555', '11223344C', 'Plaza España 5', '41001', 'Sevilla', 'España');

INSERT INTO cliente (id_cliente, id_persona, tipo, razon_social, nif, fecha_registro) VALUES
(1, 1, 'Empresa', 'EcoSolutions S.L.', 'B12345678', '2025-01-15'),
(2, 2, 'Autónomo', 'María Gómez Consulting', '87654321B', '2025-02-20');

INSERT INTO usuario (id_usuario, id_persona, fecha_nacimiento, rol, preferencias, password) VALUES
(1, 1, '1985-03-10', 'Administrador', '{"idioma": "es", "notificaciones": true}', 'hashed_pass_123'),
(2, 3, '1990-07-22', 'Editor', '{"idioma": "es", "notificaciones": false}', 'hashed_pass_456');

INSERT INTO actividad (id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones) VALUES
(1, 'Taller', 'Taller de Reciclaje', 'Taller práctico sobre reciclaje de plásticos', 'Juan Pérez', '2 horas', 500.00, 10.0, 750.00, '50 participantes, 90% satisfacción', 'Excelente', 'Sin incidencias'),
(2, 'Conferencia', 'Conferencia Sostenibilidad', 'Charla sobre sostenibilidad en empresas', 'María Gómez', '1 hora', 300.00, 5.0, 450.00, '30 asistentes, 85% satisfacción', 'Buena', 'Falta de proyector');

INSERT INTO participante (id_participante, id_persona, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro) VALUES
(1, 2, 1, 'Asistente', 'Redes sociales', 1, '2025-01-10'),
(2, 3, 2, 'Asistente', 'Recomendación', 2, '2025-02-15');

INSERT INTO empresa (id_empresa, nombre, sector, logo, ubicacion) VALUES
(1, 'GreenTech', 'Tecnología Verde', 'logo_greentech.png', 'Madrid, España'),
(2, 'EcoConsulting', 'Consultoría Ambiental', 'logo_ecoconsulting.png', 'Barcelona, España');

INSERT INTO generadoria (id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion) VALUES
(1, 'EcoBot', 'Generador de contenido sobre sostenibilidad', 1, '{"modelo": "GPT-4", "idioma": "es"}', 'Post sobre reciclaje', '2025-06-20'),
(2, 'GreenWriter', 'Generador de informes ambientales', 2, '{"modelo": "BERT", "idioma": "es"}', 'Informe climático', '2025-06-25');

INSERT INTO tipo_publicacion (id_tipo_publicacion, nombre) VALUES
(1, 'Artículo'),
(2, 'Post Redes Sociales');

INSERT INTO plantilla (id_plantilla, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion) VALUES
(1, 'Plantilla Artículo Sostenibilidad', 'Artículo', 'Introducción sobre sostenibilidad...', '2025-01-01', '2025-06-15'),
(2, 'Plantilla Post Redes', 'Post', '¡Únete al cambio! #Sostenibilidad', '2025-02-01', '2025-06-20');

INSERT INTO publicacion (id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia, id_generador_ia, feedback_empresa, id_tipo_publicacion, id_plantilla) VALUES
(1, 'El Futuro del Reciclaje', 'Artículo sobre nuevas tecnologías de reciclaje', 'Carlos López', '2025-06-10', 'Publicado', 'reciclaje, tecnología', 'reciclaje, sostenibilidad', 1, 1, 'Buen enfoque, añadir más ejemplos', 1, 1),
(2, 'Post Sostenibilidad', '¡Cuidemos el planeta! #Eco', 'María Gómez', '2025-06-15', 'Programado', 'sostenibilidad, medioambiente', 'eco, verde', 1, 2, 'Perfecto para redes', 2, 2);

INSERT INTO proyecto (id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto) VALUES
(1, 'Proyecto Reciclaje Urbano', 'Implementar puntos de reciclaje en Madrid', '2025-01-01', '2025-12-31', 'Madrid', 'Juan Pérez', 'En curso', 'Reducir residuos en un 20%', 10000.00),
(2, 'Campaña Sostenibilidad', 'Promover prácticas sostenibles', '2025-03-01', '2025-09-30', 'Barcelona', 'María Gómez', 'Planificado', 'Concienciar a 1000 personas', 5000.00);

INSERT INTO fecha_actividad (fecha) VALUES
('2025-07-01'),
('2025-08-15');

INSERT INTO actividad_fecha (id_actividad, id_fecha) VALUES
(1, 1),
(2, 2);

INSERT INTO proyecto_actividad (id_proyecto, id_actividad) VALUES
(1, 1),
(2, 2);

INSERT INTO documento (id_documento, titulo, descripcion, fecha_subida, tipo, tematica) VALUES
(1, 'Guía de Reciclaje', 'Manual para clasificar residuos', '2025-06-01', 'PDF', 'Reciclaje'),
(2, 'Informe Sostenibilidad', 'Reporte anual de sostenibilidad', '2025-06-15', 'PDF', 'Sostenibilidad');

INSERT INTO evento (id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica) VALUES
(1, 'Feria Eco 2025', 'Feria', 'Recinto Ferial', '2025-07-10', '2025-07-12', 'Madrid', 'Sostenibilidad'),
(2, 'Congreso Verde', 'Congreso', 'Palacio de Congresos', '2025-08-20', '2025-08-22', 'Barcelona', 'Medioambiente');

INSERT INTO actividad_evento (id_actividad, id_evento) VALUES
(1, 1),
(2, 2);

INSERT INTO factura (id_factura, id_cliente, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf) VALUES
(1, 1, 'Servicio', 'EcoSolutions S.L.', 'Calle Mayor 1', 'B12345678', '2025-06-20', '2025-07-20', 'Taller de Reciclaje', 'Juan Pérez', 21.0, 750.00, 619.83, 'F2025-001', 'Transferencia', 0.0),
(2, 2, 'Servicio', 'María Gómez Consulting', 'Avenida Libertad 10', '87654321B', '2025-06-25', '2025-07-25', 'Conferencia Sostenibilidad', 'María Gómez', 21.0, 450.00, 371.90, 'F2025-002', 'Tarjeta', 0.0);

INSERT INTO log_sistema (id_log_sistema, fecha, usuario_id, accion, descripcion, nivel) VALUES
(1, '2025-06-20 10:00:00', 1, 'Creación Publicación', 'Creada publicación ID 1', 'INFO'),
(2, '2025-06-25 12:00:00', 2, 'Edición Plantilla', 'Editada plantilla ID 2', 'INFO');

INSERT INTO auditoria_publicacion (id_auditoria_publicacion, publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones) VALUES
(1, 1, 1, '2025-06-10', 1, '{"tema": "reciclaje"}', 'Artículo generado', 'Buen resultado'),
(2, 2, 2, '2025-06-15', 2, '{"tema": "sostenibilidad"}', 'Post generado', 'Revisar tono');

INSERT INTO tema_ambiental (id_tema_ambiental, nombre, descripcion, relevancia) VALUES
(1, 'Reciclaje', 'Procesos de reciclaje de materiales', 'Alta'),
(2, 'Energía Renovable', 'Uso de energías renovables', 'Media');

INSERT INTO tag (id_tag, palabra_clave, categoria, frecuencia_uso) VALUES
(1, 'reciclaje', 'Medioambiente', 10),
(2, 'sostenibilidad', 'Medioambiente', 15);

INSERT INTO redsocial (id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion) VALUES
(1, 'Twitter', 'EcoMadrid', '{"token": "xyz"}', '{"hora": "10:00"}', 'Conectado', '2025-06-15'),
(2, 'Instagram', 'GreenBCN', '{"token": "abc"}', '{"hora": "12:00"}', 'Conectado', '2025-06-20');

INSERT INTO programacion (id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable) VALUES
(1, 1, 1, '2025-07-01 10:00:00', 'Programado', 'Notificar al responsable', 'Juan Pérez'),
(2, 2, 2, '2025-07-05 12:00:00', 'Programado', 'Notificar al equipo', 'María Gómez');

INSERT INTO recurso_multimedia (id_recurso_multimedia, tipo, titulo, fecha_subida, autor) VALUES
(1, 'Imagen', 'Foto Reciclaje', '2025-06-01', 'Carlos López'),
(2, 'Video', 'Video Sostenibilidad', '2025-06-10', 'María Gómez');

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

