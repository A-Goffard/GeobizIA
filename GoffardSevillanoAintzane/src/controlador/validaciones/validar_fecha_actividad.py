def validar_datos_fecha_actividad(datos):
    if "fecha" in datos and not datos["fecha"]:
        return False, "La fecha es obligatoria."
    # ...otras validaciones...
    return True, ""
