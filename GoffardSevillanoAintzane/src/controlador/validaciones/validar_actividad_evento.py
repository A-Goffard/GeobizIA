def validar_datos_actividad_evento(datos):
    if "id_actividad" not in datos or "id_evento" not in datos:
        return False, "Faltan campos obligatorios."
    # ...otras validaciones si aplica...
    return True, ""
