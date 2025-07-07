class Log_Sistema:
    def __init__(self, id_log_sistema, usuario_id, fecha=None, accion=None, descripcion=None, nivel=None):
        self._id_log_sistema = id_log_sistema
        self._usuario_id = usuario_id
        self._fecha = fecha
        self._accion = accion
        self._descripcion = descripcion
        self._nivel = nivel

    @property
    def id_log_sistema(self):
        return self._id_log_sistema

    @id_log_sistema.setter
    def id_log_sistema(self, id_log_sistema):
        self._id_log_sistema = id_log_sistema

    @property
    def usuario_id(self):
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, usuario_id):
        self._usuario_id = usuario_id

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def accion(self):
        return self._accion

    @accion.setter
    def accion(self, accion):
        self._accion = accion

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    # @staticmethod
    # def crear(id_log_sistema, usuario_id, fecha=None, accion=None, descripcion=None, nivel=None):
    #     return Log_Sistema(id_log_sistema, usuario_id, fecha, accion, descripcion, nivel)

    def __str__(self):
        return (
            f"ID: {self.id_log_sistema}, Usuario ID: {self.usuario_id}, Fecha: {self.fecha or 'N/A'}, "
            f"Acción: {self.accion or 'N/A'}, Descripción: {self.descripcion or 'N/A'}, "
            f"Nivel: {self.nivel or 'N/A'}"
        )