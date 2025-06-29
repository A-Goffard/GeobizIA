def validar_datos_publicacion_tag(datos):
    if "id_publicacion" not in datos or "id_tag" not in datos:
        return False, "Faltan campos obligatorios."
    # ...otras validaciones si aplica...
    return True, ""
