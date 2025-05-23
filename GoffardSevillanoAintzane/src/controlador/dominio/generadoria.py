class GeneradorIA:
    def __init__(self, id, nombre, tipo_ia, configuraciones, empresa_id, plantillas, tags, temas_ambientales, ultima_generacion):
        self._id = id
        self._nombre = nombre
        self._tipo_ia = tipo_ia
        self._configuraciones = configuraciones
        self._empresa_id = empresa_id
        self._plantillas = plantillas
        self._tags = tags
        self._temas_ambientales = temas_ambientales
        self._ultima_generacion = ultima_generacion

    @staticmethod
    def crear_generador_ia(id, nombre, tipo_ia, configuraciones, empresa_id, plantillas, tags, temas_ambientales, ultima_generacion):
        return GeneradorIA(id, nombre, tipo_ia, configuraciones, empresa_id, plantillas, tags, temas_ambientales, ultima_generacion)

    @property
    def id(self): return self._id
    @id.setter
    def id(self, id): self._id = id

    @property
    def nombre(self): return self._nombre
    @nombre.setter
    def nombre(self, nombre): self._nombre = nombre

    @property
    def tipo_ia(self): return self._tipo_ia
    @tipo_ia.setter
    def tipo_ia(self, tipo_ia): self._tipo_ia = tipo_ia

    @property
    def configuraciones(self): return self._configuraciones
    @configuraciones.setter
    def configuraciones(self, configuraciones): self._configuraciones = configuraciones

    @property
    def empresa_id(self): return self._empresa_id
    @empresa_id.setter
    def empresa_id(self, empresa_id): self._empresa_id = empresa_id

    @property
    def plantillas(self): return self._plantillas
    @plantillas.setter
    def plantillas(self, plantillas): self._plantillas = plantillas

    @property
    def tags(self): return self._tags
    @tags.setter
    def tags(self, tags): self._tags = tags

    @property
    def temas_ambientales(self): return self._temas_ambientales
    @temas_ambientales.setter
    def temas_ambientales(self, temas_ambientales): self._temas_ambientales = temas_ambientales

    @property
    def ultima_generacion(self): return self._ultima_generacion
    @ultima_generacion.setter
    def ultima_generacion(self, ultima_generacion): self._ultima_generacion = ultima_generacion

    def __str__(self):
        return (
            f"ID: {self.id}, Nombre: {self.nombre}, Tipo IA: {self.tipo_ia}, "
            f"Configuraciones: {self.configuraciones}, Empresa ID: {self.empresa_id}, "
            f"Plantillas: {self.plantillas}, Tags: {self.tags}, Temas ambientales: {self.temas_ambientales}, "
            f"Última generación: {self.ultima_generacion}"
        )
