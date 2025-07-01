class Publicacion:
    def __init__(
        self,
        id_publicacion,
        titulo,
        contenido,
        autor,
        fecha_creacion,
        estado,
        tags,
        palabras_clave,
        generada_por_ia,
        id_generador_ia,
        feedback_empresa,
        id_tipo_publicacion,
        id_plantilla
    ):
        self._id_publicacion = id_publicacion
        self._titulo = titulo
        self._contenido = contenido
        self._autor = autor
        self._fecha_creacion = fecha_creacion
        self._estado = estado
        self._tags = tags
        self._palabras_clave = palabras_clave
        self._generada_por_ia = generada_por_ia
        self._id_generador_ia = id_generador_ia
        self._feedback_empresa = feedback_empresa
        self._id_tipo_publicacion = id_tipo_publicacion
        self._id_plantilla = id_plantilla

    @property
    def id_publicacion(self):
        return self._id_publicacion

    @id_publicacion.setter
    def id_publicacion(self, value):
        self._id_publicacion = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, value):
        self._contenido = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, value):
        self._fecha_creacion = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

    @property
    def palabras_clave(self):
        return self._palabras_clave

    @palabras_clave.setter
    def palabras_clave(self, value):
        self._palabras_clave = value

    @property
    def generada_por_ia(self):
        return self._generada_por_ia

    @generada_por_ia.setter
    def generada_por_ia(self, value):
        self._generada_por_ia = value

    @property
    def id_generador_ia(self):
        return self._id_generador_ia

    @id_generador_ia.setter
    def id_generador_ia(self, value):
        self._id_generador_ia = value

    @property
    def feedback_empresa(self):
        return self._feedback_empresa

    @feedback_empresa.setter
    def feedback_empresa(self, value):
        self._feedback_empresa = value

    @property
    def id_tipo_publicacion(self):
        return self._id_tipo_publicacion

    @id_tipo_publicacion.setter
    def id_tipo_publicacion(self, value):
        self._id_tipo_publicacion = value

    @property
    def id_plantilla(self):
        return self._id_plantilla

    @id_plantilla.setter
    def id_plantilla(self, value):
        self._id_plantilla = value

    @staticmethod
    def crear(
        id_publicacion,
        titulo,
        contenido,
        autor,
        fecha_creacion,
        estado,
        tags,
        palabras_clave,
        generada_por_ia,
        id_generador_ia,
        feedback_empresa,
        id_tipo_publicacion,
        id_plantilla
    ):
        return Publicacion(
            id_publicacion,
            titulo,
            contenido,
            autor,
            fecha_creacion,
            estado,
            tags,
            palabras_clave,
            generada_por_ia,
            id_generador_ia,
            feedback_empresa,
            id_tipo_publicacion,
            id_plantilla
        )