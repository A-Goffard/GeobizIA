from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, validar_longitud_campo

def validar_datos_generadoria(datos):
    """
    Valida los datos de una generadoría.
    
    Args:
        datos (dict): Diccionario con los datos de la generadoría
        
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
    campos_obligatorios = ['nombre', 'tipo_energia']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar nombre
    if not validar_longitud_campo(datos_sanitizados['nombre'], min_length=3, max_length=100):
        return False, "El nombre debe tener entre 3 y 100 caracteres"
    
    # Validar tipo de energía
    tipos_validos = ['SOLAR', 'EOLICA', 'HIDRAULICA', 'GEOTERMICA', 'BIOMASA', 'NUCLEAR', 'CARBON', 'GAS', 'OTRO']
    if datos_sanitizados['tipo_energia'].upper() not in tipos_validos:
        return False, f"Tipo de energía inválido. Tipos válidos: {', '.join(tipos_validos)}"
    
    # Validar capacidad (opcional)
    if 'capacidad_mw' in datos_sanitizados and datos_sanitizados['capacidad_mw']:
        capacidad_sanitizada = sanitizar_numero(datos_sanitizados['capacidad_mw'])
        if capacidad_sanitizada is None or capacidad_sanitizada <= 0:
            return False, "La capacidad debe ser un número positivo"
    
    # Validar ubicación (opcional)
    if 'ubicacion' in datos_sanitizados and datos_sanitizados['ubicacion']:
        if not validar_longitud_campo(datos_sanitizados['ubicacion'], max_length=200):
            return False, "La ubicación no puede exceder los 200 caracteres"
    
    return True, "Validación exitosa"
