class Programacion:
    def __init__(self, id_programacion, fecha, hora_inicio, hora_fin, actividad, responsable, estado):
        self._id_programacion = id_programacion
        self._fecha = fecha
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin
        self._actividad = actividad
        self._responsable = responsable
        self._estado = estado

    @property
    def id_programacion(self):
        return self._id_programacion

    @id_programacion.setter
    def id_programacion(self, value):
        self._id_programacion = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def hora_inicio(self):
        return self._hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, value):
        self._hora_inicio = value

    @property
    def hora_fin(self):
        return self._hora_fin

    @hora_fin.setter
    def hora_fin(self, value):
        self._hora_fin = value

    @property
    def actividad(self):
        return self._actividad

    @actividad.setter
    def actividad(self, value):
        self._actividad = value

    @property
    def responsable(self):
        return self._responsable

    @responsable.setter
    def responsable(self, value):
        self._responsable = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @staticmethod
    def crear(id_programacion, fecha, hora_inicio, hora_fin, actividad, responsable, estado):
        return Programacion(id_programacion, fecha, hora_inicio, hora_fin, actividad, responsable, estado)

    def __str__(self):
        return f"{self.fecha} {self.hora_inicio}-{self.hora_fin} | Actividad: {self.actividad} | Responsable: {self.responsable} | Estado: {self.estado}"
