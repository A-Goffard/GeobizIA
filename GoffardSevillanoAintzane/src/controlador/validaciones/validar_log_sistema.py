def validar_datos_log_sistema(datos):
    if "accion" in datos and len(datos["accion"]) > 100:
        return False, "La acción no puede exceder los 100 caracteres."
    # ...otras validaciones...
    return True, ""
