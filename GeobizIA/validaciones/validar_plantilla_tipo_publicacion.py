def validar_datos_plantilla_tipo_publicacion(datos):
    if "id_plantilla" not in datos or "id_tipo_publicacion" not in datos:
        return False, "Faltan campos obligatorios."
    # ...otras validaciones si aplica...
    return True, ""
