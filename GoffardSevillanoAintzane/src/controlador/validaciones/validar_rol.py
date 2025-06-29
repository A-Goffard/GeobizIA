def validar_datos_rol(datos):
    if "nombre" in datos and len(datos["nombre"]) > 100:
        return False, "El nombre no puede exceder los 100 caracteres."
    # ...otras validaciones...
    return True, ""
