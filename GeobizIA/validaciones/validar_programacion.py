def validar_datos_programacion(datos):
    if "estado" in datos and len(datos["estado"]) > 50:
        return False, "El estado no puede exceder los 50 caracteres."
    # ...otras validaciones...
    return True, ""
