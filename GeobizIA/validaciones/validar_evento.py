from datetime import datetime

def validar_datos_evento(datos):

    # 1. Campos obligatorios
    campos_obligatorios = ['nombre', 'fecha_comienzo', 'fecha_final']
    for campo in campos_obligatorios:
        if campo not in datos or not datos[campo]:
            return False, f"El campo '{campo}' es obligatorio y no puede estar vacío."

    # 2. Validación de tipos y formatos
    # Nombre
    if not isinstance(datos['nombre'], str) or len(datos['nombre'].strip()) == 0:
        return False, "El nombre debe ser un texto no vacío."
    if len(datos['nombre']) > 100:
        return False, "El nombre no puede exceder los 100 caracteres."

    # Fechas
    try:
        fecha_comienzo = datetime.strptime(datos['fecha_comienzo'], '%Y-%m-%d')
        fecha_final = datetime.strptime(datos['fecha_final'], '%Y-%m-%d')
    except ValueError:
        return False, "Las fechas deben tener el formato 'YYYY-MM-DD'."

    # 3. Reglas de negocio
    # La fecha de fin no puede ser anterior a la de inicio
    if fecha_final < fecha_comienzo:
        return False, "La fecha de fin no puede ser anterior a la fecha de comienzo."

    # Campos de texto opcionales
    for campo in ['descripcion', 'responsable', 'ubicacion']:
        if campo in datos and datos[campo] is not None:
            if not isinstance(datos[campo], str):
                return False, f"El campo '{campo}' debe ser un texto."
            if len(datos[campo]) > 255: # Límite genérico, se puede ajustar
                return False, f"El campo '{campo}' no puede exceder los 255 caracteres."

    # 4. Si todo es correcto
    return True, ""
