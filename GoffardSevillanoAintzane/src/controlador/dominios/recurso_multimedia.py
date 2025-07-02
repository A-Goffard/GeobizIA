class RecursoMultimedia:
    def __init__(self, id_recurso_multimedia, tipo, titulo, fecha_subida, autor):
        self._id_recurso_multimedia = id_recurso_multimedia
        self._tipo = tipo
        self._titulo = titulo
        self._fecha_subida = fecha_subida
        self._autor = autor

    @property
    def id_recurso_multimedia(self):
        return self._id_recurso_multimedia

    @id_recurso_multimedia.setter
    def id_recurso_multimedia(self, value):
        self._id_recurso_multimedia = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def fecha_subida(self):
        return self._fecha_subida

    @fecha_subida.setter
    def fecha_subida(self, value):
        self._fecha_subida = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    # @staticmethod
    # def crear(id_recurso_multimedia, tipo, titulo, fecha_subida, autor):
    #     return RecursoMultimedia(id_recurso_multimedia, tipo, titulo, fecha_subida, autor)

    def __str__(self):
        return f"ID: {self.id_recurso_multimedia}, Título: {self.titulo}, Tipo: {self.tipo}, Fecha: {self.fecha_subida}, Autor: {self.autor}"
