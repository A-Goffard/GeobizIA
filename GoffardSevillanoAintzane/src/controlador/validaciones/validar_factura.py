def validar_datos_factura(datos):
    if "numero_factura" in datos and len(datos["numero_factura"]) > 50:
        return False, "El número de factura no puede exceder los 50 caracteres."
    # ...otras validaciones...
    return True, ""
