-- Tabla: usuario
INSERT INTO usuario (id_usuario, nombre, apellido, email, telefono, fecha_nacimiento, direccion, dni, cp, poblacion, pais, rol, preferencias, password)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM usuario WHERE id_usuario = ?;

UPDATE usuario SET nombre=?, apellido=?, email=?, telefono=?, fecha_nacimiento=?, direccion=?, dni=?, cp=?, poblacion=?, pais=?, rol=?, preferencias=?, password=?
WHERE id_usuario = ?;

DELETE FROM usuario WHERE id_usuario = ?;

-- Tabla: participante
INSERT INTO participante (id_participante, nombre, apellido, email, telefono, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM participante WHERE id_participante = ?;

UPDATE participante SET nombre=?, apellido=?, email=?, telefono=?, numero_personas_juntas=?, rol=?, como_conocer=?, actividad_id=?, fecha_registro=?
WHERE id_participante = ?;

DELETE FROM participante WHERE id_participante = ?;

-- Tabla: publicacion
INSERT INTO publicacion (id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia, id_generador_ia, feedback_empresa)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM publicacion WHERE id_publicacion = ?;

UPDATE publicacion SET titulo=?, contenido=?, autor=?, fecha_creacion=?, estado=?, tags=?, palabras_clave=?, generada_por_ia=?, id_generador_ia=?, feedback_empresa=?
WHERE id_publicacion = ?;

DELETE FROM publicacion WHERE id_publicacion = ?;

-- Tabla: cliente
INSERT INTO cliente (id_cliente, tipo, nombre, apellido, razon_social, nif, dni, email, telefono, direccion, cp, poblacion, pais, fecha_registro)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM cliente WHERE id_cliente = ?;

UPDATE cliente SET tipo=?, nombre=?, apellido=?, razon_social=?, nif=?, dni=?, email=?, telefono=?, direccion=?, cp=?, poblacion=?, pais=?, fecha_registro=?
WHERE id_cliente = ?;

DELETE FROM cliente WHERE id_cliente = ?;

-- Tabla: documento
INSERT INTO documento (id_documento, titulo, descripcion, fecha_subida, tipo, tematica)
VALUES (?, ?, ?, ?, ?, ?);

SELECT * FROM documento WHERE id_documento = ?;

UPDATE documento SET titulo=?, descripcion=?, fecha_subida=?, tipo=?, tematica=?
WHERE id_documento = ?;

DELETE FROM documento WHERE id_documento = ?;

-- Tabla: factura
INSERT INTO factura (id_factura, id_cliente, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM factura WHERE id_factura = ?;

UPDATE factura SET id_cliente=?, fecha_facturacion=?, fecha_vencimiento=?, concepto=?, responsable=?, iva=?, coste_total=?, base_imponible=?, numero_factura=?, tipo_pago=?, irpf=?
WHERE id_factura = ?;

DELETE FROM factura WHERE id_factura = ?;

-- Tabla: actividad
INSERT INTO actividad (id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, modificaciones)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM actividad WHERE id_actividad = ?;

UPDATE actividad SET tipo=?, nombre=?, descripcion=?, responsable=?, duracion=?, coste_economico=?, coste_horas=?, facturacion=?, resultados=?, valoracion=?, modificaciones=?
WHERE id_actividad = ?;

DELETE FROM actividad WHERE id_actividad = ?;

-- Tabla: proyecto
INSERT INTO proyecto (id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM proyecto WHERE id_proyecto = ?;

UPDATE proyecto SET nombre=?, descripcion=?, fecha_inicio=?, fecha_fin=?, poblacion=?, responsable=?, estado=?, objetivos=?, presupuesto=?
WHERE id_proyecto = ?;

DELETE FROM proyecto WHERE id_proyecto = ?;

-- Tabla: plantilla
INSERT INTO plantilla (id_plantilla, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion, relaciones)
VALUES (?, ?, ?, ?, ?, ?, ?);

SELECT * FROM plantilla WHERE id_plantilla = ?;

UPDATE plantilla SET titulo=?, tipo=?, contenido_base=?, fecha_creacion=?, ultima_modificacion=?, relaciones=?
WHERE id_plantilla = ?;

DELETE FROM plantilla WHERE id_plantilla = ?;

-- Tabla: empresa
INSERT INTO empresa (id_empresa, nombre, sector, logo, ubicacion)
VALUES (?, ?, ?, ?, ?);

SELECT * FROM empresa WHERE id_empresa = ?;

UPDATE empresa SET nombre=?, sector=?, logo=?, ubicacion=?
WHERE id_empresa = ?;

DELETE FROM empresa WHERE id_empresa = ?;

-- Tabla: evento
INSERT INTO evento (id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM evento WHERE id_evento = ?;

UPDATE evento SET nombre=?, tipo=?, lugar=?, fecha_comienzo=?, fecha_final=?, poblacion=?, tematica=?
WHERE id_evento = ?;

DELETE FROM evento WHERE id_evento = ?;

-- Tabla: generadoria
INSERT INTO generadoria (id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion)
VALUES (?, ?, ?, ?, ?, ?, ?);

SELECT * FROM generadoria WHERE id_generador_ia = ?;

UPDATE generadoria SET nombre=?, descripcion=?, empresa_id=?, configuraciones=?, ejemplos_estilo=?, ultima_generacion=?
WHERE id_generador_ia = ?;

DELETE FROM generadoria WHERE id_generador_ia = ?;

-- Tabla: log_sistema
INSERT INTO log_sistema (id_log_sistema, fecha, usuario_id, accion, descripcion, nivel)
VALUES (?, ?, ?, ?, ?, ?);

SELECT * FROM log_sistema WHERE id_log_sistema = ?;

UPDATE log_sistema SET fecha=?, usuario_id=?, accion=?, descripcion=?, nivel=?
WHERE id_log_sistema = ?;

DELETE FROM log_sistema WHERE id_log_sistema = ?;

-- Tabla: auditoria_publicacion
INSERT INTO auditoria_publicacion (id_auditoria_publicacion, publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM auditoria_publicacion WHERE id_auditoria_publicacion = ?;

UPDATE auditoria_publicacion SET publicacion_id=?, generador_ia_id=?, fecha_generacion=?, usuario_id=?, parametros_entrada=?, resultado=?, observaciones=?
WHERE id_auditoria_publicacion = ?;

DELETE FROM auditoria_publicacion WHERE id_auditoria_publicacion = ?;

-- Tabla: tema_ambiental
INSERT INTO tema_ambiental (id_tema_ambiental, nombre, descripcion, relevancia, relacion_actividades, relacion_publicaciones)
VALUES (?, ?, ?, ?, ?, ?);

SELECT * FROM tema_ambiental WHERE id_tema_ambiental = ?;

UPDATE tema_ambiental SET nombre=?, descripcion=?, relevancia=?, relacion_actividades=?, relacion_publicaciones=?
WHERE id_tema_ambiental = ?;

DELETE FROM tema_ambiental WHERE id_tema_ambiental = ?;

-- Tabla: tag
INSERT INTO tag (id_tag, palabra_clave, categoria, frecuencia_uso, relaciones)
VALUES (?, ?, ?, ?, ?);

SELECT * FROM tag WHERE id_tag = ?;

UPDATE tag SET palabra_clave=?, categoria=?, frecuencia_uso=?, relaciones=?
WHERE id_tag = ?;

DELETE FROM tag WHERE id_tag = ?;

-- Tabla: redsocial
INSERT INTO redsocial (id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion)
VALUES (?, ?, ?, ?, ?, ?, ?);

SELECT * FROM redsocial WHERE id_red_social = ?;

UPDATE redsocial SET plataforma=?, nombre_cuenta=?, credenciales=?, preferencias_publicacion=?, estado_conexion=?, ultima_publicacion=?
WHERE id_red_social = ?;

DELETE FROM redsocial WHERE id_red_social = ?;

-- Tabla: programacion
INSERT INTO programacion (id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable)
VALUES (?, ?, ?, ?, ?, ?, ?);

SELECT * FROM programacion WHERE id_programacion = ?;

UPDATE programacion SET publicacion_id=?, red_social_id=?, fecha_programada=?, estado=?, notificaciones=?, responsable=?
WHERE id_programacion = ?;

DELETE FROM programacion WHERE id_programacion = ?;

-- Tabla: recurso_multimedia
INSERT INTO recurso_multimedia (id_recurso_multimedia, tipo, titulo, fecha_subida, autor, relaciones)
VALUES (?, ?, ?, ?, ?, ?);

SELECT * FROM recurso_multimedia WHERE id_recurso_multimedia = ?;

UPDATE recurso_multimedia SET tipo=?, titulo=?, fecha_subida=?, autor=?, relaciones=?
WHERE id_recurso_multimedia = ?;

DELETE FROM recurso_multimedia WHERE id_recurso_multimedia = ?;
