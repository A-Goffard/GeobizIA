def validar_datos_documento(datos):
    if "titulo" in datos and len(datos["titulo"]) > 100:
        return False, "El título no puede exceder los 100 caracteres."
    # ...otras validaciones...
    return True, ""
