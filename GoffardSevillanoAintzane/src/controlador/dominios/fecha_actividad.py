class FechaActividad:
    def __init__(self, id_fecha, fecha):
        self._id_fecha = id_fecha
        self._fecha = fecha

    @property
    def id_fecha(self):
        return self._id_fecha

    @id_fecha.setter
    def id_fecha(self, id_fecha):
        self._id_fecha = id_fecha

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @staticmethod
    def crear(id_fecha, fecha):
        return FechaActividad(id_fecha, fecha)

    def __str__(self):
        return f"ID: {self.id_fecha}, Fecha: {self.fecha}"