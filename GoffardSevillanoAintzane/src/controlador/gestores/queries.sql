-- Tabla: usuarios
INSERT INTO usuarios (id_usuario, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais, fecha_nacimiento, preferencias, rol, password)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM usuarios WHERE id_usuario = ?;

UPDATE usuarios SET nombre=?, apellido=?, email=?, telefono=?, dni=?, direccion=?, cp=?, poblacion=?, pais=?, fecha_nacimiento=?, preferencias=?, rol=?, password=?
WHERE id_usuario = ?;

DELETE FROM usuarios WHERE id_usuario = ?;

-- Tabla: participantes
INSERT INTO participantes (id_participante, nombre, apellido, email, telefono, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM participantes WHERE id_participante = ?;

UPDATE participantes SET nombre=?, apellido=?, email=?, telefono=?, numero_personas_juntas=?, rol=?, como_conocer=?, actividad_id=?, fecha_registro=?
WHERE id_participante = ?;

DELETE FROM participantes WHERE id_participante = ?;

-- Tabla: publicaciones
INSERT INTO publicaciones (id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM publicaciones WHERE id_publicacion = ?;

UPDATE publicaciones SET titulo=?, contenido=?, autor=?, fecha_creacion=?, estado=?, tags=?, palabras_clave=?
WHERE id_publicacion = ?;

DELETE FROM publicaciones WHERE id_publicacion = ?;

-- Tabla: clientes
INSERT INTO clientes (id_cliente, nombre, apellido, email, telefono, tipo, direccion, cp, poblacion, pais, fecha_registro)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM clientes WHERE id_cliente = ?;

UPDATE clientes SET nombre=?, apellido=?, email=?, telefono=?, tipo=?, direccion=?, cp=?, poblacion=?, pais=?, fecha_registro=?
WHERE id_cliente = ?;

DELETE FROM clientes WHERE id_cliente = ?;

-- Tabla: documentos
INSERT INTO documentos (id_documento, titulo, descripcion, fecha_subida, tipo, tematica)
VALUES (?, ?, ?, ?, ?, ?);

SELECT * FROM documentos WHERE id_documento = ?;

UPDATE documentos SET titulo=?, descripcion=?, fecha_subida=?, tipo=?, tematica=?
WHERE id_documento = ?;

DELETE FROM documentos WHERE id_documento = ?;

-- Tabla: facturas
INSERT INTO facturas (id_factura, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM facturas WHERE id_factura = ?;

UPDATE facturas SET tipo=?, nombre=?, direccion=?, nif=?, fecha_facturacion=?, fecha_vencimiento=?, concepto=?, responsable=?, iva=?, coste_total=?, base_imponible=?, numero_factura=?, tipo_pago=?, irpf=?
WHERE id_factura = ?;

DELETE FROM facturas WHERE id_factura = ?;

-- Tabla: actividades
INSERT INTO actividades (id_actividad, tipo, nombre, fecha_ejecucion, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, modificaciones)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM actividades WHERE id_actividad = ?;

UPDATE actividades SET tipo=?, nombre=?, fecha_ejecucion=?, descripcion=?, responsable=?, duracion=?, coste_economico=?, coste_horas=?, facturacion=?, resultados=?, valoracion=?, modificaciones=?
WHERE id_actividad = ?;

DELETE FROM actividades WHERE id_actividad = ?;

-- Tabla: proyectos
INSERT INTO proyectos (id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, actividades, presupuesto)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM proyectos WHERE id_proyecto = ?;

UPDATE proyectos SET nombre=?, descripcion=?, fecha_inicio=?, fecha_fin=?, poblacion=?, responsable=?, estado=?, objetivos=?, actividades=?, presupuesto=?
WHERE id_proyecto = ?;

DELETE FROM proyectos WHERE id_proyecto = ?;

-- Tabla: roles
INSERT INTO roles (nombre, tareas_permitidas)
VALUES (?, ?);

SELECT * FROM roles WHERE nombre = ?;

UPDATE roles SET tareas_permitidas=?
WHERE nombre = ?;

DELETE FROM roles WHERE nombre = ?;

-- Tabla: redes_sociales
INSERT INTO redes_sociales (id_red_social, plataforma, nombre_cuenta, credenciales, empresa_id, preferencias_publicacion, estado_conexion, ultima_publicacion, relaciones)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM redes_sociales WHERE id_red_social = ?;

UPDATE redes_sociales SET plataforma=?, nombre_cuenta=?, credenciales=?, empresa_id=?, preferencias_publicacion=?, estado_conexion=?, ultima_publicacion=?, relaciones=?
WHERE id_red_social = ?;

DELETE FROM redes_sociales WHERE id_red_social = ?;

-- Tabla: temas_ambientales
INSERT INTO temas_ambientales (id_tema_ambiental, nombre, descripcion, relevancia, relacion_actividades, relacion_publicaciones)
VALUES (?, ?, ?, ?, ?, ?);

SELECT * FROM temas_ambientales WHERE id_tema_ambiental = ?;

UPDATE temas_ambientales SET nombre=?, descripcion=?, relevancia=?, relacion_actividades=?, relacion_publicaciones=?
WHERE id_tema_ambiental = ?;

DELETE FROM temas_ambientales WHERE id_tema_ambiental = ?;

-- Tabla: tags_palabras_clave
INSERT INTO tags_palabras_clave (id_tag, palabra_clave, categoria, frecuencia_uso, relaciones)
VALUES (?, ?, ?, ?, ?);

SELECT * FROM tags_palabras_clave WHERE id_tag = ?;

UPDATE tags_palabras_clave SET palabra_clave=?, categoria=?, frecuencia_uso=?, relaciones=?
WHERE id_tag = ?;

DELETE FROM tags_palabras_clave WHERE id_tag = ?;

-- Tabla: recursos_multimedia
INSERT INTO recursos_multimedia (id_recurso_multimedia, tipo, titulo, fecha_subida, autor, relaciones)
VALUES (?, ?, ?, ?, ?, ?);

SELECT * FROM recursos_multimedia WHERE id_recurso_multimedia = ?;

UPDATE recursos_multimedia SET tipo=?, titulo=?, fecha_subida=?, autor=?, relaciones=?
WHERE id_recurso_multimedia = ?;

DELETE FROM recursos_multimedia WHERE id_recurso_multimedia = ?;

-- Tabla: plantillas
INSERT INTO plantillas (id_plantilla, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion, relaciones)
VALUES (?, ?, ?, ?, ?, ?, ?);

SELECT * FROM plantillas WHERE id_plantilla = ?;

UPDATE plantillas SET titulo=?, tipo=?, contenido_base=?, fecha_creacion=?, ultima_modificacion=?, relaciones=?
WHERE id_plantilla = ?;

DELETE FROM plantillas WHERE id_plantilla = ?;

-- Tabla: empresas
INSERT INTO empresas (id_empresa, nombre, sector, valores, objetivos, redes_sociales, logo, ubicacion)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM empresas WHERE id_empresa = ?;

UPDATE empresas SET nombre=?, sector=?, valores=?, objetivos=?, redes_sociales=?, logo=?, ubicacion=?
WHERE id_empresa = ?;

DELETE FROM empresas WHERE id_empresa = ?;

-- Tabla: fisicas
INSERT INTO fisicas (id_cliente, nombre, apellido, email, telefono, tipo, direccion, cp, poblacion, pais, fecha_registro, dni, fecha_nacimiento)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM fisicas WHERE id_cliente = ?;

UPDATE fisicas SET nombre=?, apellido=?, email=?, telefono=?, tipo=?, direccion=?, cp=?, poblacion=?, pais=?, fecha_registro=?, dni=?, fecha_nacimiento=?
WHERE id_cliente = ?;

DELETE FROM fisicas WHERE id_cliente = ?;

-- Tabla: juridicas
INSERT INTO juridicas (id_cliente, nombre, apellido, email, telefono, tipo, direccion, cp, poblacion, pais, fecha_registro, nif)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM juridicas WHERE id_cliente = ?;

UPDATE juridicas SET nombre=?, apellido=?, email=?, telefono=?, tipo=?, direccion=?, cp=?, poblacion=?, pais=?, fecha_registro=?, nif=?
WHERE id_cliente = ?;

DELETE FROM juridicas WHERE id_cliente = ?;

-- Tabla: programaciones
INSERT INTO programaciones (id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable)
VALUES (?, ?, ?, ?, ?, ?, ?);

SELECT * FROM programaciones WHERE id_programacion = ?;

UPDATE programaciones SET publicacion_id=?, red_social_id=?, fecha_programada=?, estado=?, notificaciones=?, responsable=?
WHERE id_programacion = ?;

DELETE FROM programaciones WHERE id_programacion = ?;

-- Tabla: eventos
INSERT INTO eventos (id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM eventos WHERE id_evento = ?;

UPDATE eventos SET nombre=?, tipo=?, lugar=?, fecha_comienzo=?, fecha_final=?, poblacion=?, tematica=?
WHERE id_evento = ?;

DELETE FROM eventos WHERE id_evento = ?;

-- Tabla: generadores_ia
INSERT INTO generadores_ia (id_generador_ia, nombre, tipo_ia, configuraciones, empresa_id, plantillas, tags, temas_ambientales, ultima_generacion)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);

SELECT * FROM generadores_ia WHERE id_generador_ia = ?;

UPDATE generadores_ia SET nombre=?, tipo_ia=?, configuraciones=?, empresa_id=?, plantillas=?, tags=?, temas_ambientales=?, ultima_generacion=?
WHERE id_generador_ia = ?;

DELETE FROM generadores_ia WHERE id_generador_ia = ?;

-- Agrega más tablas y queries según tus entidades y atributos reales.
