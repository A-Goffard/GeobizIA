class FacturaActividad:
    def __init__(self, id_factura_actividad, actividad_id, factura_id, monto, fecha):
        self._id_factura_actividad = id_factura_actividad
        self._actividad_id = actividad_id
        self._factura_id = factura_id
        self._monto = monto
        self._fecha = fecha

    @property
    def id_factura_actividad(self):
        return self._id_factura_actividad

    @id_factura_actividad.setter
    def id_factura_actividad(self, value):
        self._id_factura_actividad = value

    @property
    def actividad_id(self):
        return self._actividad_id

    @actividad_id.setter
    def actividad_id(self, value):
        self._actividad_id = value

    @property
    def factura_id(self):
        return self._factura_id

    @factura_id.setter
    def factura_id(self, value):
        self._factura_id = value

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, value):
        self._monto = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @staticmethod
    def crear(id_factura_actividad, actividad_id, factura_id, monto, fecha):
        return FacturaActividad(id_factura_actividad, actividad_id, factura_id, monto, fecha)

    def __str__(self):
        return f"ID: {self.id_factura_actividad}, Actividad ID: {self.actividad_id}, Factura ID: {self.factura_id}, Monto: {self.monto}, Fecha: {self.fecha}"
