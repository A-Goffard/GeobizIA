from .sanitizacion import sanitizar_entrada, sanitizar_dict, validar_longitud_campo

def validar_datos_redsocial(datos):
    """
    Valida los datos de una red social.
    
    Args:
        datos (dict): Diccionario con los datos de la red social
        
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
    campos_obligatorios = ['nombre', 'plataforma']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar nombre
    if not validar_longitud_campo(datos_sanitizados['nombre'], min_length=1, max_length=100):
        return False, "El nombre debe tener entre 1 y 100 caracteres"
    
    # Validar plataforma
    plataformas_validas = ['FACEBOOK', 'TWITTER', 'INSTAGRAM', 'LINKEDIN', 'YOUTUBE', 'TIKTOK', 'WHATSAPP', 'TELEGRAM', 'OTRA']
    if datos_sanitizados['plataforma'].upper() not in plataformas_validas:
        return False, f"Plataforma inválida. Plataformas válidas: {', '.join(plataformas_validas)}"
    
    # Validar descripción (opcional)
    if 'descripcion' in datos_sanitizados and datos_sanitizados['descripcion']:
        if not validar_longitud_campo(datos_sanitizados['descripcion'], max_length=300):
            return False, "La descripción no puede exceder los 300 caracteres"
    
    return True, "Validación exitosa"
