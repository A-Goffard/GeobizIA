class RecursoMultimedia:
    def __init__(self, id_recurso_multimedia, tipo, titulo, fecha_subida, autor, relaciones):
        self._id_recurso_multimedia = id_recurso_multimedia
        self._tipo = tipo
        self._titulo = titulo
        self._fecha_subida = fecha_subida
        self._autor = autor
        self._relaciones = relaciones

    @property
    def id_recurso_multimedia(self):
        return self._id_recurso_multimedia

    @id_recurso_multimedia.setter
    def id_recurso_multimedia(self, id_recurso_multimedia):
        self._id_recurso_multimedia = id_recurso_multimedia

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def fecha_subida(self):
        return self._fecha_subida

    @fecha_subida.setter
    def fecha_subida(self, fecha_subida):
        self._fecha_subida = fecha_subida

    @staticmethod
    def crear_recurso_multimedia(id_recurso_multimedia, tipo, url, descripcion, fecha_creacion, etiquetas):
        return RecursoMultimedia(
            id_recurso_multimedia=id_recurso_multimedia,
            tipo=tipo,
            url=url,
            descripcion=descripcion,
            fecha_creacion=fecha_creacion,
            etiquetas=etiquetas
        )

    def __str__(self):
        return (
            f"ID: {self.id_recurso_multimedia}, Tipo: {self.tipo}, Título: {self.titulo}, "
            f"Fecha subida: {self.fecha_subida}, Autor: {self._autor}, Relaciones: {self._relaciones}"
        )
