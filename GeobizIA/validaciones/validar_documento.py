from .sanitizacion import sanitizar_entrada, sanitizar_dict, validar_longitud_campo
import re
from datetime import datetime

def validar_datos_documento(datos):
    """
    Valida los datos de un documento.
    
    Args:
        datos (dict): Diccionario con los datos del documento
        
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
    campos_obligatorios = ['titulo', 'tipo_documento', 'contenido']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar título
    if not validar_longitud_campo(datos_sanitizados['titulo'], min_length=1, max_length=200):
        return False, "El título debe tener entre 1 y 200 caracteres"
    
    # Validar tipo de documento
    tipos_validos = ['PDF', 'DOC', 'DOCX', 'TXT', 'XLS', 'XLSX', 'PPT', 'PPTX', 'IMG', 'VIDEO', 'AUDIO']
    if datos_sanitizados['tipo_documento'].upper() not in tipos_validos:
        return False, f"Tipo de documento inválido. Tipos válidos: {', '.join(tipos_validos)}"
    
    # Validar contenido
    if not validar_longitud_campo(datos_sanitizados['contenido'], min_length=1, max_length=10000):
        return False, "El contenido debe tener entre 1 y 10000 caracteres"
    
    # Validar descripción (opcional)
    if 'descripcion' in datos_sanitizados and datos_sanitizados['descripcion']:
        if not validar_longitud_campo(datos_sanitizados['descripcion'], max_length=500):
            return False, "La descripción no puede exceder los 500 caracteres"
    
    # Validar URL del archivo (opcional)
    if 'url_archivo' in datos_sanitizados and datos_sanitizados['url_archivo']:
        url_pattern = re.compile(
            r'^https?://'  # http:// o https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # dominio
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
            r'(?::\d+)?'  # puerto opcional
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if not url_pattern.match(datos_sanitizados['url_archivo']):
            return False, "La URL del archivo no es válida"
    
    # Validar tamaño del archivo (opcional)
    if 'tamaño_archivo' in datos_sanitizados and datos_sanitizados['tamaño_archivo']:
        try:
            tamaño = int(datos_sanitizados['tamaño_archivo'])
            if tamaño < 0 or tamaño > 100000000:  # 100MB máximo
                return False, "El tamaño del archivo debe estar entre 0 y 100MB"
        except ValueError:
            return False, "El tamaño del archivo debe ser un número válido"
    
    # Validar fecha de creación (opcional)
    if 'fecha_creacion' in datos_sanitizados and datos_sanitizados['fecha_creacion']:
        try:
            datetime.strptime(datos_sanitizados['fecha_creacion'], '%Y-%m-%d')
        except ValueError:
            return False, "La fecha de creación debe tener formato YYYY-MM-DD"
    
    # Validar tags (opcional)
    if 'tags' in datos_sanitizados and datos_sanitizados['tags']:
        if isinstance(datos_sanitizados['tags'], list):
            for tag in datos_sanitizados['tags']:
                if not isinstance(tag, str) or len(tag) > 50:
                    return False, "Cada tag debe ser una cadena de máximo 50 caracteres"
        else:
            return False, "Los tags deben ser una lista"
    
    return True, "Validación exitosa"
