from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, validar_longitud_campo

def validar_datos_tipo_publicacion_redsocial(datos):
    """
    Valida los datos de la relación entre tipo de publicación y red social.
    
    Args:
        datos (dict): Diccionario con los datos de la relación
        
    Returns:
        tuple: (bool, str) - (es_valido, mensaje_error)
    """
    if not isinstance(datos, dict):
        return False, "Los datos deben ser un diccionario válido"
    
    # Sanitizar todos los datos de entrada
    try:
        datos_sanitizados = sanitizar_dict(datos)
    except Exception as e:
        return False, f"Error al sanitizar datos: {str(e)}"
    
    # Validar campos obligatorios
    campos_obligatorios = ['tipo_publicacion_id', 'redsocial_id']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar tipo_publicacion_id
    tipo_id_sanitizado = sanitizar_numero(datos_sanitizados['tipo_publicacion_id'])
    if tipo_id_sanitizado is None or tipo_id_sanitizado <= 0:
        return False, "El ID del tipo de publicación debe ser un número entero positivo"
    
    # Validar redsocial_id
    redsocial_id_sanitizado = sanitizar_numero(datos_sanitizados['redsocial_id'])
    if redsocial_id_sanitizado is None or redsocial_id_sanitizado <= 0:
        return False, "El ID de la red social debe ser un número entero positivo"
    
    # Validar configuración específica (opcional)
    if 'configuracion' in datos_sanitizados and datos_sanitizados['configuracion']:
        if not validar_longitud_campo(datos_sanitizados['configuracion'], max_length=1000):
            return False, "La configuración no puede exceder los 1000 caracteres"
    
    # Validar estado (opcional)
    if 'activo' in datos_sanitizados and datos_sanitizados['activo']:
        if datos_sanitizados['activo'].lower() not in ['true', 'false', '1', '0', 'si', 'no']:
            return False, "El campo activo debe ser un valor booleano válido"
    
    return True, "Validación exitosa"
