class ProyectoActividad:
    def __init__(self, id_proyecto, id_actividad):
        self._id_proyecto = id_proyecto
        self._id_actividad = id_actividad

    # @staticmethod
    # def crear(id_proyecto, id_actividad):
    #     return ProyectoActividad(id_proyecto, id_actividad)

    @property
    def actividad_id(self):
        return self._actividad_id

    @actividad_id.setter
    def actividad_id(self, actividad_id):
        self._actividad_id = actividad_id

    def __str__(self):
        return f"Proyecto ID: {self.id_proyecto}, Actividad ID: {self.id_actividad}"