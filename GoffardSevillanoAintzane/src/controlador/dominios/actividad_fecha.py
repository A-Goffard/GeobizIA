class ActividadFecha:
    def __init__(self, id_actividad_fecha, actividad_id, fecha):
        self._id_actividad_fecha = id_actividad_fecha
        self._actividad_id = actividad_id
        self._fecha = fecha

    @property
    def id_actividad_fecha(self):
        return self._id_actividad_fecha

    @id_actividad_fecha.setter
    def id_actividad_fecha(self, value):
        self._id_actividad_fecha = value

    @property
    def actividad_id(self):
        return self._actividad_id

    @actividad_id.setter
    def actividad_id(self, value):
        self._actividad_id = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @staticmethod
    def crear(id_actividad_fecha, actividad_id, fecha):
        return ActividadFecha(id_actividad_fecha, actividad_id, fecha)

    def __str__(self):
        return f"ID: {self.id_actividad_fecha}, Actividad ID: {self.actividad_id}, Fecha: {self.fecha}"
