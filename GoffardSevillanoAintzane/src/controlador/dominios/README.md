---

## Rol

nombre  
tareas_permitidas

Métodos:
crear_rol(self, nombre, tareas_permitidas) -> Rol  
Constructor!!!  
get_nombre() -> nombre  
set_nombre(nombre) -> nombre  
get_tareas_permitidas() -> tareas_permitidas  
set_tareas_permitidas(tareas_permitidas) -> tareas_permitidas  

---

## Persona

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

---

## Usuario

id_usuario  
id_persona  
fecha_nacimiento  
rol  
preferencias  
password  
(nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais heredados de Persona)

Métodos:
crear_usuario(self, id_usuario, id_persona, fecha_nacimiento, rol, preferencias, password, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) -> Usuario  
Constructor!!!  
get_id_usuario() -> id_usuario  
set_id_usuario(id_usuario) -> id_usuario  
get_nombre() -> nombre  
set_nombre(nombre) -> nombre  
get_apellido() -> apellido  
set_apellido(apellido) -> apellido  
get_email() -> email  
set_email(email) -> email  
get_telefono() -> telefono  
set_telefono(telefono) -> telefono  
get_fecha_nacimiento() -> fecha_nacimiento  
set_fecha_nacimiento(fecha_nacimiento) -> fecha_nacimiento  
get_direccion() -> direccion  
set_direccion(direccion) -> direccion  
get_dni() -> dni  
set_dni(dni) -> dni  
get_cp() -> cp  
set_cp(cp) -> cp  
get_poblacion() -> poblacion  
set_poblacion(poblacion) -> poblacion  
get_pais() -> pais  
set_pais(pais) -> pais  
get_rol() -> rol  
set_rol(rol) -> rol  
get_preferencias() -> preferencias  
set_preferencias(preferencias) -> preferencias  
get_password() -> password  
set_password(password) -> password  

---

## Tag

id_tag  
palabra_clave  
categoria  
frecuencia_uso  
relaciones

Métodos:
crear_tag(self, id_tag, palabra_clave, categoria, frecuencia_uso, relaciones) -> Tag  
Constructor!!!  
get_id_tag() -> id_tag  
set_id_tag(id_tag) -> id_tag  
get_palabra_clave() -> palabra_clave  
set_palabra_clave(palabra_clave) -> palabra_clave  
get_categoria() -> categoria  
set_categoria(categoria) -> categoria  
get_frecuencia_uso() -> frecuencia_uso  
set_frecuencia_uso(frecuencia_uso) -> frecuencia_uso  
get_relaciones() -> relaciones  
set_relaciones(relaciones) -> relaciones  

---

## TemaAmbiental

id_tema_ambiental  
nombre  
descripcion  
relevancia  
relacion_actividades  
relacion_publicaciones

Métodos:
crear_tema_ambiental(self, id_tema_ambiental, nombre, descripcion, relevancia, relacion_actividades, relacion_publicaciones) -> TemaAmbiental  
Constructor!!!  
get_id_tema_ambiental() -> id_tema_ambiental  
set_id_tema_ambiental(id_tema_ambiental) -> id_tema_ambiental  
get_nombre() -> nombre  
set_nombre(nombre) -> nombre  
get_descripcion() -> descripcion  
set_descripcion(descripcion) -> descripcion  
get_relevancia() -> relevancia  
set_relevancia(relevancia) -> relevancia  
get_relacion_actividades() -> relacion_actividades  
set_relacion_actividades(relacion_actividades) -> relacion_actividades  
get_relacion_publicaciones() -> relacion_publicaciones  
set_relacion_publicaciones(relacion_publicaciones) -> relacion_publicaciones  

---

## RedSocial

id_red_social  
plataforma  
nombre_cuenta  
credenciales  
preferencias_publicacion  
estado_conexion  
ultima_publicacion

Métodos:
crear_red_social(self, id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion) -> RedSocial  
Constructor!!!  
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

---

## RecursoMultimedia

id_recurso_multimedia  
tipo  
titulo  
fecha_subida  
autor  
relaciones

Métodos:
crear_recurso_multimedia(self, id_recurso_multimedia, tipo, titulo, fecha_subida, autor, relaciones) -> RecursoMultimedia  
Constructor!!!  
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
get_relaciones() -> relaciones  
set_relaciones(relaciones) -> relaciones  

---

## Publicacion

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

Métodos:
crear_publicacion(self, id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia, id_generador_ia, feedback_empresa) -> Publicacion  
Constructor!!!  
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

---

## Proyecto

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
crear_proyecto(self, id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto) -> Proyecto  
Constructor!!!  
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

---

## Programacion

id_programacion  
publicacion_id  
red_social_id  
fecha_programada  
estado  
notificaciones  
responsable

Métodos:
crear_programacion(self, id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable) -> Programacion  
Constructor!!!  
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

---

## Plantilla

id_plantilla  
titulo  
tipo  
contenido_base  
fecha_creacion  
ultima_modificacion  
relaciones

Métodos:
crear_plantilla(self, id_plantilla, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion, relaciones) -> Plantilla  
Constructor!!!  
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
get_relaciones() -> relaciones  
set_relaciones(relaciones) -> relaciones  

---

## Participante

id_participante  
id_persona  
numero_personas_juntas  
rol  
como_conocer  
actividad_id  
fecha_registro  
(nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais heredados de Persona)

Métodos:
crear_participante(self, id_participante, id_persona, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) -> Participante  
Constructor!!!  
get_id_participante() -> id_participante  
set_id_participante(id_participante) -> id_participante  
get_nombre() -> nombre  
set_nombre(nombre) -> nombre  
get_apellido() -> apellido  
set_apellido(apellido) -> apellido  
get_email() -> email  
set_email(email) -> email  
get_telefono() -> telefono  
set_telefono(telefono) -> telefono  
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

---

## LogSistema

id_log_sistema  
fecha  
usuario_id  
accion  
descripcion  
nivel

Métodos:
crear_log_sistema(self, id_log_sistema, fecha, usuario_id, accion, descripcion, nivel) -> LogSistema  
Constructor!!!  
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

---

## GeneradorIA

id_generador_ia  
nombre  
descripcion  
empresa_id  
configuraciones  
ejemplos_estilo  
ultima_generacion

Métodos:
crear_generador_ia(self, id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion) -> GeneradorIA  
Constructor!!!  
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

---

## Factura

id_factura  
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
crear_factura(self, id_factura, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf) -> Factura  
Constructor!!!  
get_id_factura() -> id_factura  
set_id_factura(id_factura) -> id_factura  
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

---

## Evento

id_evento  
nombre  
tipo  
lugar  
fecha_comienzo  
fecha_final  
poblacion  
tematica

Métodos:
crear_evento(self, id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica) -> Evento  
Constructor!!!  
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

---

## Documento

id_documento  
titulo  
descripcion  
fecha_subida  
tipo  
tematica

Métodos:
crear_documento(self, id_documento, titulo, descripcion, fecha_subida, tipo, tematica) -> Documento  
Constructor!!!  
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

---

## Cliente

id_cliente  
id_persona  
tipo  
razon_social  
nif  
fecha_registro  
(nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais heredados de Persona)

Métodos:
crear_cliente(self, id_cliente, id_persona, tipo, razon_social, nif, fecha_registro, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais) -> Cliente  
Constructor!!!  
get_id_cliente() -> id_cliente  
set_id_cliente(id_cliente) -> id_cliente  
get_tipo() -> tipo  
set_tipo(tipo) -> tipo  
get_nombre() -> nombre  
set_nombre(nombre) -> nombre  
get_apellido() -> apellido  
set_apellido(apellido) -> apellido  
get_razon_social() -> razon_social  
set_razon_social(razon_social) -> razon_social  
get_nif() -> nif  
set_nif(nif) -> nif  
get_dni() -> dni  
set_dni(dni) -> dni  
get_email() -> email  
set_email(email) -> email  
get_telefono() -> telefono  
set_telefono(telefono) -> telefono  
get_direccion() -> direccion  
set_direccion(direccion) -> direccion  
get_cp() -> cp  
set_cp(cp) -> cp  
get_poblacion() -> poblacion  
set_poblacion(poblacion) -> poblacion  
get_pais() -> pais  
set_pais(pais) -> pais  
get_fecha_registro() -> fecha_registro  
set_fecha_registro(fecha_registro) -> fecha_registro  

---

## AuditoriaPublicacion

id_auditoria_publicacion  
publicacion_id  
generador_ia_id  
fecha_generacion  
usuario_id  
parametros_entrada  
resultado  
observaciones

Métodos:
crear_auditoria_publicacion(self, id_auditoria_publicacion, publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones) -> AuditoriaPublicacion  
Constructor!!!  
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

---

## Actividad

id_actividad  
tipo  
nombre  
fecha_ejecucion  
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
crear_actividad(self, id_actividad, tipo, nombre, fecha_ejecucion, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones) -> Actividad  
Constructor!!!  
get_id_actividad() -> id_actividad  
set_id_actividad(id_actividad) -> id_actividad  
get_tipo() -> tipo  
set_tipo(tipo) -> tipo  
get_nombre() -> nombre  
set_nombre(nombre) -> nombre  
get_fecha_ejecucion() -> fecha_ejecucion  
set_fecha_ejecucion(fecha_ejecucion) -> fecha_ejecucion  
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

---
---
