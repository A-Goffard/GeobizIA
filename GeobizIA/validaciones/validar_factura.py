from .sanitizacion import sanitizar_entrada, sanitizar_dict, sanitizar_numero, validar_longitud_campo
import re
from datetime import datetime

def validar_datos_factura(datos):
    """
    Valida los datos de una factura.
    
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
    
    # Validar campos obligatorios
    campos_obligatorios = ['numero_factura', 'fecha_emision', 'cliente_id', 'total']
    for campo in campos_obligatorios:
        if campo not in datos_sanitizados or not datos_sanitizados[campo]:
            return False, f"El campo '{campo}' es obligatorio"
    
    # Validar número de factura
    if not validar_longitud_campo(datos_sanitizados['numero_factura'], min_length=3, max_length=50):
        return False, "El número de factura debe tener entre 3 y 50 caracteres"
    
    # Validar formato del número de factura (letras, números, guiones)
    if not re.match(r'^[A-Z0-9-]+$', datos_sanitizados['numero_factura']):
        return False, "El número de factura solo puede contener letras mayúsculas, números y guiones"
    
    # Validar fecha de emisión
    try:
        fecha_emision = datetime.strptime(datos_sanitizados['fecha_emision'], '%Y-%m-%d')
        if fecha_emision > datetime.now():
            return False, "La fecha de emisión no puede ser futura"
    except ValueError:
        return False, "La fecha de emisión debe tener formato YYYY-MM-DD"
    
    # Validar cliente_id
    cliente_id_sanitizado = sanitizar_numero(datos_sanitizados['cliente_id'])
    if cliente_id_sanitizado is None or cliente_id_sanitizado <= 0:
        return False, "El ID del cliente debe ser un número entero positivo"
    
    # Validar total
    total_sanitizado = sanitizar_numero(datos_sanitizados['total'])
    if total_sanitizado is None:
        return False, "El total debe ser un número válido"
    if total_sanitizado < 0:
        return False, "El total no puede ser negativo"
    if total_sanitizado > 999999999.99:
        return False, "El total no puede exceder 999,999,999.99"
    
    # Validar subtotal (opcional)
    if 'subtotal' in datos_sanitizados and datos_sanitizados['subtotal']:
        subtotal_sanitizado = sanitizar_numero(datos_sanitizados['subtotal'])
        if subtotal_sanitizado is None:
            return False, "El subtotal debe ser un número válido"
        if subtotal_sanitizado < 0:
            return False, "El subtotal no puede ser negativo"
        if subtotal_sanitizado > total_sanitizado:
            return False, "El subtotal no puede ser mayor que el total"
    
    # Validar impuestos (opcional)
    if 'impuestos' in datos_sanitizados and datos_sanitizados['impuestos']:
        impuestos_sanitizado = sanitizar_numero(datos_sanitizados['impuestos'])
        if impuestos_sanitizado is None:
            return False, "Los impuestos deben ser un número válido"
        if impuestos_sanitizado < 0:
            return False, "Los impuestos no pueden ser negativos"
    
    # Validar descuento (opcional)
    if 'descuento' in datos_sanitizados and datos_sanitizados['descuento']:
        descuento_sanitizado = sanitizar_numero(datos_sanitizados['descuento'])
        if descuento_sanitizado is None:
            return False, "El descuento debe ser un número válido"
        if descuento_sanitizado < 0 or descuento_sanitizado > 100:
            return False, "El descuento debe estar entre 0 y 100 (porcentaje)"
    
    # Validar estado de la factura (opcional)
    if 'estado' in datos_sanitizados and datos_sanitizados['estado']:
        estados_validos = ['BORRADOR', 'EMITIDA', 'ENVIADA', 'PAGADA', 'VENCIDA', 'CANCELADA']
        if datos_sanitizados['estado'].upper() not in estados_validos:
            return False, f"Estado inválido. Estados válidos: {', '.join(estados_validos)}"
    
    # Validar fecha de vencimiento (opcional)
    if 'fecha_vencimiento' in datos_sanitizados and datos_sanitizados['fecha_vencimiento']:
        try:
            fecha_vencimiento = datetime.strptime(datos_sanitizados['fecha_vencimiento'], '%Y-%m-%d')
            if fecha_vencimiento <= fecha_emision:
                return False, "La fecha de vencimiento debe ser posterior a la fecha de emisión"
        except ValueError:
            return False, "La fecha de vencimiento debe tener formato YYYY-MM-DD"
    
    # Validar método de pago (opcional)
    if 'metodo_pago' in datos_sanitizados and datos_sanitizados['metodo_pago']:
        metodos_validos = ['EFECTIVO', 'TARJETA_CREDITO', 'TARJETA_DEBITO', 'TRANSFERENCIA', 'CHEQUE', 'PAYPAL', 'OTRO']
        if datos_sanitizados['metodo_pago'].upper() not in metodos_validos:
            return False, f"Método de pago inválido. Métodos válidos: {', '.join(metodos_validos)}"
    
    # Validar moneda (opcional)
    if 'moneda' in datos_sanitizados and datos_sanitizados['moneda']:
        monedas_validas = ['EUR', 'USD', 'GBP', 'COP', 'MXN', 'ARS', 'CLP', 'PEN', 'VEF']
        if datos_sanitizados['moneda'].upper() not in monedas_validas:
            return False, f"Moneda inválida. Monedas válidas: {', '.join(monedas_validas)}"
    
    # Validar notas (opcional)
    if 'notas' in datos_sanitizados and datos_sanitizados['notas']:
        if not validar_longitud_campo(datos_sanitizados['notas'], max_length=500):
            return False, "Las notas no pueden exceder los 500 caracteres"
    
    # Validar proyecto_id (opcional)
    if 'proyecto_id' in datos_sanitizados and datos_sanitizados['proyecto_id']:
        proyecto_id_sanitizado = sanitizar_numero(datos_sanitizados['proyecto_id'])
        if proyecto_id_sanitizado is None or proyecto_id_sanitizado <= 0:
            return False, "El ID del proyecto debe ser un número entero positivo"
    
    return True, "Validación exitosa"
