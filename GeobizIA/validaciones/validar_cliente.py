import re
from .sanitizacion import sanitizar_entrada, sanitizar_email, sanitizar_telefono, validar_longitud_campo


def validar_datos_cliente(datos):
    """
    Valida los datos de un cliente.
    
    Campos esperados:
    - razon_social (obligatorio): Nombre o razón social del cliente
    - nif (obligatorio): NIF/CIF del cliente
    - direccion (opcional): Dirección del cliente
    - telefono (opcional): Teléfono de contacto
    - email (opcional): Email de contacto
    - persona_contacto (opcional): Nombre de la persona de contacto
    """
    
    # 1. Campos obligatorios
    campos_obligatorios = ['razon_social', 'nif']
    for campo in campos_obligatorios:
        if campo not in datos or not datos[campo]:
            return False, f"El campo '{campo}' es obligatorio y no puede estar vacío."
    
    # 2. Sanitizar campos de texto
    campos_texto = ['razon_social', 'nif', 'direccion', 'persona_contacto']
    for campo in campos_texto:
        if campo in datos and datos[campo] is not None:
            datos[campo] = sanitizar_entrada(datos[campo])
    
    # 3. Sanitización específica para email y teléfono
    if 'email' in datos and datos['email']:
        datos['email'] = sanitizar_email(datos['email'])
    
    if 'telefono' in datos and datos['telefono']:
        datos['telefono'] = sanitizar_telefono(datos['telefono'])
    
    # 4. Validaciones específicas
    
    # Razón social
    valido, mensaje = validar_longitud_campo(datos['razon_social'], 2, 100)
    if not valido:
        return False, f"Razón social: {mensaje}"
    
    if not re.match(r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ\-\.\,\&]{2,100}$", datos['razon_social']):
        return False, "La razón social contiene caracteres no permitidos."
    
    # NIF/CIF
    valido, mensaje = validar_longitud_campo(datos['nif'], 8, 15)
    if not valido:
        return False, f"NIF/CIF: {mensaje}"
    
    if not re.match(r"^[A-Z0-9]{8,15}$", datos['nif'].upper()):
        return False, "El NIF/CIF debe contener solo letras y números (8-15 caracteres)."
    
    # Email (si se proporciona)
    if 'email' in datos and datos['email']:
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", datos['email']):
            return False, "El formato del email no es válido."
    
    # Teléfono (si se proporciona)
    if 'telefono' in datos and datos['telefono']:
        valido, mensaje = validar_longitud_campo(datos['telefono'], 9, 15)
        if not valido:
            return False, f"Teléfono: {mensaje}"
    
    # Dirección (si se proporciona)
    if 'direccion' in datos and datos['direccion']:
        valido, mensaje = validar_longitud_campo(datos['direccion'], 5, 255)
        if not valido:
            return False, f"Dirección: {mensaje}"
    
    # Persona de contacto (si se proporciona)
    if 'persona_contacto' in datos and datos['persona_contacto']:
        valido, mensaje = validar_longitud_campo(datos['persona_contacto'], 2, 100)
        if not valido:
            return False, f"Persona de contacto: {mensaje}"
        
        if not re.match(r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ\-\.]{2,100}$", datos['persona_contacto']):
            return False, "La persona de contacto contiene caracteres no permitidos."
    
    # 5. Validar id_cliente si viene (para actualizaciones)
    if "id_cliente" in datos and datos["id_cliente"] is not None:
        if not isinstance(datos["id_cliente"], int) or datos["id_cliente"] <= 0:
            return False, "El id_cliente debe ser un número entero positivo."
    
    return True, ""
