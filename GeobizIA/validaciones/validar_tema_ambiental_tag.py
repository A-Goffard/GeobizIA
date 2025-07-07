def validar_datos_tema_ambiental_tag(datos):
    if "id_tema_ambiental" not in datos or "id_tag" not in datos:
        return False, "Faltan campos obligatorios."
    # ...otras validaciones si aplica...
    return True, ""
