def validar_datos_proyecto_actividad(datos):
    if "id_proyecto" not in datos or "id_actividad" not in datos:
        return False, "Faltan campos obligatorios."
    # ...otras validaciones si aplica...
    return True, ""
