from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_email, sanitizar_telefono, validar_longitud_campo
import re
from datetime import datetime

def validar_datos_persona(datos):
    """
    Valida los datos de una persona.
    
    Args:
        datos (dict): Diccionario con los datos de la persona
        
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
    campos_obligatorios = ['nombre', 'apellido']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar nombre
    if not validar_longitud_campo(datos_sanitizados['nombre'], min_length=1, max_length=100):
        return False, "El nombre debe tener entre 1 y 100 caracteres"
    
    # Validar que el nombre solo contenga letras, espacios y algunos caracteres especiales
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\'-]+$', datos_sanitizados['nombre']):
        return False, "El nombre solo puede contener letras, espacios, apostrofes y guiones"
    
    # Validar apellido
    if not validar_longitud_campo(datos_sanitizados['apellido'], min_length=1, max_length=100):
        return False, "El apellido debe tener entre 1 y 100 caracteres"
    
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\'-]+$', datos_sanitizados['apellido']):
        return False, "El apellido solo puede contener letras, espacios, apostrofes y guiones"
    
    # Validar email (opcional)
    if 'email' in datos_sanitizados and datos_sanitizados['email']:
        email_sanitizado = sanitizar_email(datos_sanitizados['email'])
        if not email_sanitizado:
            return False, "El email no es válido"
        datos_sanitizados['email'] = email_sanitizado
    
    # Validar teléfono (opcional)
    if 'telefono' in datos_sanitizados and datos_sanitizados['telefono']:
        telefono_sanitizado = sanitizar_telefono(datos_sanitizados['telefono'])
        if not telefono_sanitizado:
            return False, "El teléfono no es válido"
        datos_sanitizados['telefono'] = telefono_sanitizado
    
    # Validar fecha de nacimiento (opcional)
    if 'fecha_nacimiento' in datos_sanitizados and datos_sanitizados['fecha_nacimiento']:
        try:
            fecha_nac = datetime.strptime(datos_sanitizados['fecha_nacimiento'], '%Y-%m-%d')
            if fecha_nac > datetime.now():
                return False, "La fecha de nacimiento no puede ser futura"
            if fecha_nac.year < 1900:
                return False, "La fecha de nacimiento no puede ser anterior a 1900"
        except ValueError:
            return False, "La fecha de nacimiento debe tener formato YYYY-MM-DD"
    
    # Validar documento de identidad (opcional)
    if 'documento_identidad' in datos_sanitizados and datos_sanitizados['documento_identidad']:
        if not validar_longitud_campo(datos_sanitizados['documento_identidad'], min_length=5, max_length=20):
            return False, "El documento de identidad debe tener entre 5 y 20 caracteres"
        if not re.match(r'^[0-9A-Z-]+$', datos_sanitizados['documento_identidad']):
            return False, "El documento de identidad solo puede contener números, letras mayúsculas y guiones"
    
    # Validar tipo de documento (opcional)
    if 'tipo_documento' in datos_sanitizados and datos_sanitizados['tipo_documento']:
        tipos_validos = ['DNI', 'NIE', 'PASAPORTE', 'CEDULA', 'CI', 'RUT', 'CURP']
        if datos_sanitizados['tipo_documento'].upper() not in tipos_validos:
            return False, f"Tipo de documento inválido. Tipos válidos: {', '.join(tipos_validos)}"
    
    # Validar dirección (opcional)
    if 'direccion' in datos_sanitizados and datos_sanitizados['direccion']:
        if not validar_longitud_campo(datos_sanitizados['direccion'], max_length=200):
            return False, "La dirección no puede exceder los 200 caracteres"
    
    # Validar código postal (opcional)
    if 'codigo_postal' in datos_sanitizados and datos_sanitizados['codigo_postal']:
        if not validar_longitud_campo(datos_sanitizados['codigo_postal'], min_length=3, max_length=10):
            return False, "El código postal debe tener entre 3 y 10 caracteres"
        if not re.match(r'^[0-9A-Z-]+$', datos_sanitizados['codigo_postal']):
            return False, "El código postal solo puede contener números, letras mayúsculas y guiones"
    
    # Validar país (opcional)
    if 'pais' in datos_sanitizados and datos_sanitizados['pais']:
        if not validar_longitud_campo(datos_sanitizados['pais'], min_length=2, max_length=50):
            return False, "El país debe tener entre 2 y 50 caracteres"
    
    # Validar estado civil (opcional)
    if 'estado_civil' in datos_sanitizados and datos_sanitizados['estado_civil']:
        estados_validos = ['SOLTERO', 'CASADO', 'DIVORCIADO', 'VIUDO', 'UNION_LIBRE']
        if datos_sanitizados['estado_civil'].upper() not in estados_validos:
            return False, f"Estado civil inválido. Estados válidos: {', '.join(estados_validos)}"
    
    return True, "Validación exitosa"
