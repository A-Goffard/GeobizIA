Modelo de Datos Actualizado
Rol

id_rol
nombre
descripcion

Métodos:

crear_rol(self, id_rol, nombre, descripcion) -> RolConstructor!!!
get_id_rol() -> id_rol
set_id_rol(id_rol) -> id_rol
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_descripcion() -> descripcion
set_descripcion(descripcion) -> descripcion


Persona

id_persona
nombre
apellido
email
telefono
dni
direccion
cp
poblacion
pais

Métodos:

crear_persona(self, id_persona, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) -> PersonaConstructor!!!
get_id_persona() -> id_persona
set_id_persona(id_persona) -> id_persona
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_apellido() -> apellido
set_apellido(apellido) -> apellido
get_email() -> email
set_email(email) -> email
get_telefono() -> telefono
set_telefono(telefono) -> telefono
get_dni() -> dni
set_dni(dni) -> dni
get_direccion() -> direccion
set_direccion(direccion) -> direccion
get_cp() -> cp
set_cp(cp) -> cp
get_poblacion() -> poblacion
set_poblacion(poblacion) -> poblacion
get_pais() -> pais
set_pais(pais) -> pais


Cliente

id_cliente
id_persona
tipo
razon_social
nif
fecha_registro
(nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais heredados de Persona)

Métodos:

crear_cliente(self, id_cliente, id_persona, tipo, razon_social, nif, fecha_registro, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) -> ClienteConstructor!!!
get_id_cliente() -> id_cliente
set_id_cliente(id_cliente) -> id_cliente
get_id_persona() -> id_persona
set_id_persona(id_persona) -> id_persona
get_tipo() -> tipo
set_tipo(tipo) -> tipo
get_razon_social() -> razon_social
set_razon_social(razon_social) -> razon_social
get_nif() -> nif
set_nif(nif) -> nif
get_fecha_registro() -> fecha_registro
set_fecha_registro(fecha_registro) -> fecha_registro
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_apellido() -> apellido
set_apellido(apellido) -> apellido
get_email() -> email
set_email(email) -> email
get_telefono() -> telefono
set_telefono(telefono) -> telefono
get_dni() -> dni
set_dni(dni) -> dni
get_direccion() -> direccion
set_direccion(direccion) -> direccion
get_cp() -> cp
set_cp(cp) -> cp
get_poblacion() -> poblacion
set_poblacion(poblacion) -> poblacion
get_pais() -> pais
set_pais(pais) -> pais


Usuario

id_usuario
id_persona
fecha_nacimiento
rol
preferencias
password
(nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais heredados de Persona)

Métodos:

crear_usuario(self, id_usuario, id_persona, fecha_nacimiento, rol, preferencias, password, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) -> UsuarioConstructor!!!
get_id_usuario() -> id_usuario
set_id_usuario(id_usuario) -> id_usuario
get_id_persona() -> id_persona
set_id_persona(id_persona) -> id_persona
get_fecha_nacimiento() -> fecha_nacimiento
set_fecha_nacimiento(fecha_nacimiento) -> fecha_nacimiento
get_rol() -> rol
set_rol(rol) -> rol
get_preferencias() -> preferencias
set_preferencias(preferencias) -> preferencias
get_password() -> password
set_password(password) -> password
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_apellido() -> apellido
set_apellido(apellido) -> apellido
get_email() -> email
set_email(email) -> email
get_telefono() -> telefono
set_telefono(telefono) -> telefono
get_dni() -> dni
set_dni(dni) -> dni
get_direccion() -> direccion
set_direccion(direccion) -> direccion
get_cp() -> cp
set_cp(cp) -> cp
get_poblacion() -> poblacion
set_poblacion(poblacion) -> poblacion
get_pais() -> pais
set_pais(pais) -> pais


Actividad

id_actividad
tipo
nombre
descripcion
responsable
duracion
coste_economico
coste_horas
facturacion
resultados
valoracion
observaciones

Métodos:

crear_actividad(self, id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones) -> ActividadConstructor!!!
get_id_actividad() -> id_actividad
set_id_actividad(id_actividad) -> id_actividad
get_tipo() -> tipo
set_tipo(tipo) -> tipo
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_descripcion() -> descripcion
set_descripcion(descripcion) -> descripcion
get_responsable() -> responsable
set_responsable(responsable) -> responsable
get_duracion() -> duracion
set_duracion(duracion) -> duracion
get_coste_economico() -> coste_economico
set_coste_economico(coste_economico) -> coste_economico
get_coste_horas() -> coste_horas
set_coste_horas(coste_horas) -> coste_horas
get_facturacion() -> facturacion
set_facturacion(facturacion) -> facturacion
get_resultados() -> resultados
set_resultados(resultados) -> resultados
get_valoracion() -> valoracion
set_valoracion(valoracion) -> valoracion
get_observaciones() -> observaciones
set_observaciones(observaciones) -> observaciones


Participante

id_participante
id_persona
numero_personas_juntas
rol
como_conocer
actividad_id
fecha_registro
(nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais heredados de Persona)

Métodos:

crear_participante(self, id_participante, id_persona, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) -> ParticipanteConstructor!!!
get_id_participante() -> id_participante
set_id_participante(id_participante) -> id_participante
get_id_persona() -> id_persona
set_id_persona(id_persona) -> id_persona
get_numero_personas_juntas() -> numero_personas_juntas
set_numero_personas_juntas(numero_personas_juntas) -> numero_personas_juntas
get_rol() -> rol
set_rol(rol) -> rol
get_como_conocer() -> como_conocer
set_como_conocer(como_conocer) -> como_conocer
get_actividad_id() -> actividad_id
set_actividad_id(actividad_id) -> actividad_id
get_fecha_registro() -> fecha_registro
set_fecha_registro(fecha_registro) -> fecha_registro
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_apellido() -> apellido
set_apellido(apellido) -> apellido
get_email() -> email
set_email(email) -> email
get_telefono() -> telefono
set_telefono(telefono) -> telefono
get_dni() -> dni
set_dni(dni) -> dni
get_direccion() -> direccion
set_direccion(direccion) -> direccion
get_cp() -> cp
set_cp(cp) -> cp
get_poblacion() -> poblacion
set_poblacion(poblacion) -> poblacion
get_pais() -> pais
set_pais(pais) -> pais


Empresa

id_empresa
nombre
sector
logo
ubicacion

Métodos:

crear_empresa(self, id_empresa, nombre, sector, logo, ubicacion) -> EmpresaConstructor!!!
get_id_empresa() -> id_empresa
set_id_empresa(id_empresa) -> id_empresa
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_sector() -> sector
set_sector(sector) -> sector
get_logo() -> logo
set_logo(logo) -> logo
get_ubicacion() -> ubicacion
set_ubicacion(ubicacion) -> ubicacion


GeneradorIA

id_generador_ia
nombre
descripcion
empresa_id
configuraciones
ejemplos_estilo
ultima_generacion

Métodos:

crear_generador_ia(self, id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion) -> GeneradorIAConstructor!!!
get_id_generador_ia() -> id_generador_ia
set_id_generador_ia(id_generador_ia) -> id_generador_ia
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_descripcion() -> descripcion
set_descripcion(descripcion) -> descripcion
get_empresa_id() -> empresa_id
set_empresa_id(empresa_id) -> empresa_id
get_configuraciones() -> configuraciones
set_configuraciones(configuraciones) -> configuraciones
get_ejemplos_estilo() -> ejemplos_estilo
set_ejemplos_estilo(ejemplos_estilo) -> ejemplos_estilo
get_ultima_generacion() -> ultima_generacion
set_ultima_generacion(ultima_generacion) -> ultima_generacion


TipoPublicacion

id_tipo_publicacion
nombre

Métodos:

crear_tipo_publicacion(self, id_tipo_publicacion, nombre) -> TipoPublicacionConstructor!!!
get_id_tipo_publicacion() -> id_tipo_publicacion
set_id_tipo_publicacion(id_tipo_publicacion) -> id_tipo_publicacion
get_nombre() -> nombre
set_nombre(nombre) -> nombre


Plantilla

id_plantilla
titulo
tipo
contenido_base
fecha_creacion
ultima_modificacion

Métodos:

crear_plantilla(self, id_plantilla, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion) -> PlantillaConstructor!!!
get_id_plantilla() -> id_plantilla
set_id_plantilla(id_plantilla) -> id_plantilla
get_titulo() -> titulo
set_titulo(titulo) -> titulo
get_tipo() -> tipo
set_tipo(tipo) -> tipo
get_contenido_base() -> contenido_base
set_contenido_base(contenido_base) -> contenido_base
get_fecha_creacion() -> fecha_creacion
set_fecha_creacion(fecha_creacion) -> fecha_creacion
get_ultima_modificacion() -> ultima_modificacion
set_ultima_modificacion(ultima_modificacion) -> ultima_modificacion


Publicacion

id_publicacion
titulo
contenido
autor
fecha_creacion
estado
tags
palabras_clave
generada_por_ia
id_generador_ia
feedback_empresa
id_tipo_publicacion
id_plantilla

Métodos:

crear_publicacion(self, id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia, id_generador_ia, feedback_empresa, id_tipo_publicacion, id_plantilla) -> PublicacionConstructor!!!
get_id_publicacion() -> id_publicacion
set_id_publicacion(id_publicacion) -> id_publicacion
get_titulo() -> titulo
set_titulo(titulo) -> titulo
get_contenido() -> contenido
set_contenido(contenido) -> contenido
get_autor() -> autor
set_autor(autor) -> autor
get_fecha_creacion() -> fecha_creacion
set_fecha_creacion(fecha_creacion) -> fecha_creacion
get_estado() -> estado
set_estado(estado) -> estado
get_tags() -> tags
set_tags(tags) -> tags
get_palabras_clave() -> palabras_clave
set_palabras_clave(palabras_clave) -> palabras_clave
get_generada_por_ia() -> generada_por_ia
set_generada_por_ia(generada_por_ia) -> generada_por_ia
get_id_generador_ia() -> id_generador_ia
set_id_generador_ia(id_generador_ia) -> id_generador_ia
get_feedback_empresa() -> feedback_empresa
set_feedback_empresa(feedback_empresa) -> feedback_empresa
get_id_tipo_publicacion() -> id_tipo_publicacion
set_id_tipo_publicacion(id_tipo_publicacion) -> id_tipo_publicacion
get_id_plantilla() -> id_plantilla
set_id_plantilla(id_plantilla) -> id_plantilla


Proyecto

id_proyecto
nombre
descripcion
fecha_inicio
fecha_fin
poblacion
responsable
estado
objetivos
presupuesto

Métodos:

crear_proyecto(self, id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto) -> ProyectoConstructor!!!
get_id_proyecto() -> id_proyecto
set_id_proyecto(id_proyecto) -> id_proyecto
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_descripcion() -> descripcion
set_descripcion(descripcion) -> descripcion
get_fecha_inicio() -> fecha_inicio
set_fecha_inicio(fecha_inicio) -> fecha_inicio
get_fecha_fin() -> fecha_fin
set_fecha_fin(fecha_fin) -> fecha_fin
get_poblacion() -> poblacion
set_poblacion(poblacion) -> poblacion
get_responsable() -> responsable
set_responsable(responsable) -> responsable
get_estado() -> estado
set_estado(estado) -> estado
get_objetivos() -> objetivos
set_objetivos(objetivos) -> objetivos
get_presupuesto() -> presupuesto
set_presupuesto(presupuesto) -> presupuesto


FechaActividad

id_fecha
fecha

Métodos:

crear_fecha_actividad(self, id_fecha, fecha) -> FechaActividadConstructor!!!
get_id_fecha() -> id_fecha
set_id_fecha(id_fecha) -> id_fecha
get_fecha() -> fecha
set_fecha(fecha) -> fecha


ActividadFecha

id_actividad
id_fecha

Métodos:

crear_actividad_fecha(self, id_actividad, id_fecha) -> ActividadFechaConstructor!!!
get_id_actividad() -> id_actividad
set_id_actividad(id_actividad) -> id_actividad
get_id_fecha() -> id_fecha
set_id_fecha(id_fecha) -> id_fecha


ProyectoActividad

id_proyecto
id_actividad

Métodos:

crear_proyecto_actividad(self, id_proyecto, id_actividad) -> ProyectoActividadConstructor!!!
get_id_proyecto() -> id_proyecto
set_id_proyecto(id_proyecto) -> id_proyecto
get_id_actividad() -> id_actividad
set_id_actividad(id_actividad) -> id_actividad


Documento

id_documento
titulo
descripcion
fecha_subida
tipo
tematica

Métodos:

crear_documento(self, id_documento, titulo, descripcion, fecha_subida, tipo, tematica) -> DocumentoConstructor!!!
get_id_documento() -> id_documento
set_id_documento(id_documento) -> id_documento
get_titulo() -> titulo
set_titulo(titulo) -> titulo
get_descripcion() -> descripcion
set_descripcion(descripcion) -> descripcion
get_fecha_subida() -> fecha_subida
set_fecha_subida(fecha_subida) -> fecha_subida
get_tipo() -> tipo
set_tipo(tipo) -> tipo
get_tematica() -> tematica
set_tematica(tematica) -> tematica


Evento

id_evento
nombre
tipo
lugar
fecha_comienzo
fecha_final
poblacion
tematica

Métodos:

crear_evento(self, id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica) -> EventoConstructor!!!
get_id_evento() -> id_evento
set_id_evento(id_evento) -> id_evento
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_tipo() -> tipo
set_tipo(tipo) -> tipo
get_lugar() -> lugar
set_lugar(lugar) -> lugar
get_fecha_comienzo() -> fecha_comienzo
set_fecha_comienzo(fecha_comienzo) -> fecha_comienzo
get_fecha_final() -> fecha_final
set_fecha_final(fecha_final) -> fecha_final
get_poblacion() -> poblacion
set_poblacion(poblacion) -> poblacion
get_tematica() -> tematica
set_tematica(tematica) -> tematica


ActividadEvento

id_actividad
id_evento

Métodos:

crear_actividad_evento(self, id_actividad, id_evento) -> ActividadEventoConstructor!!!
get_id_actividad() -> id_actividad
set_id_actividad(id_actividad) -> id_actividad
get_id_evento() -> id_evento
set_id_evento(id_evento) -> id_evento


Factura

id_factura
id_cliente
tipo
nombre
direccion
nif
fecha_facturacion
fecha_vencimiento
concepto
responsable
iva
coste_total
base_imponible
numero_factura
tipo_pago
irpf

Métodos:

crear_factura(self, id_factura, id_cliente, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf) -> FacturaConstructor!!!
get_id_factura() -> id_factura
set_id_factura(id_factura) -> id_factura
get_id_cliente() -> id_cliente
set_id_cliente(id_cliente) -> id_cliente
get_tipo() -> tipo
set_tipo(tipo) -> tipo
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_direccion() -> direccion
set_direccion(direccion) -> direccion
get_nif() -> nif
set_nif(nif) -> nif
get_fecha_facturacion() -> fecha_facturacion
set_fecha_facturacion(fecha_facturacion) -> fecha_facturacion
get_fecha_vencimiento() -> fecha_vencimiento
set_fecha_vencimiento(fecha_vencimiento) -> fecha_vencimiento
get_concepto() -> concepto
set_concepto(concepto) -> concepto
get_responsable() -> responsable
set_responsable(responsable) -> responsable
get_iva() -> iva
set_iva(iva) -> iva
get_coste_total() -> coste_total
set_coste_total(coste_total) -> coste_total
get_base_imponible() -> base_imponible
set_base_imponible(base_imponible) -> base_imponible
get_numero_factura() -> numero_factura
set_numero_factura(numero_factura) -> numero_factura
get_tipo_pago() -> tipo_pago
set_tipo_pago(tipo_pago) -> tipo_pago
get_irpf() -> irpf
set_irpf(irpf) -> irpf


FacturaActividad

id_factura
id_actividad

Métodos:

crear_factura_actividad(self, id_factura, id_actividad) -> FacturaActividadConstructor!!!
get_id_factura() -> id_factura
set_id_factura(id_factura) -> id_factura
get_id_actividad() -> id_actividad
set_id_actividad(id_actividad) -> id_actividad


LogSistema

id_log_sistema
fecha
usuario_id
accion
descripcion
nivel

Métodos:

crear_log_sistema(self, id_log_sistema, fecha, usuario_id, accion, descripcion, nivel) -> LogSistemaConstructor!!!
get_id_log_sistema() -> id_log_sistema
set_id_log_sistema(id_log_sistema) -> id_log_sistema
get_fecha() -> fecha
set_fecha(fecha) -> fecha
get_usuario_id() -> usuario_id
set_usuario_id(usuario_id) -> usuario_id
get_accion() -> accion
set_accion(accion) -> accion
get_descripcion() -> descripcion
set_descripcion(descripcion) -> descripcion
get_nivel() -> nivel
set_nivel(nivel) -> nivel


AuditoriaPublicacion

id_auditoria_publicacion
publicacion_id
generador_ia_id
fecha_generacion
usuario_id
parametros_entrada
resultado
observaciones

Métodos:

crear_auditoria_publicacion(self, id_auditoria_publicacion, publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones) -> AuditoriaPublicacionConstructor!!!
get_id_auditoria_publicacion() -> id_auditoria_publicacion
set_id_auditoria_publicacion(id_auditoria_publicacion) -> id_auditoria_publicacion
get_publicacion_id() -> publicacion_id
set_publicacion_id(publicacion_id) -> publicacion_id
get_generador_ia_id() -> generador_ia_id
set_generador_ia_id(generador_ia_id) -> generador_ia_id
get_fecha_generacion() -> fecha_generacion
set_fecha_generacion(fecha_generacion) -> fecha_generacion
get_usuario_id() -> usuario_id
set_usuario_id(usuario_id) -> usuario_id
get_parametros_entrada() -> parametros_entrada
set_parametros_entrada(parametros_entrada) -> parametros_entrada
get_resultado() -> resultado
set_resultado(resultado) -> resultado
get_observaciones() -> observaciones
set_observaciones(observaciones) -> observaciones


TemaAmbiental

id_tema_ambiental
nombre
descripcion
relevancia

Métodos:

crear_tema_ambiental(self, id_tema_ambiental, nombre, descripcion, relevancia) -> TemaAmbientalConstructor!!!
get_id_tema_ambiental() -> id_tema_ambiental
set_id_tema_ambiental(id_tema_ambiental) -> id_tema_ambiental
get_nombre() -> nombre
set_nombre(nombre) -> nombre
get_descripcion() -> descripcion
set_descripcion(descripcion) -> descripcion
get_relevancia() -> relevancia
set_relevancia(relevancia) -> relevancia


Tag

id_tag
palabra_clave
categoria
frecuencia_uso

Métodos:

crear_tag(self, id_tag, palabra_clave, categoria, frecuencia_uso) -> TagConstructor!!!
get_id_tag() -> id_tag
set_id_tag(id_tag) -> id_tag
get_palabra_clave() -> palabra_clave
set_palabra_clave(palabra_clave) -> palabra_clave
get_categoria() -> categoria
set_categoria(categoria) -> categoria
get_frecuencia_uso() -> frecuencia_uso
set_frecuencia_uso(frecuencia_uso) -> frecuencia_uso


RedSocial

id_red_social
plataforma
nombre_cuenta
credenciales
preferencias_publicacion
estado_conexion
ultima_publicacion

Métodos:

crear_red_social(self, id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion) -> RedSocialConstructor!!!
get_id_red_social() -> id_red_social
set_id_red_social(id_red_social) -> id_red_social
get_plataforma() -> plataforma
set_plataforma(plataforma) -> plataforma
get_nombre_cuenta() -> nombre_cuenta
set_nombre_cuenta(nombre_cuenta) -> nombre_cuenta
get_credenciales() -> credenciales
set_credenciales(credenciales) -> credenciales
get_preferencias_publicacion() -> preferencias_publicacion
set_preferencias_publicacion(preferencias_publicacion) -> preferencias_publicacion
get_estado_conexion() -> estado_conexion
set_estado_conexion(estado_conexion) -> estado_conexion
get_ultima_publicacion() -> ultima_publicacion
set_ultima_publicacion(ultima_publicacion) -> ultima_publicacion


Programacion

id_programacion
publicacion_id
red_social_id
fecha_programada
estado
notificaciones
responsable

Métodos:

crear_programacion(self, id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable) -> ProgramacionConstructor!!!
get_id_programacion() -> id_programacion
set_id_programacion(id_programacion) -> id_programacion
get_publicacion_id() -> publicacion_id
set_publicacion_id(publicacion_id) -> publicacion_id
get_red_social_id() -> red_social_id
set_red_social_id(red_social_id) -> red_social_id
get_fecha_programada() -> fecha_programada
set_fecha_programada(fecha_programada) -> fecha_programada
get_estado() -> estado
set_estado(estado) -> estado
get_notificaciones() -> notificaciones
set_notificaciones(notificaciones) -> notificaciones
get_responsable() -> responsable
set_responsable(responsable) -> responsable


RecursoMultimedia

id_recurso_multimedia
tipo
titulo
fecha_subida
autor

Métodos:

crear_recurso_multimedia(self, id_recurso_multimedia, tipo, titulo, fecha_subida, autor) -> RecursoMultimediaConstructor!!!
get_id_recurso_multimedia() -> id_recurso_multimedia
set_id_recurso_multimedia(id_recurso_multimedia) -> id_recurso_multimedia
get_tipo() -> tipo
set_tipo(tipo) -> tipo
get_titulo() -> titulo
set_titulo(titulo) -> titulo
get_fecha_subida() -> fecha_subida
set_fecha_subida(fecha_subida) -> fecha_subida
get_autor() -> autor
set_autor(autor) -> autor


PublicacionTag

id_publicacion
id_tag

Métodos:

crear_publicacion_tag(self, id_publicacion, id_tag) -> PublicacionTagConstructor!!!
get_id_publicacion() -> id_publicacion
set_id_publicacion(id_publicacion) -> id_publicacion
get_id_tag() -> id_tag
set_id_tag(id_tag) -> id_tag


TemaAmbientalTag

id_tema_ambiental
id_tag

Métodos:

crear_tema_ambiental_tag(self, id_tema_ambiental, id_tag) -> TemaAmbientalTagConstructor!!!
get_id_tema_ambiental() -> id_tema_ambiental
set_id_tema_ambiental(id_tema_ambiental) -> id_tema_ambiental
get_id_tag() -> id_tag
set_id_tag(id_tag) -> id_tag


RecursoMultimediaTag

id_recurso_multimedia
id_tag

Métodos:

crear_recurso_multimedia_tag(self, id_recurso_multimedia, id_tag) -> RecursoMultimediaTagConstructor!!!
get_id_recurso_multimedia() -> id_recurso_multimedia
set_id_recurso_multimedia(id_recurso_multimedia) -> id_recurso_multimedia
get_id_tag() -> id_tag
set_id_tag(id_tag) -> id_tag


DocumentoTag

id_documento
id_tag

Métodos:

crear_documento_tag(self, id_documento, id_tag) -> DocumentoTagConstructor!!!
get_id_documento() -> id_documento
set_id_documento(id_documento) -> id_documento
get_id_tag() -> id_tag
set_id_tag(id_tag) -> id_tag


PlantillaTipoPublicacion

id_plantilla
id_tipo_publicacion

Métodos:

crear_plantilla_tipo_publicacion(self, id_plantilla, id_tipo_publicacion) -> PlantillaTipoPublicacionConstructor!!!
get_id_plantilla() -> id_plantilla
set_id_plantilla(id_plantilla) -> id_plantilla
get_id_tipo_publicacion() -> id_tipo_publicacion
set_id_tipo_publicacion(id_tipo_publicacion) -> id_tipo_publicacion


TipoPublicacionRedsocial

id_tipo_publicacion
id_red_social

Métodos:

crear_tipo_publicacion_redsocial(self, id_tipo_publicacion, id_red_social) -> TipoPublicacionRedsocialConstructor!!!
get_id_tipo_publicacion() -> id_tipo_publicacion
set_id_tipo_publicacion(id_tipo_publicacion) -> id_tipo_publicacion
get_id_red_social() -> id_red_social
set_id_red_social(id_red_social) -> id_red_social
