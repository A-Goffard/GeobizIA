def validar_datos_actividad(datos):
    if "nombre" in datos and len(datos["nombre"]) > 100:
        return False, "El nombre no puede exceder los 100 caracteres."
    # ...otras validaciones...
    return True, ""
