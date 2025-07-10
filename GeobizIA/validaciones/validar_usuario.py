import re
from .sanitizacion import sanitizar_entrada, validar_longitud_campo


def validar_datos_usuario(datos):
    """
    Valida los datos de un usuario.
    
    Campos esperados:
    - id_persona (obligatorio): ID de la persona asociada
    - rol (obligatorio): Rol del usuario (Administrador, Usuario, Moderador)
    - password (obligatorio): Contraseña del usuario
    - activo (opcional): Si el usuario está activo (True/False)
    """
    
    # 1. Campos obligatorios
    campos_obligatorios = ['id_persona', 'rol', 'password']
    for campo in campos_obligatorios:
        if campo not in datos or datos[campo] in [None, ""]:
            return False, f"El campo '{campo}' es obligatorio y no puede estar vacío."
    
    # 2. Sanitizar campos de texto
    if 'rol' in datos and datos['rol']:
        datos['rol'] = sanitizar_entrada(datos['rol'])
    
    # 3. Validaciones específicas
    
    # Validar id_persona
    if not isinstance(datos['id_persona'], int) or datos['id_persona'] <= 0:
        return False, "El id_persona debe ser un número entero positivo."
    
    # Validar rol
    valido, mensaje = validar_longitud_campo(datos['rol'], 3, 20)
    if not valido:
        return False, f"Rol: {mensaje}"
    
    roles_permitidos = ['Administrador', 'Usuario', 'Moderador', 'Editor']
    if datos['rol'] not in roles_permitidos:
        return False, f"El rol debe ser uno de: {', '.join(roles_permitidos)}"
    
    # Validar contraseña
    if not isinstance(datos['password'], str):
        return False, "La contraseña debe ser una cadena de texto."
    
    if len(datos['password']) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres."
    
    if len(datos['password']) > 128:
        return False, "La contraseña no puede exceder los 128 caracteres."
    
    # Validación de complejidad de contraseña (opcional - ajustar según necesidades)
    if not re.search(r"[A-Za-z]", datos['password']):
        return False, "La contraseña debe contener al menos una letra."
    
    if not re.search(r"[0-9]", datos['password']):
        return False, "La contraseña debe contener al menos un número."
    
    # Validar campo activo (si se proporciona)
    if 'activo' in datos and datos['activo'] is not None:
        if not isinstance(datos['activo'], bool):
            # Intentar convertir strings comunes a boolean
            if isinstance(datos['activo'], str):
                if datos['activo'].lower() in ['true', '1', 'yes', 'si']:
                    datos['activo'] = True
                elif datos['activo'].lower() in ['false', '0', 'no']:
                    datos['activo'] = False
                else:
                    return False, "El campo 'activo' debe ser True o False."
            else:
                return False, "El campo 'activo' debe ser True o False."
    
    # 4. Validar id_usuario si viene (para actualizaciones)
    if "id_usuario" in datos and datos["id_usuario"] is not None:
        if not isinstance(datos["id_usuario"], int) or datos["id_usuario"] <= 0:
            return False, "El id_usuario debe ser un número entero positivo."
    
    return True, ""


def validar_datos_persona(datos):
    """
    Valida los datos de una persona.
    
    Campos esperados:
    - nombre (obligatorio): Nombre de la persona
    - apellido (obligatorio): Apellido de la persona
    - email (obligatorio): Email de la persona
    - telefono (opcional): Teléfono de contacto
    - dni (opcional): DNI de la persona
    - direccion (opcional): Dirección
    - cp (opcional): Código postal
    - poblacion (opcional): Población
    - pais (opcional): País
    """
    
    # 1. Campos obligatorios
    campos_obligatorios = ['nombre', 'apellido', 'email']
    for campo in campos_obligatorios:
        if campo not in datos or not datos[campo]:
            return False, f"El campo '{campo}' es obligatorio y no puede estar vacío."
    
    # 2. Sanitizar campos de texto
    campos_texto = ['nombre', 'apellido', 'dni', 'direccion', 'poblacion', 'pais']
    for campo in campos_texto:
        if campo in datos and datos[campo] is not None:
            datos[campo] = sanitizar_entrada(datos[campo])
    
    # 3. Sanitización específica para email y teléfono
    if 'email' in datos:
        from .sanitizacion import sanitizar_email
        datos['email'] = sanitizar_email(datos['email'])
    
    if 'telefono' in datos and datos['telefono']:
        from .sanitizacion import sanitizar_telefono
        datos['telefono'] = sanitizar_telefono(datos['telefono'])
    
    # 4. Validaciones específicas
    
    # Nombre
    valido, mensaje = validar_longitud_campo(datos['nombre'], 2, 50)
    if not valido:
        return False, f"Nombre: {mensaje}"
    
    if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s\-\']{2,50}$", datos['nombre']):
        return False, "El nombre contiene caracteres no permitidos."
    
    # Apellido
    valido, mensaje = validar_longitud_campo(datos['apellido'], 2, 50)
    if not valido:
        return False, f"Apellido: {mensaje}"
    
    if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s\-\']{2,50}$", datos['apellido']):
        return False, "El apellido contiene caracteres no permitidos."
    
    # Email
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", datos['email']):
        return False, "El formato del email no es válido."
    
    # DNI (si se proporciona)
    if 'dni' in datos and datos['dni']:
        valido, mensaje = validar_longitud_campo(datos['dni'], 8, 12)
        if not valido:
            return False, f"DNI: {mensaje}"
    
    # Teléfono (si se proporciona)
    if 'telefono' in datos and datos['telefono']:
        valido, mensaje = validar_longitud_campo(datos['telefono'], 9, 15)
        if not valido:
            return False, f"Teléfono: {mensaje}"
    
    # Código postal (si se proporciona)
    if 'cp' in datos and datos['cp']:
        datos['cp'] = sanitizar_entrada(datos['cp'])
        if not re.match(r"^\d{5}$", datos['cp']):
            return False, "El código postal debe tener 5 dígitos."
    
    # Otros campos opcionales
    campos_opcionales = ['direccion', 'poblacion', 'pais']
    for campo in campos_opcionales:
        if campo in datos and datos[campo]:
            valido, mensaje = validar_longitud_campo(datos[campo], 2, 100)
            if not valido:
                return False, f"{campo.capitalize()}: {mensaje}"
    
    # 5. Validar id_persona si viene (para actualizaciones)
    if "id_persona" in datos and datos["id_persona"] is not None:
        if not isinstance(datos["id_persona"], int) or datos["id_persona"] <= 0:
            return False, "El id_persona debe ser un número entero positivo."
    
    return True, ""
