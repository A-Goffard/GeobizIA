from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, validar_longitud_campo
from datetime import datetime

def validar_datos_log_sistema(datos):
    """
    Valida los datos de un log del sistema.
    
    Args:
        datos (dict): Diccionario con los datos del log
        
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
    campos_obligatorios = ['accion', 'fecha_hora']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar acción
    if not validar_longitud_campo(datos_sanitizados['accion'], min_length=1, max_length=100):
        return False, "La acción debe tener entre 1 y 100 caracteres"
    
    # Validar fecha y hora
    try:
        datetime.strptime(datos_sanitizados['fecha_hora'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return False, "La fecha y hora debe tener formato YYYY-MM-DD HH:MM:SS"
    
    # Validar nivel del log (opcional)
    if 'nivel' in datos_sanitizados and datos_sanitizados['nivel']:
        niveles_validos = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if datos_sanitizados['nivel'].upper() not in niveles_validos:
            return False, f"Nivel inválido. Niveles válidos: {', '.join(niveles_validos)}"
    
    # Validar usuario_id (opcional)
    if 'usuario_id' in datos_sanitizados and datos_sanitizados['usuario_id']:
        usuario_id_sanitizado = sanitizar_numero(datos_sanitizados['usuario_id'])
        if usuario_id_sanitizado is None or usuario_id_sanitizado <= 0:
            return False, "El ID del usuario debe ser un número entero positivo"
    
    # Validar descripción (opcional)
    if 'descripcion' in datos_sanitizados and datos_sanitizados['descripcion']:
        if not validar_longitud_campo(datos_sanitizados['descripcion'], max_length=500):
            return False, "La descripción no puede exceder los 500 caracteres"
    
    return True, "Validación exitosa"
