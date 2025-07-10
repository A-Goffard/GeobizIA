import re
from .sanitizacion import sanitizar_entrada, sanitizar_email, sanitizar_telefono, validar_longitud_campo


def validar_datos_empresa(datos):
    """
    Valida los datos de una empresa.
    
    Campos esperados:
    - nombre (obligatorio): Nombre de la empresa
    - sector (obligatorio): Sector de actividad
    - logo (opcional): URL del logo de la empresa
    - ubicacion (obligatorio): Ubicación de la empresa
    """
    
    # 1. Campos obligatorios
    campos_obligatorios = ['nombre', 'sector', 'ubicacion']
    for campo in campos_obligatorios:
        if campo not in datos or not datos[campo]:
            return False, f"El campo '{campo}' es obligatorio y no puede estar vacío."
    
    # 2. Sanitizar campos de texto
    campos_texto = ['nombre', 'sector', 'logo', 'ubicacion']
    for campo in campos_texto:
        if campo in datos and datos[campo] is not None:
            datos[campo] = sanitizar_entrada(datos[campo])
    
    # 3. Validaciones específicas
    
    # Nombre de la empresa
    valido, mensaje = validar_longitud_campo(datos['nombre'], 2, 100)
    if not valido:
        return False, f"Nombre de empresa: {mensaje}"
    
    if not re.match(r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ\-\.\,\&]{2,100}$", datos['nombre']):
        return False, "El nombre de la empresa contiene caracteres no permitidos."
    
    # Sector
    valido, mensaje = validar_longitud_campo(datos['sector'], 2, 100)
    if not valido:
        return False, f"Sector: {mensaje}"
    
    if not re.match(r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ\-\.\,\&]{2,100}$", datos['sector']):
        return False, "El sector contiene caracteres no permitidos."
    
    # Ubicación
    valido, mensaje = validar_longitud_campo(datos['ubicacion'], 2, 200)
    if not valido:
        return False, f"Ubicación: {mensaje}"
    
    if not re.match(r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ\-\.\,\&]{2,200}$", datos['ubicacion']):
        return False, "La ubicación contiene caracteres no permitidos."
    
    # Logo (opcional)
    if 'logo' in datos and datos['logo']:
        valido, mensaje = validar_longitud_campo(datos['logo'], 5, 500)
        if not valido:
            return False, f"Logo URL: {mensaje}"
        
        # Validar que sea una URL válida
        url_pattern = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
        if not re.match(url_pattern, datos['logo']):
            return False, "El logo debe ser una URL válida."
    
    return True, "Datos válidos"
