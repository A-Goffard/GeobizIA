def validar_datos_cliente(datos):
    if "razon_social" in datos and len(datos["razon_social"]) > 100:
        return False, "La razón social no puede exceder los 100 caracteres."
    # ...otras validaciones...
    return True, ""
