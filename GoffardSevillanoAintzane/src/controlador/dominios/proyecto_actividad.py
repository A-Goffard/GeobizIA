class ProyectoActividad:
    def __init__(self, proyecto_id, actividad_id):
        self._proyecto_id = proyecto_id
        self._actividad_id = actividad_id

    @property
    def proyecto_id(self):
        return self._proyecto_id

    @proyecto_id.setter
    def proyecto_id(self, proyecto_id):
        self._proyecto_id = proyecto_id

    @property
    def actividad_id(self):
        return self._actividad_id

    @actividad_id.setter
    def actividad_id(self, actividad_id):
        self._actividad_id = actividad_id

    @staticmethod
    def crear(proyecto_id, actividad_id):
        return ProyectoActividad(proyecto_id, actividad_id)

    def __str__(self):
        return f"Proyecto ID: {self.proyecto_id}, Actividad ID: {self.actividad_id}"
