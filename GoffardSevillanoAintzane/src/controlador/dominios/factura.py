class Factura:
    def __init__(self, id, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf):
        self._id = id
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

    @staticmethod
    def crear_factura(id, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf):
        return Factura(
            id=id,
            tipo=tipo,
            nombre=nombre,
            direccion=direccion,
            nif=nif,
            fecha_facturacion=fecha_facturacion,
            fecha_vencimiento=fecha_vencimiento,
            concepto=concepto,
            responsable=responsable,
            iva=iva,
            coste_total=coste_total,
            base_imponible=base_imponible,
            numero_factura=numero_factura,
            tipo_pago=tipo_pago,
            irpf=irpf
        )

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

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

    def __str__(self):
        return (
            f"ID: {self.id}, Tipo: {self.tipo}, Nombre: {self.nombre}, Dirección: {self.direccion}, "
            f"NIF: {self.nif}, Fecha facturación: {self.fecha_facturacion}, Fecha vencimiento: {self.fecha_vencimiento}, "
            f"Concepto: {self.concepto}, Responsable: {self.responsable}, IVA: {self.iva}, "
            f"Coste total: {self.coste_total}, Base imponible: {self.base_imponible}, "
            f"Número factura: {self.numero_factura}, Tipo pago: {self.tipo_pago}, IRPF: {self.irpf}"
        )