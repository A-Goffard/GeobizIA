class ActividadEvento:
    def __init__(self, id_actividad_evento, actividad_id, evento_id):
        self._id_actividad_evento = id_actividad_evento
        self._actividad_id = actividad_id
        self._evento_id = evento_id

    @property
    def id_actividad_evento(self):
        return self._id_actividad_evento

    @id_actividad_evento.setter
    def id_actividad_evento(self, value):
        self._id_actividad_evento = value

    @property
    def actividad_id(self):
        return self._actividad_id

    @actividad_id.setter
    def actividad_id(self, value):
        self._actividad_id = value

    @property
    def evento_id(self):
        return self._evento_id

    @evento_id.setter
    def evento_id(self, value):
        self._evento_id = value

    @staticmethod
    def crear(id_actividad_evento, actividad_id, evento_id):
        return ActividadEvento(id_actividad_evento, actividad_id, evento_id)

    def __str__(self):
        return f"ID: {self.id_actividad_evento}, Actividad ID: {self.actividad_id}, Evento ID: {self.evento_id}"
