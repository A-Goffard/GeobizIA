def validar_datos_persona(datos):
    if "nombre" in datos and len(datos["nombre"]) > 100:
        return False, "El nombre no puede exceder los 100 caracteres."
    if "email" in datos and "@" not in datos["email"]:
        return False, "El email debe ser válido."
    # ...otras validaciones...
    return True, ""
