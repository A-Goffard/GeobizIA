def validar_datos_factura_actividad(datos):
    if "id_factura" not in datos or "id_actividad" not in datos:
        return False, "Faltan campos obligatorios."
    # ...otras validaciones si aplica...
    return True, ""
