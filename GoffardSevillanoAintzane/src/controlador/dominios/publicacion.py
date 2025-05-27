class Publicacion:
    def __init__(self, id, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave):
        self._id = id
        self._titulo = titulo
        self._contenido = contenido
        self._autor = autor
        self._fecha_creacion = fecha_creacion
        self._estado = estado
        self._tags = tags
        self._palabras_clave = palabras_clave

    @property
    def id(self):
        return self._id

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

    @staticmethod
    def crear_publicacion(id, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave):
        return Publicacion(
            id=id,
            titulo=titulo,
            contenido=contenido,
            autor=autor,
            fecha_creacion=fecha_creacion,
            estado=estado,
            tags=tags,
            palabras_clave=palabras_clave
        )

    def __str__(self):
        return (
            f"ID: {self.id}, Título: {self.titulo}, Contenido: {self.contenido}, "
            f"Autor: {self.autor}, Fecha creación: {self.fecha_creacion}, Estado: {self.estado}, "
            f"Tags: {self.tags}, Palabras clave: {self.palabras_clave}"
        )
