from .sanitizacion import sanitizar_entrada, sanitizar_dict, validar_longitud_campo

def validar_datos_rol(datos):
    """
    Valida los datos de un rol.
    
    Args:
        datos (dict): Diccionario con los datos del rol
        
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
    campos_obligatorios = ['nombre']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar nombre del rol
    if not validar_longitud_campo(datos_sanitizados['nombre'], min_length=2, max_length=50):
        return False, "El nombre del rol debe tener entre 2 y 50 caracteres"
    
    # Validar descripción (opcional)
    if 'descripcion' in datos_sanitizados and datos_sanitizados['descripcion']:
        if not validar_longitud_campo(datos_sanitizados['descripcion'], max_length=200):
            return False, "La descripción no puede exceder los 200 caracteres"
    
    # Validar nivel de acceso (opcional)
    if 'nivel_acceso' in datos_sanitizados and datos_sanitizados['nivel_acceso']:
        niveles_validos = ['BASICO', 'INTERMEDIO', 'AVANZADO', 'ADMIN', 'SUPER_ADMIN']
        if datos_sanitizados['nivel_acceso'].upper() not in niveles_validos:
            return False, f"Nivel de acceso inválido. Niveles válidos: {', '.join(niveles_validos)}"
    
    # Validar estado (opcional)
    if 'activo' in datos_sanitizados and datos_sanitizados['activo']:
        if datos_sanitizados['activo'].lower() not in ['true', 'false', '1', '0', 'si', 'no']:
            return False, "El campo activo debe ser un valor booleano válido"
    
    return True, "Validación exitosa"
