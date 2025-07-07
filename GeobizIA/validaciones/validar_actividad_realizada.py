import re
import html


def sanitize_input(value):
    if isinstance(value, str):
        value = ''.join(c for c in value if c.isprintable())
        value = html.escape(value.strip())
    return value


def validar_datos_actividad(datos):
    # Sanitiza y valida campos obligatorios
    campos_obligatorios = [
        # "id_actividad",  # Elimina este campo de los obligatorios
        "tipo", "nombre", "descripcion", "responsable",
        "duracion", "coste_economico", "coste_horas", "facturacion"
    ]
    for campo in campos_obligatorios:
        if campo not in datos or datos[campo] in [None, ""]:
            return False, f"El campo '{campo}' es obligatorio."
        datos[campo] = sanitize_input(datos[campo])

    # Validar id_actividad solo si viene (por ejemplo, para actualizar)
    if "id_actividad" in datos and datos["id_actividad"] is not None:
        if not isinstance(datos["id_actividad"], int) or datos["id_actividad"] <= 0:
            return False, "El id_actividad debe ser un número entero positivo."

    # Validar tipo, nombre, responsable (solo letras, espacios y algunos símbolos)
    for campo in ["tipo", "nombre", "responsable"]:
        if not re.match(r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ\-\.]{2,100}$", datos[campo]):
            return False, f"El campo '{campo}' contiene caracteres no permitidos o es demasiado corto/largo."

    # Validar descripción
    if len(datos["descripcion"]) > 500:
        return False, "La descripción no puede exceder los 500 caracteres."

    # Validar duración (ejemplo: "2 horas", "1h", "30min")
    if not re.match(r"^[\w\s\d\.]{1,50}$", datos["duracion"]):
        return False, "La duración contiene caracteres no válidos."

    # Validar números positivos
    for campo in ["coste_economico", "coste_horas", "facturacion"]:
        try:
            valor = float(datos[campo])
            if valor < 0:
                return False, f"El campo '{campo}' debe ser un número positivo."
        except Exception:
            return False, f"El campo '{campo}' debe ser un número válido."

    # Validar opcionales (resultados, valoracion, observaciones)
    for campo in ["resultados", "valoracion", "observaciones"]:
        if campo in datos and datos[campo]:
            datos[campo] = sanitize_input(datos[campo])
            if len(datos[campo]) > 500:
                return False, f"El campo '{campo}' no puede exceder los 500 caracteres."

    return True, ""


def validar_datos_actividad_realizada(datos):
    # Campos obligatorios
    campos_obligatorios = ["id_actividad", "fecha", "asistentes", "coste_economico", "facturacion"]
    for campo in campos_obligatorios:
        if campo not in datos or datos[campo] in [None, ""]:
            return False, f"El campo '{campo}' es obligatorio."
        datos[campo] = sanitize_input(datos[campo])

    # id_actividad debe ser entero positivo
    if not isinstance(datos["id_actividad"], int) or datos["id_actividad"] <= 0:
        return False, "El id_actividad debe ser un número entero positivo."

    # fecha formato simple (YYYY-MM-DD)
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(datos["fecha"])):
        return False, "La fecha debe tener formato YYYY-MM-DD."

    # asistentes debe ser entero positivo
    try:
        asistentes = int(datos["asistentes"])
        if asistentes < 0:
            return False, "El número de asistentes debe ser positivo."
    except Exception:
        return False, "El número de asistentes debe ser un entero."

    # coste_economico y facturacion deben ser números positivos
    for campo in ["coste_economico", "facturacion"]:
        try:
            valor = float(datos[campo])
            if valor < 0:
                return False, f"El campo '{campo}' debe ser un número positivo."
        except Exception:
            return False, f"El campo '{campo}' debe ser un número válido."

    # observaciones opcional, máximo 500 caracteres
    if "observaciones" in datos and datos["observaciones"]:
        datos["observaciones"] = sanitize_input(datos["observaciones"])
        if len(datos["observaciones"]) > 500:
            return False, "El campo 'observaciones' no puede exceder los 500 caracteres."

    # id_evento e id_proyecto opcionales, si vienen deben ser enteros positivos o None
    for campo in ["id_evento", "id_proyecto"]:
        if campo in datos and datos[campo] not in [None, ""]:
            try:
                if int(datos[campo]) <= 0:
                    return False, f"El campo '{campo}' debe ser un entero positivo o nulo."
            except Exception:
                return False, f"El campo '{campo}' debe ser un entero o nulo."

    return True, ""
