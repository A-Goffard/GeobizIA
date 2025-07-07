class PublicacionTag:
    def __init__(self, id_publicacion, id_tag):
        self._id_publicacion = id_publicacion
        self._id_tag = id_tag

    @property
    def id_publicacion(self):
        return self._id_publicacion

    @id_publicacion.setter
    def id_publicacion(self, value):
        self._id_publicacion = value

    @property
    def id_tag(self):
        return self._id_tag

    @id_tag.setter
    def id_tag(self, value):
        self._id_tag = value

    # @staticmethod
    # def crear(id_publicacion, id_tag):
    #     return PublicacionTag(id_publicacion, id_tag)

    def __str__(self):
        return f"Publicacion ID: {self.id_publicacion}, Tag ID: {self.id_tag}"
