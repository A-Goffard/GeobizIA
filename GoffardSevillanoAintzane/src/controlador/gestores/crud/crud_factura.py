from src.controlador.dominios.factura import Factura
from src.controlador.gestores.facturas import Facturas

def crear_factura(id_factura, id_cliente, tipo=None, nombre=None, direccion=None, nif=None, fecha_facturacion=None, fecha_vencimiento=None, concepto=None, responsable=None, iva=None, coste_total=None, base_imponible=None, numero_factura=None, tipo_pago=None, irpf=None):
    """
    Crea una nueva factura en la base de datos.

    Args:
        id_factura (int): ID de la factura.
        id_cliente (int): ID del cliente asociado.
        tipo (str, optional): Tipo de factura.
        nombre (str, optional): Nombre en la factura.
        direccion (str, optional): Dirección en la factura.
        nif (str, optional): NIF en la factura.
        fecha_facturacion (str, optional): Fecha de facturación.
        fecha_vencimiento (str, optional): Fecha de vencimiento.
        concepto (str, optional): Concepto de la factura.
        responsable (str, optional): Responsable de la factura.
        iva (float, optional): IVA aplicado.
        coste_total (float, optional): Coste total de la factura.
        base_imponible (float, optional): Base imponible de la factura.
        numero_factura (str, optional): Número de la factura.
        tipo_pago (str, optional): Tipo de pago.
        irpf (float, optional): IRPF aplicado.

    Returns:
        Factura: Objeto Factura creado, o None si falla.
    """
    gestor = Facturas()
    return gestor.agregar(id_factura=id_factura, id_cliente=id_cliente, tipo=tipo, nombre=nombre, direccion=direccion, nif=nif, fecha_facturacion=fecha_facturacion, fecha_vencimiento=fecha_vencimiento, concepto=concepto, responsable=responsable, iva=iva, coste_total=coste_total, base_imponible=base_imponible, numero_factura=numero_factura, tipo_pago=tipo_pago, irpf=irpf)

def leer_factura(id_factura):
    """
    Lee una factura por su ID.

    Args:
        id_factura (int): ID de la factura.

    Returns:
        Factura: Objeto Factura si se encuentra, o None si no.
    """
    gestor = Facturas()
    return gestor.buscar(id_factura)

def actualizar_factura(id_factura, id_cliente=None, tipo=None, nombre=None, direccion=None, nif=None, fecha_facturacion=None, fecha_vencimiento=None, concepto=None, responsable=None, iva=None, coste_total=None, base_imponible=None, numero_factura=None, tipo_pago=None, irpf=None):
    """
    Actualiza una factura existente.

    Args:
        id_factura (int): ID de la factura.
        id_cliente (int, optional): Nuevo ID del cliente asociado.
        tipo (str, optional): Nuevo tipo.
        nombre (str, optional): Nuevo nombre.
        direccion (str, optional): Nueva dirección.
        nif (str, optional): Nuevo NIF.
        fecha_facturacion (str, optional): Nueva fecha de facturación.
        fecha_vencimiento (str, optional): Nueva fecha de vencimiento.
        concepto (str, optional): Nuevo concepto.
        responsable (str, optional): Nuevo responsable.
        iva (float, optional): Nuevo IVA.
        coste_total (float, optional): Nuevo coste total.
        base_imponible (float, optional): Nueva base imponible.
        numero_factura (str, optional): Nuevo número de factura.
        tipo_pago (str, optional): Nuevo tipo de pago.
        irpf (float, optional): Nuevo IRPF.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Facturas()
    return gestor.actualizar(id_factura, id_cliente=id_cliente, tipo=tipo, nombre=nombre, direccion=direccion, nif=nif, fecha_facturacion=fecha_facturacion, fecha_vencimiento=fecha_vencimiento, concepto=concepto, responsable=responsable, iva=iva, coste_total=coste_total, base_imponible=base_imponible, numero_factura=numero_factura, tipo_pago=tipo_pago, irpf=irpf)

def eliminar_factura(id_factura):
    """
    Elimina una factura por su ID.

    Args:
        id_factura (int): ID de la factura.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Facturas()
    return gestor.eliminar(id_factura)