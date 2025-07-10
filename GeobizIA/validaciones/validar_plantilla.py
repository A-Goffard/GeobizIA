from .sanitizacion import sanitizar_entrada, sanitizar_dict, validar_longitud_campo

def validar_datos_plantilla(datos):
    """
    Valida los datos de una plantilla.
    
    Args:
        datos (dict): Diccionario con los datos de la plantilla
        
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
    campos_obligatorios = ['nombre', 'contenido', 'tipo']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar nombre de la plantilla
    if not validar_longitud_campo(datos_sanitizados['nombre'], min_length=3, max_length=100):
        return False, "El nombre debe tener entre 3 y 100 caracteres"
    
    # Validar contenido
    if not validar_longitud_campo(datos_sanitizados['contenido'], min_length=10, max_length=5000):
        return False, "El contenido debe tener entre 10 y 5000 caracteres"
    
    # Validar tipo de plantilla
    tipos_validos = ['EMAIL', 'SMS', 'DOCUMENTO', 'REPORTE', 'NOTIFICACION', 'PUBLICACION']
    if datos_sanitizados['tipo'].upper() not in tipos_validos:
        return False, f"Tipo inválido. Tipos válidos: {', '.join(tipos_validos)}"
    
    # Validar descripción (opcional)
    if 'descripcion' in datos_sanitizados and datos_sanitizados['descripcion']:
        if not validar_longitud_campo(datos_sanitizados['descripcion'], max_length=300):
            return False, "La descripción no puede exceder los 300 caracteres"
    
    # Validar variables de plantilla (opcional)
    if 'variables' in datos_sanitizados and datos_sanitizados['variables']:
        if isinstance(datos_sanitizados['variables'], list):
            for variable in datos_sanitizados['variables']:
                if not isinstance(variable, str) or len(variable) > 50:
                    return False, "Cada variable debe ser una cadena de máximo 50 caracteres"
        else:
            return False, "Las variables deben ser una lista"
    
    return True, "Validación exitosa"
