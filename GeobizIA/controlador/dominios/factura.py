class Factura:
    def __init__(self, id_factura, id_cliente, tipo=None, nombre=None, direccion=None, nif=None, fecha_facturacion=None, fecha_vencimiento=None, concepto=None, responsable=None, iva=None, coste_total=None, base_imponible=None, numero_factura=None, tipo_pago=None, irpf=None):
        self._id_factura = id_factura
        self._id_cliente = id_cliente
        self._tipo = tipo
        self._nombre = nombre
        self._direccion = direccion
        self._nif = nif
        self._fecha_facturacion = fecha_facturacion
        self._fecha_vencimiento = fecha_vencimiento
        self._concepto = concepto
        self._responsable = responsable
        self._iva = iva
        self._coste_total = coste_total
        self._base_imponible = base_imponible
        self._numero_factura = numero_factura
        self._tipo_pago = tipo_pago
        self._irpf = irpf

    @property
    def id_factura(self):
        return self._id_factura

    @id_factura.setter
    def id_factura(self, id_factura):
        self._id_factura = id_factura

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def nif(self):
        return self._nif

    @nif.setter
    def nif(self, nif):
        self._nif = nif

    @property
    def fecha_facturacion(self):
        return self._fecha_facturacion

    @fecha_facturacion.setter
    def fecha_facturacion(self, fecha_facturacion):
        self._fecha_facturacion = fecha_facturacion

    @property
    def fecha_vencimiento(self):
        return self._fecha_vencimiento

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, fecha_vencimiento):
        self._fecha_vencimiento = fecha_vencimiento

    @property
    def concepto(self):
        return self._concepto

    @concepto.setter
    def concepto(self, concepto):
        self._concepto = concepto

    @property
    def responsable(self):
        return self._responsable

    @responsable.setter
    def responsable(self, responsable):
        self._responsable = responsable

    @property
    def iva(self):
        return self._iva

    @iva.setter
    def iva(self, iva):
        self._iva = iva

    @property
    def coste_total(self):
        return self._coste_total

    @coste_total.setter
    def coste_total(self, coste_total):
        self._coste_total = coste_total

    @property
    def base_imponible(self):
        return self._base_imponible

    @base_imponible.setter
    def base_imponible(self, base_imponible):
        self._base_imponible = base_imponible

    @property
    def numero_factura(self):
        return self._numero_factura

    @numero_factura.setter
    def numero_factura(self, numero_factura):
        self._numero_factura = numero_factura

    @property
    def tipo_pago(self):
        return self._tipo_pago

    @tipo_pago.setter
    def tipo_pago(self, tipo_pago):
        self._tipo_pago = tipo_pago

    @property
    def irpf(self):
        return self._irpf

    @irpf.setter
    def irpf(self, irpf):
        self._irpf = irpf

    def to_dict(self):
        """Convierte la factura a un diccionario para serialización JSON"""
        return {
            'id_factura': self.id_factura,
            'id_cliente': self.id_cliente,
            'tipo': self.tipo,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'nif': self.nif,
            'fecha_facturacion': self.fecha_facturacion,
            'fecha_vencimiento': self.fecha_vencimiento,
            'concepto': self.concepto,
            'responsable': self.responsable,
            'iva': self.iva,
            'coste_total': self.coste_total,
            'base_imponible': self.base_imponible,
            'numero_factura': self.numero_factura,
            'tipo_pago': self.tipo_pago,
            'irpf': self.irpf
        }

    def __str__(self):
        return (
            f"ID: {self.id_factura}, ID Cliente: {self.id_cliente}, Tipo: {self.tipo or 'N/A'}, "
            f"Nombre: {self.nombre or 'N/A'}, Dirección: {self.direccion or 'N/A'}, NIF: {self.nif or 'N/A'}, "
            f"Fecha Facturación: {self.fecha_facturacion or 'N/A'}, Fecha Vencimiento: {self.fecha_vencimiento or 'N/A'}, "
            f"Concepto: {self.concepto or 'N/A'}, Responsable: {self.responsable or 'N/A'}, "
            f"IVA: {self.iva or 'N/A'}, Coste Total: {self.coste_total or 'N/A'}, "
            f"Base Imponible: {self.base_imponible or 'N/A'}, Número Factura: {self.numero_factura or 'N/A'}, "
            f"Tipo Pago: {self.tipo_pago or 'N/A'}, IRPF: {self.irpf or 'N/A'}"
        )