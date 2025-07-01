class TipoPublicacionRedSocial:
    def __init__(self, id_tipo_publicacion: int, id_red_social: int):
        self.id_tipo_publicacion = id_tipo_publicacion
        self.id_red_social = id_red_social

    @staticmethod
    def crear(id_tipo_publicacion, id_red_social):
        return TipoPublicacionRedSocial(id_tipo_publicacion, id_red_social)

    def __repr__(self):
        return (f"TipoPublicacionRedSocial(id_tipo_publicacion={self.id_tipo_publicacion}, "
                f"id_red_social={self.id_red_social})")
