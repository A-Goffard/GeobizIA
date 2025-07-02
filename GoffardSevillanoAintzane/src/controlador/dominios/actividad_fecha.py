class ActividadFecha:
    def __init__(self, id_actividad, id_fecha):
        self._id_actividad = id_actividad
        self._id_fecha = id_fecha

    @property
    def id_actividad(self):
        return self._id_actividad

    @id_actividad.setter
    def id_actividad(self, value):
        self._id_actividad = value

    @property
    def id_fecha(self):
        return self._id_fecha

    @id_fecha.setter
    def id_fecha(self, value):
        self._id_fecha = value

    @staticmethod
    def crear(id_actividad, id_fecha):
        return ActividadFecha(id_actividad, id_fecha)

    def __str__(self):
        return f"ID Actividad: {self.id_actividad}, ID Fecha: {self.id_fecha}"
    def fecha(self, value):
        self._fecha = value
