from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, validar_longitud_campo
import re
from datetime import datetime

def validar_datos_publicacion(datos):
    """
    Valida los datos de una publicación.
    
    Args:
        datos (dict): Diccionario con los datos de la publicación
        
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
    campos_obligatorios = ['titulo', 'contenido', 'tipo_publicacion_id']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar título
    if not validar_longitud_campo(datos_sanitizados['titulo'], min_length=3, max_length=200):
        return False, "El título debe tener entre 3 y 200 caracteres"
    
    # Validar contenido
    if not validar_longitud_campo(datos_sanitizados['contenido'], min_length=10, max_length=5000):
        return False, "El contenido debe tener entre 10 y 5000 caracteres"
    
    # Validar tipo_publicacion_id
    tipo_id_sanitizado = sanitizar_numero(datos_sanitizados['tipo_publicacion_id'])
    if tipo_id_sanitizado is None or tipo_id_sanitizado <= 0:
        return False, "El ID del tipo de publicación debe ser un número entero positivo"
    
    # Validar estado (opcional)
    if 'estado' in datos_sanitizados and datos_sanitizados['estado']:
        estados_validos = ['BORRADOR', 'PROGRAMADA', 'PUBLICADA', 'ARCHIVADA', 'ELIMINADA']
        if datos_sanitizados['estado'].upper() not in estados_validos:
            return False, f"Estado inválido. Estados válidos: {', '.join(estados_validos)}"
    
    # Validar fecha de publicación (opcional)
    if 'fecha_publicacion' in datos_sanitizados and datos_sanitizados['fecha_publicacion']:
        try:
            datetime.strptime(datos_sanitizados['fecha_publicacion'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                datetime.strptime(datos_sanitizados['fecha_publicacion'], '%Y-%m-%d')
            except ValueError:
                return False, "La fecha de publicación debe tener formato YYYY-MM-DD o YYYY-MM-DD HH:MM:SS"
    
    # Validar hashtags (opcional)
    if 'hashtags' in datos_sanitizados and datos_sanitizados['hashtags']:
        if isinstance(datos_sanitizados['hashtags'], list):
            for hashtag in datos_sanitizados['hashtags']:
                if not isinstance(hashtag, str) or len(hashtag) > 50:
                    return False, "Cada hashtag debe ser una cadena de máximo 50 caracteres"
                if not re.match(r'^#[a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ]+$', hashtag):
                    return False, "Los hashtags deben comenzar con # y contener solo letras, números y guiones bajos"
        elif isinstance(datos_sanitizados['hashtags'], str):
            # Si es string, dividir por espacios o comas
            hashtags_list = re.split(r'[,\s]+', datos_sanitizados['hashtags'])
            for hashtag in hashtags_list:
                if hashtag and not re.match(r'^#[a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ]+$', hashtag.strip()):
                    return False, "Los hashtags deben comenzar con # y contener solo letras, números y guiones bajos"
        else:
            return False, "Los hashtags deben ser una lista o una cadena"
    
    # Validar URL de imagen (opcional)
    if 'imagen_url' in datos_sanitizados and datos_sanitizados['imagen_url']:
        url_pattern = re.compile(
            r'^https?://'  # http:// o https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # dominio
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
            r'(?::\d+)?'  # puerto opcional
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if not url_pattern.match(datos_sanitizados['imagen_url']):
            return False, "La URL de la imagen no es válida"
    
    # Validar prioridad (opcional)
    if 'prioridad' in datos_sanitizados and datos_sanitizados['prioridad']:
        prioridad_sanitizada = sanitizar_numero(datos_sanitizados['prioridad'])
        if prioridad_sanitizada is None or prioridad_sanitizada < 1 or prioridad_sanitizada > 10:
            return False, "La prioridad debe ser un número entre 1 y 10"
    
    # Validar audiencia objetivo (opcional)
    if 'audiencia_objetivo' in datos_sanitizados and datos_sanitizados['audiencia_objetivo']:
        audiencias_validas = ['GENERAL', 'EMPRESAS', 'ESTUDIANTES', 'PROFESIONALES', 'JOVENES', 'ADULTOS', 'ESPECIALISTAS']
        if datos_sanitizados['audiencia_objetivo'].upper() not in audiencias_validas:
            return False, f"Audiencia objetivo inválida. Audiencias válidas: {', '.join(audiencias_validas)}"
    
    return True, "Validación exitosa"
