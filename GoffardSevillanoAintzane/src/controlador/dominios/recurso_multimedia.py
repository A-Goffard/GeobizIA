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

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def relaciones(self):
        return self._relaciones

    @relaciones.setter
    def relaciones(self, relaciones):
        self._relaciones = relaciones

    @staticmethod
    def crear_recurso_multimedia(id_recurso_multimedia, tipo, titulo, fecha_subida, autor, relaciones):
        return RecursoMultimedia(
            id_recurso_multimedia=id_recurso_multimedia,
            tipo=tipo,
            titulo=titulo,
            fecha_subida=fecha_subida,
            autor=autor,
            relaciones=relaciones
        )

    def __str__(self):
        return (
            f"ID: {self.id_recurso_multimedia}, Tipo: {self.tipo}, Título: {self.titulo}, "
            f"Fecha subida: {self.fecha_subida}, Autor: {self.autor}, Relaciones: {self.relaciones}"
        )
