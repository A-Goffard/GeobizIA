from .sanitizacion import sanitizar_entrada, sanitizar_dict, validar_longitud_campo

def validar_datos_tema_ambiental(datos):
    """
    Valida los datos de un tema ambiental.
    
    Args:
        datos (dict): Diccionario con los datos del tema ambiental
        
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
    campos_obligatorios = ['nombre', 'categoria']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar nombre
    if not validar_longitud_campo(datos_sanitizados['nombre'], min_length=3, max_length=100):
        return False, "El nombre debe tener entre 3 y 100 caracteres"
    
    # Validar categoría ambiental
    categorias_validas = ['AGUA', 'AIRE', 'SUELO', 'BIODIVERSIDAD', 'CLIMA', 'ENERGIA', 'RESIDUOS', 'CONTAMINACION', 'SOSTENIBILIDAD', 'OTRO']
    if datos_sanitizados['categoria'].upper() not in categorias_validas:
        return False, f"Categoría inválida. Categorías válidas: {', '.join(categorias_validas)}"
    
    # Validar descripción (opcional)
    if 'descripcion' in datos_sanitizados and datos_sanitizados['descripcion']:
        if not validar_longitud_campo(datos_sanitizados['descripcion'], max_length=500):
            return False, "La descripción no puede exceder los 500 caracteres"
    
    # Validar importancia (opcional)
    if 'importancia' in datos_sanitizados and datos_sanitizados['importancia']:
        importancias_validas = ['BAJA', 'MEDIA', 'ALTA', 'CRITICA']
        if datos_sanitizados['importancia'].upper() not in importancias_validas:
            return False, f"Importancia inválida. Importancias válidas: {', '.join(importancias_validas)}"
    
    return True, "Validación exitosa"
