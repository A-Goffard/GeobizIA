class Programacion:
    def __init__(self, id, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable):
        self._id = id
        self._publicacion_id = publicacion_id
        self._red_social_id = red_social_id
        self._fecha_programada = fecha_programada
        self._estado = estado
        self._notificaciones = notificaciones
        self._responsable = responsable

    @staticmethod
    def crear_programacion(id, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable):
        return Programacion(id, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable)

    @property
    def id(self): return self._id
    @id.setter
    def id(self, id): self._id = id

    @property
    def publicacion_id(self): return self._publicacion_id
    @publicacion_id.setter
    def publicacion_id(self, publicacion_id): self._publicacion_id = publicacion_id

    @property
    def red_social_id(self): return self._red_social_id
    @red_social_id.setter
    def red_social_id(self, red_social_id): self._red_social_id = red_social_id

    @property
    def fecha_programada(self): return self._fecha_programada
    @fecha_programada.setter
    def fecha_programada(self, fecha_programada): self._fecha_programada = fecha_programada

    @property
    def estado(self): return self._estado
    @estado.setter
    def estado(self, estado): self._estado = estado

    @property
    def notificaciones(self): return self._notificaciones
    @notificaciones.setter
    def notificaciones(self, notificaciones): self._notificaciones = notificaciones

    @property
    def responsable(self): return self._responsable
    @responsable.setter
    def responsable(self, responsable): self._responsable = responsable

    def __str__(self):
        return (
            f"ID: {self.id}, Publicación ID: {self.publicacion_id}, Red social ID: {self.red_social_id}, "
            f"Fecha programada: {self.fecha_programada}, Estado: {self.estado}, "
            f"Notificaciones: {self.notificaciones}, Responsable: {self.responsable}"
        )
