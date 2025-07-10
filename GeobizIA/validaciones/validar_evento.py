from datetime import datetime
import re
from .sanitizacion import sanitizar_entrada, validar_longitud_campo

def validar_datos_evento(datos):

    # 1. Campos obligatorios
    campos_obligatorios = ['nombre', 'fecha_comienzo', 'fecha_final']
    for campo in campos_obligatorios:
        if campo not in datos or not datos[campo]:
            return False, f"El campo '{campo}' es obligatorio y no puede estar vacío."

    # 2. Sanitizar campos de texto
    campos_texto = ['nombre', 'descripcion', 'responsable', 'ubicacion']
    for campo in campos_texto:
        if campo in datos and datos[campo] is not None:
            datos[campo] = sanitizar_entrada(datos[campo])

    # 3. Validación de tipos y formatos
    # Nombre
    if not isinstance(datos['nombre'], str) or len(datos['nombre'].strip()) == 0:
        return False, "El nombre debe ser un texto no vacío."
    
    valido, mensaje = validar_longitud_campo(datos['nombre'], 1, 100)
    if not valido:
        return False, f"El nombre: {mensaje}"
    
    # Validar que el nombre solo contenga caracteres permitidos
    if not re.match(r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ\-\.\,\:\!]{1,100}$", datos['nombre']):
        return False, "El nombre contiene caracteres no permitidos."

    # Fechas - Validar formato primero
    try:
        fecha_comienzo = datetime.strptime(str(datos['fecha_comienzo']), '%Y-%m-%d')
        fecha_final = datetime.strptime(str(datos['fecha_final']), '%Y-%m-%d')
    except ValueError:
        return False, "Las fechas deben tener el formato 'YYYY-MM-DD'."

    # 4. Reglas de negocio
    # La fecha de fin no puede ser anterior a la de inicio
    if fecha_final < fecha_comienzo:
        return False, "La fecha de fin no puede ser anterior a la fecha de comienzo."

    # Validar que las fechas no sean muy antiguas (opcional - ajusta según necesidad)
    fecha_limite = datetime(2020, 1, 1)
    if fecha_comienzo < fecha_limite:
        return False, "La fecha de comienzo no puede ser anterior al año 2020."

    # 5. Campos de texto opcionales con validación mejorada
    campos_opcionales = {
        'descripcion': 500,
        'responsable': 100,
        'ubicacion': 255
    }
    
    for campo, max_length in campos_opcionales.items():
        if campo in datos and datos[campo] is not None:
            if not isinstance(datos[campo], str):
                return False, f"El campo '{campo}' debe ser un texto."
            
            valido, mensaje = validar_longitud_campo(datos[campo], 0, max_length)
            if not valido:
                return False, f"El campo '{campo}': {mensaje}"
            
            # Validación específica para responsable
            if campo == 'responsable' and datos[campo]:
                if not re.match(r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ\-\.]{1,100}$", datos[campo]):
                    return False, "El responsable contiene caracteres no permitidos."

    # 6. Validar id_evento si viene (para actualizaciones)
    if "id_evento" in datos and datos["id_evento"] is not None:
        if not isinstance(datos["id_evento"], int) or datos["id_evento"] <= 0:
            return False, "El id_evento debe ser un número entero positivo."

    # 7. Si todo es correcto
    return True, ""
