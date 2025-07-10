from .sanitizacion import sanitizar_entrada, sanitizar_dict, validar_longitud_campo

def validar_datos_tipo_publicacion(datos):
    """
    Valida los datos de un tipo de publicación.
    
    Args:
        datos (dict): Diccionario con los datos del tipo de publicación
        
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
    campos_obligatorios = ['nombre', 'descripcion']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar nombre del tipo
    if not validar_longitud_campo(datos_sanitizados['nombre'], min_length=2, max_length=50):
        return False, "El nombre debe tener entre 2 y 50 caracteres"
    
    # Validar descripción
    if not validar_longitud_campo(datos_sanitizados['descripcion'], min_length=5, max_length=200):
        return False, "La descripción debe tener entre 5 y 200 caracteres"
    
    # Validar formato permitido (opcional)
    if 'formato' in datos_sanitizados and datos_sanitizados['formato']:
        formatos_validos = ['TEXTO', 'IMAGEN', 'VIDEO', 'AUDIO', 'DOCUMENTO', 'LINK', 'MIXTO']
        if datos_sanitizados['formato'].upper() not in formatos_validos:
            return False, f"Formato inválido. Formatos válidos: {', '.join(formatos_validos)}"
    
    # Validar categoría (opcional)
    if 'categoria' in datos_sanitizados and datos_sanitizados['categoria']:
        categorias_validas = ['INFORMATIVA', 'EDUCATIVA', 'PROMOCIONAL', 'ENTRETENIMIENTO', 'NOTICIAS', 'OPINION', 'TUTORIAL']
        if datos_sanitizados['categoria'].upper() not in categorias_validas:
            return False, f"Categoría inválida. Categorías válidas: {', '.join(categorias_validas)}"
    
    return True, "Validación exitosa"
