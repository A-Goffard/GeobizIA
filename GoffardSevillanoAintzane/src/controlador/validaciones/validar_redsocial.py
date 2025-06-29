def validar_datos_redsocial(datos):
    if "plataforma" in datos and len(datos["plataforma"]) > 100:
        return False, "La plataforma no puede exceder los 100 caracteres."
    # ...otras validaciones...
    return True, ""
