class ActividadEvento:
    def __init__(self, id_actividad, id_evento):
        self._id_actividad = id_actividad
        self._id_evento = id_evento

    @property
    def id_actividad(self):
        return self._id_actividad

    @id_actividad.setter
    def id_actividad(self, value):
        self._id_actividad = value

    @property
    def id_evento(self):
        return self._id_evento

    @id_evento.setter
    def id_evento(self, value):
        self._id_evento = value

    @staticmethod
    def crear(id_actividad, id_evento):
        return ActividadEvento(id_actividad, id_evento)

    def __str__(self):
        return f"ID Actividad: {self.id_actividad}, ID Evento: {self.id_evento}"
 