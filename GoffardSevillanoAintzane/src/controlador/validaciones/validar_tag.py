def validar_datos_tag(datos):
    if "palabra_clave" in datos and len(datos["palabra_clave"]) > 100:
        return False, "La palabra clave no puede exceder los 100 caracteres."
    # ...otras validaciones...
    return True, ""
