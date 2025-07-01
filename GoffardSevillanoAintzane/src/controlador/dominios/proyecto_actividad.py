class ProyectoActividad:
    def __init__(self, id_proyecto, id_actividad):
        self.id_proyecto = id_proyecto
        self.id_actividad = id_actividad

    @staticmethod
    def crear(id_proyecto, id_actividad):
        return ProyectoActividad(id_proyecto, id_actividad)

    def __str__(self):
        return f"Proyecto ID: {self.id_proyecto}, Actividad ID: {self.id_actividad}"
        self._proyecto_id = proyecto_id

    @property
    def actividad_id(self):
        return self._actividad_id

    @actividad_id.setter
    def actividad_id(self, actividad_id):
        self._actividad_id = actividad_id

