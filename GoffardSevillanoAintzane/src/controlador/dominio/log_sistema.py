class LogSistema:
    def __init__(self, id, fecha, usuario_id, accion, descripcion, nivel="INFO"):
        self._id = id
        self._fecha = fecha
        self._usuario_id = usuario_id
        self._accion = accion
        self._descripcion = descripcion
        self._nivel = nivel

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def usuario_id(self):
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, value):
        self._usuario_id = value

    @property
    def accion(self):
        return self._accion

    @accion.setter
    def accion(self, value):
        self._accion = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, value):
        self._nivel = value

    def __str__(self):
        return (
            f"[{self.nivel}] {self.fecha} - Usuario: {self.usuario_id} - Acción: {self.accion} - {self.descripcion}"
        )