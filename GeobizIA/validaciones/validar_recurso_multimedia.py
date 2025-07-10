from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, validar_longitud_campo
import re

def validar_datos_recurso_multimedia(datos):
    """
    Valida los datos de un recurso multimedia.
    
    Args:
        datos (dict): Diccionario con los datos del recurso multimedia
        
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
    campos_obligatorios = ['nombre', 'tipo_recurso', 'url']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar nombre
    if not validar_longitud_campo(datos_sanitizados['nombre'], min_length=1, max_length=100):
        return False, "El nombre debe tener entre 1 y 100 caracteres"
    
    # Validar tipo de recurso
    tipos_validos = ['IMAGEN', 'VIDEO', 'AUDIO', 'DOCUMENTO', 'ANIMACION', 'PRESENTACION']
    if datos_sanitizados['tipo_recurso'].upper() not in tipos_validos:
        return False, f"Tipo de recurso inválido. Tipos válidos: {', '.join(tipos_validos)}"
    
    # Validar URL
    url_pattern = re.compile(
        r'^https?://'  # http:// o https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # dominio
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
        r'(?::\d+)?'  # puerto opcional
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if not url_pattern.match(datos_sanitizados['url']):
        return False, "La URL no es válida"
    
    # Validar tamaño del archivo (opcional)
    if 'tamaño_archivo' in datos_sanitizados and datos_sanitizados['tamaño_archivo']:
        tamaño_sanitizado = sanitizar_numero(datos_sanitizados['tamaño_archivo'])
        if tamaño_sanitizado is None or tamaño_sanitizado < 0:
            return False, "El tamaño del archivo debe ser un número positivo"
    
    # Validar descripción (opcional)
    if 'descripcion' in datos_sanitizados and datos_sanitizados['descripcion']:
        if not validar_longitud_campo(datos_sanitizados['descripcion'], max_length=500):
            return False, "La descripción no puede exceder los 500 caracteres"
    
    return True, "Validación exitosa"
