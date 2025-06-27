class Publicacion:
    def __init__(self, id_publicacion, id_generador_IA, id_tipo_publicacion, contenido=None, fecha_creacion=None):
        self._id_publicacion = id_publicacion
        self._id_generador_IA = id_generador_IA
        self._id_tipo_publicacion = id_tipo_publicacion
        self._contenido = contenido
        self._fecha_creacion = fecha_creacion

    @property
    def id_publicacion(self):
        return self._id_publicacion

    @id_publicacion.setter
    def id_publicacion(self, id_publicacion):
        self._id_publicacion = id_publicacion

    @property
    def id_generador_IA(self):
        return self._id_generador_IA

    @id_generador_IA.setter
    def id_generador_IA(self, id_generador_IA):
        self._id_generador_IA = id_generador_IA

    @property
    def id_tipo_publicacion(self):
        return self._id_tipo_publicacion

    @id_tipo_publicacion.setter
    def id_tipo_publicacion(self, id_tipo_publicacion):
        self._id_tipo_publicacion = id_tipo_publicacion

    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, contenido):
        self._contenido = contenido

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion):
        self._fecha_creacion = fecha_creacion

    @staticmethod
    def crear(id_publicacion, id_generador_IA, id_tipo_publicacion, contenido=None, fecha_creacion=None):
        return Publicacion(id_publicacion, id_generador_IA, id_tipo_publicacion, contenido, fecha_creacion)

    def __str__(self):
        return f"ID: {self.id_publicacion}, ID Generador IA: {self.id_generador_IA}, ID Tipo Publicación: {self.id_tipo_publicacion}, Contenido: {self.contenido or 'N/A'}, Fecha Creación: {self.fecha_creacion or 'N/A'}"