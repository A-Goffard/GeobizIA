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

    # Validar números positivos usando sanitización
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


def validar_datos_actividad_realizada(datos):
    # Campos obligatorios
    campos_obligatorios = ["id_actividad", "fecha", "asistentes", "coste_economico", "facturacion"]
    
    for campo in campos_obligatorios:
        if campo not in datos or datos[campo] in [None, ""]:
            return False, f"El campo '{campo}' es obligatorio."
        datos[campo] = sanitizar_entrada(datos[campo])

    # id_actividad debe ser entero positivo
    if not isinstance(datos["id_actividad"], int) or datos["id_actividad"] <= 0:
        return False, "El id_actividad debe ser un número entero positivo."

    # fecha formato simple (YYYY-MM-DD)
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(datos["fecha"])):
        return False, "La fecha debe tener formato YYYY-MM-DD."

    # asistentes debe ser entero positivo
    asistentes_sanitizado = sanitizar_numero(datos["asistentes"])
    if asistentes_sanitizado is None or asistentes_sanitizado < 0:
        return False, "El número de asistentes debe ser un entero positivo."
    datos["asistentes"] = int(asistentes_sanitizado)

    # coste_economico y facturacion deben ser números positivos
    for campo in ["coste_economico", "facturacion"]:
        numero_sanitizado = sanitizar_numero(datos[campo])
        if numero_sanitizado is None:
            return False, f"El campo '{campo}' debe ser un número válido."
        if numero_sanitizado < 0:
            return False, f"El campo '{campo}' debe ser un número positivo."
        datos[campo] = numero_sanitizado

    # observaciones opcional, máximo 500 caracteres
    if "observaciones" in datos and datos["observaciones"]:
        datos["observaciones"] = sanitizar_entrada(datos["observaciones"])
        valido, mensaje = validar_longitud_campo(datos["observaciones"], 0, 500)
        if not valido:
            return False, f"Las observaciones: {mensaje}"

    # id_evento e id_proyecto opcionales, si vienen deben ser enteros positivos o None
    for campo in ["id_evento", "id_proyecto"]:
        if campo in datos and datos[campo] not in [None, ""]:
            numero_sanitizado = sanitizar_numero(datos[campo])
            if numero_sanitizado is None or numero_sanitizado <= 0:
                return False, f"El campo '{campo}' debe ser un entero positivo o nulo."
            datos[campo] = int(numero_sanitizado)

    return True, ""
