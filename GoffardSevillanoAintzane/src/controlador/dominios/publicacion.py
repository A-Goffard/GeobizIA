class Publicacion:
    def __init__(self, id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia=False, id_generador_ia=None, feedback_empresa=None):
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

    @property
    def id_publicacion(self):
        return self._id_publicacion

    @id_publicacion.setter
    def id_publicacion(self, id_publicacion):
        self._id_publicacion = id_publicacion

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, contenido):
        self._contenido = contenido

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion):
        self._fecha_creacion = fecha_creacion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags

    @property
    def palabras_clave(self):
        return self._palabras_clave

    @palabras_clave.setter
    def palabras_clave(self, palabras_clave):
        self._palabras_clave = palabras_clave

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

    @staticmethod
    def crear_publicacion(id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia=False, id_generador_ia=None, feedback_empresa=None):
        return Publicacion(
            id_publicacion=id_publicacion,
            titulo=titulo,
            contenido=contenido,
            autor=autor,
            fecha_creacion=fecha_creacion,
            estado=estado,
            tags=tags,
            palabras_clave=palabras_clave,
            generada_por_ia=generada_por_ia,
            id_generador_ia=id_generador_ia,
            feedback_empresa=feedback_empresa
        )

    def __str__(self):
        return (
            f"ID: {self.id_publicacion}, Título: {self.titulo}, Contenido: {self.contenido}, "
            f"Autor: {self.autor}, Fecha creación: {self.fecha_creacion}, Estado: {self.estado}, "
            f"Tags: {self.tags}, Palabras clave: {self.palabras_clave}, Generada por IA: {self.generada_por_ia}, "
            f"ID Generador IA: {self.id_generador_ia}, Feedback empresa: {self.feedback_empresa}"
        )
