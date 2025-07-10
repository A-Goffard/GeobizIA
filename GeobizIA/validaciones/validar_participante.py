from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, sanitizar_email, validar_longitud_campo
import re
from datetime import datetime

def validar_datos_participante(datos):
    """
    Valida los datos de un participante.
    
    Args:
        datos (dict): Diccionario con los datos del participante
        
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
    campos_obligatorios = ['persona_id', 'evento_id', 'rol']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar persona_id
    persona_id_sanitizado = sanitizar_numero(datos_sanitizados['persona_id'])
    if persona_id_sanitizado is None or persona_id_sanitizado <= 0:
        return False, "El ID de la persona debe ser un número entero positivo"
    
    # Validar evento_id
    evento_id_sanitizado = sanitizar_numero(datos_sanitizados['evento_id'])
    if evento_id_sanitizado is None or evento_id_sanitizado <= 0:
        return False, "El ID del evento debe ser un número entero positivo"
    
    # Validar rol del participante
    if not validar_longitud_campo(datos_sanitizados['rol'], min_length=1, max_length=50):
        return False, "El rol debe tener entre 1 y 50 caracteres"
    
    roles_validos = ['ORGANIZADOR', 'PONENTE', 'MODERADOR', 'ASISTENTE', 'VOLUNTARIO', 'SPONSOR', 'INVITADO_ESPECIAL', 'STAFF']
    if datos_sanitizados['rol'].upper() not in roles_validos:
        return False, f"Rol inválido. Roles válidos: {', '.join(roles_validos)}"
    
    # Validar estado de participación (opcional)
    if 'estado' in datos_sanitizados and datos_sanitizados['estado']:
        estados_validos = ['CONFIRMADO', 'PENDIENTE', 'CANCELADO', 'NO_ASISTIO', 'ASISTIO']
        if datos_sanitizados['estado'].upper() not in estados_validos:
            return False, f"Estado inválido. Estados válidos: {', '.join(estados_validos)}"
    
    # Validar fecha de inscripción (opcional)
    if 'fecha_inscripcion' in datos_sanitizados and datos_sanitizados['fecha_inscripcion']:
        try:
            fecha_inscripcion = datetime.strptime(datos_sanitizados['fecha_inscripcion'], '%Y-%m-%d %H:%M:%S')
            if fecha_inscripcion > datetime.now():
                return False, "La fecha de inscripción no puede ser futura"
        except ValueError:
            try:
                # Intentar formato solo fecha
                fecha_inscripcion = datetime.strptime(datos_sanitizados['fecha_inscripcion'], '%Y-%m-%d')
                if fecha_inscripcion.date() > datetime.now().date():
                    return False, "La fecha de inscripción no puede ser futura"
            except ValueError:
                return False, "La fecha de inscripción debe tener formato YYYY-MM-DD o YYYY-MM-DD HH:MM:SS"
    
    # Validar notas especiales (opcional)
    if 'notas_especiales' in datos_sanitizados and datos_sanitizados['notas_especiales']:
        if not validar_longitud_campo(datos_sanitizados['notas_especiales'], max_length=500):
            return False, "Las notas especiales no pueden exceder los 500 caracteres"
    
    # Validar requerimientos dietarios (opcional)
    if 'requerimientos_dietarios' in datos_sanitizados and datos_sanitizados['requerimientos_dietarios']:
        if not validar_longitud_campo(datos_sanitizados['requerimientos_dietarios'], max_length=200):
            return False, "Los requerimientos dietarios no pueden exceder los 200 caracteres"
    
    # Validar necesidades especiales (opcional)
    if 'necesidades_especiales' in datos_sanitizados and datos_sanitizados['necesidades_especiales']:
        if not validar_longitud_campo(datos_sanitizados['necesidades_especiales'], max_length=200):
            return False, "Las necesidades especiales no pueden exceder los 200 caracteres"
    
    # Validar email de contacto (opcional)
    if 'email_contacto' in datos_sanitizados and datos_sanitizados['email_contacto']:
        email_sanitizado = sanitizar_email(datos_sanitizados['email_contacto'])
        if not email_sanitizado:
            return False, "El email de contacto no es válido"
        datos_sanitizados['email_contacto'] = email_sanitizado
    
    # Validar calificación/rating (opcional)
    if 'calificacion' in datos_sanitizados and datos_sanitizados['calificacion']:
        calificacion_sanitizada = sanitizar_numero(datos_sanitizados['calificacion'])
        if calificacion_sanitizada is None:
            return False, "La calificación debe ser un número válido"
        if calificacion_sanitizada < 1 or calificacion_sanitizada > 5:
            return False, "La calificación debe estar entre 1 y 5"
    
    # Validar certificado emitido (opcional, boolean)
    if 'certificado_emitido' in datos_sanitizados and datos_sanitizados['certificado_emitido']:
        if datos_sanitizados['certificado_emitido'].lower() not in ['true', 'false', '1', '0', 'si', 'no']:
            return False, "El campo certificado_emitido debe ser un valor booleano válido"
    
    # Validar costo de participación (opcional)
    if 'costo_participacion' in datos_sanitizados and datos_sanitizados['costo_participacion']:
        costo_sanitizado = sanitizar_numero(datos_sanitizados['costo_participacion'])
        if costo_sanitizado is None:
            return False, "El costo de participación debe ser un número válido"
        if costo_sanitizado < 0:
            return False, "El costo de participación no puede ser negativo"
    
    return True, "Validación exitosa"
