def validar_datos_auditoria_publicacion(datos):
    if "resultado" in datos and len(datos["resultado"]) > 100:
        return False, "El resultado no puede exceder los 100 caracteres."
    # ...otras validaciones...
    return True, ""
