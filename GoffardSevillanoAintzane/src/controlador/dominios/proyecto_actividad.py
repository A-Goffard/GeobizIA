class ProyectoActividad:
    def __init__(self, id_proyecto, id_actividad):
        self._id_proyecto = id_proyecto
        self._id_actividad = id_actividad

    @property
    def id_proyecto(self):
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, value):
        self._id_proyecto = value

    @property
    def id_actividad(self):
        return self._id_actividad

    @id_actividad.setter
    def id_actividad(self, value):
        self._id_actividad = value

    def __str__(self):
        return f"Proyecto ID: {self.id_proyecto}, Actividad ID: {self.id_actividad}"