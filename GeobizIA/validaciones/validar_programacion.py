from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, validar_longitud_campo
from datetime import datetime

def validar_datos_programacion(datos):
    """
    Valida los datos de una programación.
    
    Args:
        datos (dict): Diccionario con los datos de la programación
        
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
    campos_obligatorios = ['fecha_inicio', 'fecha_fin', 'actividad_id']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar fecha_inicio
    try:
        fecha_inicio = datetime.strptime(datos_sanitizados['fecha_inicio'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return False, "La fecha de inicio debe tener formato YYYY-MM-DD HH:MM:SS"
    
    # Validar fecha_fin
    try:
        fecha_fin = datetime.strptime(datos_sanitizados['fecha_fin'], '%Y-%m-%d %H:%M:%S')
        if fecha_fin <= fecha_inicio:
            return False, "La fecha de fin debe ser posterior a la fecha de inicio"
    except ValueError:
        return False, "La fecha de fin debe tener formato YYYY-MM-DD HH:MM:SS"
    
    # Validar actividad_id
    actividad_id_sanitizado = sanitizar_numero(datos_sanitizados['actividad_id'])
    if actividad_id_sanitizado is None or actividad_id_sanitizado <= 0:
        return False, "El ID de la actividad debe ser un número entero positivo"
    
    # Validar estado (opcional)
    if 'estado' in datos_sanitizados and datos_sanitizados['estado']:
        estados_validos = ['PROGRAMADO', 'EN_PROGRESO', 'COMPLETADO', 'CANCELADO', 'SUSPENDIDO']
        if datos_sanitizados['estado'].upper() not in estados_validos:
            return False, f"Estado inválido. Estados válidos: {', '.join(estados_validos)}"
    
    # Validar prioridad (opcional)
    if 'prioridad' in datos_sanitizados and datos_sanitizados['prioridad']:
        prioridades_validas = ['BAJA', 'MEDIA', 'ALTA', 'CRITICA']
        if datos_sanitizados['prioridad'].upper() not in prioridades_validas:
            return False, f"Prioridad inválida. Prioridades válidas: {', '.join(prioridades_validas)}"
    
    # Validar notas (opcional)
    if 'notas' in datos_sanitizados and datos_sanitizados['notas']:
        if not validar_longitud_campo(datos_sanitizados['notas'], max_length=500):
            return False, "Las notas no pueden exceder los 500 caracteres"
    
    return True, "Validación exitosa"
