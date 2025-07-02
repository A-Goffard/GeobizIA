class PlantillaTipoPublicacion:
    def __init__(self, id_plantilla: int, id_tipo_publicacion: int):
        self.id_plantilla = id_plantilla
        self.id_tipo_publicacion = id_tipo_publicacion

    @property
    def id_plantilla(self):
        return self._id_plantilla
    
    @id_plantilla.setter
    def id_plantilla(self, value):
        self._id_plantilla = value

    @property
    def id_tipo_publicacion(self):
        return self._id_tipo_publicacion

    @id_tipo_publicacion.setter
    def id_tipo_publicacion(self, value):
        self._id_tipo_publicacion = value

    def __repr__(self):
        return (f"PlantillaTipoPublicacion(id_plantilla={self.id_plantilla}, "
                f"id_tipo_publicacion={self.id_tipo_publicacion})")
