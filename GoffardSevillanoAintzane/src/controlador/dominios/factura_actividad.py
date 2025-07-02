class FacturaActividad:
    def __init__(self, id_factura, id_actividad):
        self._id_factura = id_factura
        self._id_actividad = id_actividad

    @property
    def id_factura(self):
        return self._id_factura

    @id_factura.setter
    def id_factura(self, value):
        self._id_factura = value

    @property
    def id_actividad(self):
        return self._id_actividad

    @id_actividad.setter
    def id_actividad(self, value):
        self._id_actividad = value

    # @staticmethod
    # def crear(id_factura, id_actividad):
    #     return FacturaActividad(id_factura, id_actividad)

    def __str__(self):
        return f"ID Factura: {self.id_factura}, ID Actividad: {self.id_actividad}"
