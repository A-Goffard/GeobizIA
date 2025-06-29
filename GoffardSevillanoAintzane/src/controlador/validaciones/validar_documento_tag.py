def validar_datos_documento_tag(datos):
    if "id_documento" not in datos or "id_tag" not in datos:
        return False, "Faltan campos obligatorios."
    # ...otras validaciones si aplica...
    return True, ""
