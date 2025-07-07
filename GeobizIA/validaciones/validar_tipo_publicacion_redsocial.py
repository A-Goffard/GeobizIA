def validar_datos_tipo_publicacion_redsocial(datos):
    if "id_tipo_publicacion" not in datos or "id_red_social" not in datos:
        return False, "Faltan campos obligatorios."
    # ...otras validaciones si aplica...
    return True, ""
