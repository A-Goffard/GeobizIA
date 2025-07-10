from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, validar_longitud_campo
import re
from datetime import datetime

def validar_datos_factura(datos):
    """
    Valida los datos de una factura según el modelo GeobizIA.
    
    Args:
        datos (dict): Diccionario con los datos de la factura
        
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
    
    # Validar campos obligatorios según el modelo
    campos_obligatorios = ['id_cliente', 'fecha_facturacion', 'fecha_vencimiento', 'concepto', 'responsable', 'numero_factura', 'tipo_pago']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not str(datos_sanitizados[campo]).strip():
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar id_cliente
    try:
        id_cliente = int(datos_sanitizados['id_cliente'])
        if id_cliente <= 0:
            return False, "El ID del cliente debe ser un número entero positivo"
    except (ValueError, TypeError):
        return False, "El ID del cliente debe ser un número entero válido"
    
    # Validar fechas
    try:
        fecha_facturacion = datetime.strptime(datos_sanitizados['fecha_facturacion'], '%Y-%m-%d')
        fecha_vencimiento = datetime.strptime(datos_sanitizados['fecha_vencimiento'], '%Y-%m-%d')
        
        if fecha_vencimiento <= fecha_facturacion:
            return False, "La fecha de vencimiento debe ser posterior a la fecha de facturación"
            
    except ValueError:
        return False, "Las fechas deben tener formato YYYY-MM-DD"
    
    # Validar concepto
    if not validar_longitud_campo(datos_sanitizados['concepto'], min_length=5, max_length=500):
        return False, "El concepto debe tener entre 5 y 500 caracteres"
    
    # Validar responsable
    if not validar_longitud_campo(datos_sanitizados['responsable'], min_length=2, max_length=100):
        return False, "El responsable debe tener entre 2 y 100 caracteres"
    
    # Validar número de factura
    if not validar_longitud_campo(datos_sanitizados['numero_factura'], min_length=3, max_length=50):
        return False, "El número de factura debe tener entre 3 y 50 caracteres"
    
    # Validar formato del número de factura
    if not re.match(r'^[A-Z0-9-]+$', datos_sanitizados['numero_factura'].upper()):
        return False, "El número de factura solo puede contener letras, números y guiones"
    
    # Validar tipo de pago
    tipos_pago_validos = ['efectivo', 'transferencia', 'tarjeta', 'cheque']
    if datos_sanitizados['tipo_pago'].lower() not in tipos_pago_validos:
        return False, f"Tipo de pago inválido. Tipos válidos: {', '.join(tipos_pago_validos)}"
    
    # Validar campos numéricos opcionales
    campos_numericos = ['iva', 'coste_total', 'base_imponible', 'irpf']
    for campo in campos_numericos:
        if campo in datos_sanitizados and datos_sanitizados[campo] is not None:
            try:
                valor = float(datos_sanitizados[campo])
                if valor < 0:
                    return False, f"El campo '{campo}' no puede ser negativo"
                if campo in ['iva', 'irpf'] and valor > 100:
                    return False, f"El campo '{campo}' no puede ser mayor a 100%"
                if campo in ['coste_total', 'base_imponible'] and valor > 999999999.99:
                    return False, f"El campo '{campo}' excede el límite máximo"
            except (ValueError, TypeError):
                return False, f"El campo '{campo}' debe ser un número válido"
    
    return True, "Validación exitosa"
