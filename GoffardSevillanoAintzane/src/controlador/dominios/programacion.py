class Programacion:
    def __init__(self, id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable):
        self._id_programacion = id_programacion
        self._publicacion_id = publicacion_id
        self._red_social_id = red_social_id
        self._fecha_programada = fecha_programada
        self._estado = estado
        self._notificaciones = notificaciones
        self._responsable = responsable

    # @staticmethod
    # def crear(id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable):
    #     return Programacion(id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable)

    @property
    def id_programacion(self):
        return self._id_programacion

    @id_programacion.setter
    def id_programacion(self, value):
        self._id_programacion = value

    @property
    def publicacion_id(self):
        return self._publicacion_id

    @publicacion_id.setter
    def publicacion_id(self, value):
        self._publicacion_id = value

    @property
    def red_social_id(self):
        return self._red_social_id

    @red_social_id.setter
    def red_social_id(self, value):
        self._red_social_id = value

    @property
    def fecha_programada(self):
        return self._fecha_programada

    @fecha_programada.setter
    def fecha_programada(self, value):
        self._fecha_programada = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def notificaciones(self):
        return self._notificaciones

    @notificaciones.setter
    def notificaciones(self, value):
        self._notificaciones = value

    @property
    def responsable(self):
        return self._responsable

    @responsable.setter
    def responsable(self, value):
        self._responsable = value

    def __str__(self):
        return (
            f"ID: {self.id_programacion} | Publicación: {self.publicacion_id} | Red Social: {self.red_social_id} | "
            f"Fecha: {self.fecha_programada} | Estado: {self.estado} | Notificaciones: {self.notificaciones} | Responsable: {self.responsable}"
        )
