from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, validar_longitud_campo
import re
from datetime import datetime

def validar_datos_proyecto(datos):
    """
    Valida los datos de un proyecto.
    
    Args:
        datos (dict): Diccionario con los datos del proyecto
        
    Returns:
        tuple: (bool, str) - (es_valido, mensaje_error)
    """
    if not isinstance(datos, dict):
        return False, "Los datos deben ser un diccionario válido"
    
    # Sanitizar todos los datos de entrada
    try:
        datos_sanitizados = sanitizar_dict(datos)
    except Exception as e:
        return False, f"Error al sanitizar datos: {str(e)}"
    
    # Validar campos obligatorios
    campos_obligatorios = ['nombre', 'descripcion', 'estado']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
      # Validar nombre del proyecto
    nombre_valido, nombre_msg = validar_longitud_campo(datos_sanitizados['nombre'], min_length=3, max_length=200)
    if not nombre_valido:
        return False, f"Nombre del proyecto inválido: {nombre_msg}"

    # Validar descripción
    descripcion_valida, descripcion_msg = validar_longitud_campo(datos_sanitizados['descripcion'], min_length=10, max_length=1000)
    if not descripcion_valida:
        return False, f"Descripción inválida: {descripcion_msg}"
    
    # Validar estado del proyecto
    estados_validos = ['PLANIFICACION', 'EN_PROGRESO', 'PAUSADO', 'COMPLETADO', 'CANCELADO']
    if datos_sanitizados['estado'].upper() not in estados_validos:
        return False, f"Estado inválido. Estados válidos: {', '.join(estados_validos)}"
    
    # Validar fecha de inicio (opcional)
    if 'fecha_inicio' in datos_sanitizados and datos_sanitizados['fecha_inicio']:
        try:
            fecha_inicio = datetime.strptime(datos_sanitizados['fecha_inicio'], '%Y-%m-%d')
        except ValueError:
            return False, "La fecha de inicio debe tener formato YYYY-MM-DD"
    
    # Validar fecha de fin (opcional)
    if 'fecha_fin' in datos_sanitizados and datos_sanitizados['fecha_fin']:
        try:
            fecha_fin = datetime.strptime(datos_sanitizados['fecha_fin'], '%Y-%m-%d')
            # Si hay fecha de inicio, validar que la fecha de fin sea posterior
            if 'fecha_inicio' in datos_sanitizados and datos_sanitizados['fecha_inicio']:
                fecha_inicio = datetime.strptime(datos_sanitizados['fecha_inicio'], '%Y-%m-%d')
                if fecha_fin <= fecha_inicio:
                    return False, "La fecha de fin debe ser posterior a la fecha de inicio"
        except ValueError:
            return False, "La fecha de fin debe tener formato YYYY-MM-DD"
    
    # Validar presupuesto (opcional)
    if 'presupuesto' in datos_sanitizados and datos_sanitizados['presupuesto']:
        presupuesto_sanitizado = sanitizar_numero(datos_sanitizados['presupuesto'])
        if presupuesto_sanitizado is None:
            return False, "El presupuesto debe ser un número válido"
        if presupuesto_sanitizado < 0:
            return False, "El presupuesto no puede ser negativo"
        if presupuesto_sanitizado > 999999999.99:
            return False, "El presupuesto no puede exceder 999,999,999.99"
    
    # Validar prioridad (opcional)
    if 'prioridad' in datos_sanitizados and datos_sanitizados['prioridad']:
        prioridades_validas = ['BAJA', 'MEDIA', 'ALTA', 'CRITICA']
        if datos_sanitizados['prioridad'].upper() not in prioridades_validas:
            return False, f"Prioridad inválida. Prioridades válidas: {', '.join(prioridades_validas)}"
    
    # Validar cliente_id (opcional)
    if 'cliente_id' in datos_sanitizados and datos_sanitizados['cliente_id']:
        cliente_id_sanitizado = sanitizar_numero(datos_sanitizados['cliente_id'])
        if cliente_id_sanitizado is None or cliente_id_sanitizado <= 0:
            return False, "El ID del cliente debe ser un número entero positivo"
    
    # Validar responsable_id (opcional)
    if 'responsable_id' in datos_sanitizados and datos_sanitizados['responsable_id']:
        responsable_id_sanitizado = sanitizar_numero(datos_sanitizados['responsable_id'])
        if responsable_id_sanitizado is None or responsable_id_sanitizado <= 0:
            return False, "El ID del responsable debe ser un número entero positivo"
      # Validar objetivos (opcional)
    if 'objetivos' in datos_sanitizados and datos_sanitizados['objetivos']:
        objetivos_validos, objetivos_msg = validar_longitud_campo(datos_sanitizados['objetivos'], max_length=2000)
        if not objetivos_validos:
            return False, f"Objetivos inválidos: {objetivos_msg}"

    # Validar alcance (opcional)
    if 'alcance' in datos_sanitizados and datos_sanitizados['alcance']:
        alcance_valido, alcance_msg = validar_longitud_campo(datos_sanitizados['alcance'], max_length=1500)
        if not alcance_valido:
            return False, f"Alcance inválido: {alcance_msg}"
    
    # Validar metodología (opcional)
    if 'metodologia' in datos_sanitizados and datos_sanitizados['metodologia']:
        metodologias_validas = ['AGIL', 'SCRUM', 'KANBAN', 'WATERFALL', 'LEAN', 'OTRO']
        if datos_sanitizados['metodologia'].upper() not in metodologias_validas:
            return False, f"Metodología inválida. Metodologías válidas: {', '.join(metodologias_validas)}"
    
    # Validar tags del proyecto (opcional)
    if 'tags' in datos_sanitizados and datos_sanitizados['tags']:
        if isinstance(datos_sanitizados['tags'], list):
            for tag in datos_sanitizados['tags']:
                if not isinstance(tag, str) or len(tag) > 50:
                    return False, "Cada tag debe ser una cadena de máximo 50 caracteres"
        else:
            return False, "Los tags deben ser una lista"
    
    return True, "Validación exitosa"
