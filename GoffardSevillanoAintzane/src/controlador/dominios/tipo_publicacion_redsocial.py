class TipoPublicacionRedSocial:
    def __init__(self, id_tipo_publicacion: int, id_red_social: int):
        self.id_tipo_publicacion = id_tipo_publicacion
        self.id_red_social = id_red_social

    @property
    def id_tipo_publicacion(self):
        return self._id_tipo_publicacion

    @id_tipo_publicacion.setter
    def id_tipo_publicacion(self, id_tipo_publicacion):
        self._id_tipo_publicacion = id_tipo_publicacion

    @property
    def id_red_social(self):
        return self._id_red_social

    @id_red_social.setter
    def id_red_social(self, id_red_social):
        self._id_red_social = id_red_social

    # @staticmethod
    # def crear(id_tipo_publicacion, id_red_social):
    #     return TipoPublicacionRedSocial(id_tipo_publicacion, id_red_social)

    def __repr__(self):
        return (f"TipoPublicacionRedSocial(id_tipo_publicacion={self.id_tipo_publicacion}, "
                f"id_red_social={self.id_red_social})")
