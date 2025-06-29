def validar_datos_participante(datos):
    if "rol" in datos and len(datos["rol"]) > 50:
        return False, "El rol no puede exceder los 50 caracteres."
    # ...otras validaciones...
    return True, ""
