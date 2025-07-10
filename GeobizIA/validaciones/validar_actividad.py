import re
from .sanitizacion import sanitizar_entrada, sanitizar_numero, validar_longitud_campo


def validar_datos_actividad(datos):
    # Sanitiza y valida campos obligatorios
    campos_obligatorios = [
        "tipo", "nombre", "descripcion", "responsable",
        "duracion", "coste_economico", "coste_horas", "facturacion"
    ]
    
    for campo in campos_obligatorios:
        if campo not in datos or datos[campo] in [None, ""]:
            return False, f"El campo '{campo}' es obligatorio."
        datos[campo] = sanitizar_entrada(datos[campo])

    # Validar id_actividad solo si viene (por ejemplo, para actualizar)
    if "id_actividad" in datos and datos["id_actividad"] is not None:
        if not isinstance(datos["id_actividad"], int) or datos["id_actividad"] <= 0:
            return False, "El id_actividad debe ser un número entero positivo."

    # Validar tipo, nombre, responsable (solo letras, espacios y algunos símbolos)
    for campo in ["tipo", "nombre", "responsable"]:
        valido, mensaje = validar_longitud_campo(datos[campo], 2, 100)
        if not valido:
            return False, f"El campo '{campo}': {mensaje}"
        if not re.match(r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ\-\.]{2,100}$", datos[campo]):
            return False, f"El campo '{campo}' contiene caracteres no permitidos."

    # Validar descripción
    valido, mensaje = validar_longitud_campo(datos["descripcion"], 1, 500)
    if not valido:
        return False, f"La descripción: {mensaje}"

    # Validar duración
    valido, mensaje = validar_longitud_campo(datos["duracion"], 1, 50)
    if not valido:
        return False, f"La duración: {mensaje}"
    if not re.match(r"^[\w\s\d\.]{1,50}$", datos["duracion"]):
        return False, "La duración contiene caracteres no válidos."

    # Validar números positivos usando sanitización mejorada
    for campo in ["coste_economico", "coste_horas", "facturacion"]:
        numero_sanitizado = sanitizar_numero(datos[campo])
        if numero_sanitizado is None:
            return False, f"El campo '{campo}' debe ser un número válido."
        if numero_sanitizado < 0:
            return False, f"El campo '{campo}' debe ser un número positivo."
        datos[campo] = numero_sanitizado

    # Validar campos opcionales
    for campo in ["resultados", "valoracion", "observaciones"]:
        if campo in datos and datos[campo]:
            datos[campo] = sanitizar_entrada(datos[campo])
            valido, mensaje = validar_longitud_campo(datos[campo], 0, 500)
            if not valido:
                return False, f"El campo '{campo}': {mensaje}"

    return True, ""
