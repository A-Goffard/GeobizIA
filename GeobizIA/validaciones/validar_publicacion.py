def validar_datos_publicacion(datos):
    if "titulo" in datos and len(datos["titulo"]) > 200:
        return False, "El título no puede exceder los 200 caracteres."
    # ...otras validaciones...
    return True, ""
