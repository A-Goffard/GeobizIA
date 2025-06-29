def validar_datos_actividad_fecha(datos):
    if "id_actividad" not in datos or "id_fecha" not in datos:
        return False, "Faltan campos obligatorios."
    # ...otras validaciones si aplica...
    return True, ""
