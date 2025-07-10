from .sanitizacion import sanitizar_entrada, sanitizar_dict, validar_longitud_campo
import re

def validar_datos_tag(datos):
    """
    Valida los datos de un tag.
    
    Args:
        datos (dict): Diccionario con los datos del tag
        
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
    campos_obligatorios = ['palabra_clave']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar palabra clave
    if not validar_longitud_campo(datos_sanitizados['palabra_clave'], min_length=1, max_length=50):
        return False, "La palabra clave debe tener entre 1 y 50 caracteres"
    
    # Validar formato de la palabra clave (sin espacios al principio/final, sin caracteres especiales problemáticos)
    if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s_-]+$', datos_sanitizados['palabra_clave']):
        return False, "La palabra clave solo puede contener letras, números, espacios, guiones y guiones bajos"
    
    # Validar descripción (opcional)
    if 'descripcion' in datos_sanitizados and datos_sanitizados['descripcion']:
        if not validar_longitud_campo(datos_sanitizados['descripcion'], max_length=200):
            return False, "La descripción no puede exceder los 200 caracteres"
    
    # Validar categoría (opcional)
    if 'categoria' in datos_sanitizados and datos_sanitizados['categoria']:
        categorias_validas = ['GENERAL', 'TECNICO', 'MARKETING', 'AMBIENTAL', 'SOCIAL', 'ECONOMICO', 'EDUCATIVO']
        if datos_sanitizados['categoria'].upper() not in categorias_validas:
            return False, f"Categoría inválida. Categorías válidas: {', '.join(categorias_validas)}"
    
    # Validar color asociado (opcional)
    if 'color' in datos_sanitizados and datos_sanitizados['color']:
        # Validar formato hexadecimal de color
        if not re.match(r'^#[0-9A-Fa-f]{6}$', datos_sanitizados['color']):
            return False, "El color debe estar en formato hexadecimal (#RRGGBB)"
    
    # Validar popularidad/uso (opcional)
    if 'uso_frecuente' in datos_sanitizados and datos_sanitizados['uso_frecuente']:
        if datos_sanitizados['uso_frecuente'].lower() not in ['true', 'false', '1', '0', 'si', 'no']:
            return False, "El campo uso_frecuente debe ser un valor booleano válido"
    
    return True, "Validación exitosa"
