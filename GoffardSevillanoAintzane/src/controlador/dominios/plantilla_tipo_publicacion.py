class PlantillaTipoPublicacion:
    def __init__(self, id_plantilla: int, id_tipo_publicacion: int):
        self.id_plantilla = id_plantilla
        self.id_tipo_publicacion = id_tipo_publicacion

    def __repr__(self):
        return (f"PlantillaTipoPublicacion(id_plantilla={self.id_plantilla}, "
                f"id_tipo_publicacion={self.id_tipo_publicacion})")
