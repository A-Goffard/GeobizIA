class Documento:
    def __init__(self, id, titulo, descripcion, fecha_subida, tipo, tematica):
        self._id = id
        self._titulo = titulo
        self._descripcion = descripcion
        self._fecha_subida = fecha_subida
        self._tipo = tipo
        self._tematica = tematica

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
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def fecha_subida(self):
        return self._fecha_subida

    @fecha_subida.setter
    def fecha_subida(self, fecha_subida):
        self._fecha_subida = fecha_subida

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def tematica(self):
        return self._tematica

    @tematica.setter
    def tematica(self, tematica):
        self._tematica = tematica

    @staticmethod
    def crear_documento(id, titulo, descripcion, fecha_subida, tipo, tematica):
        return Documento(
            id=id,
            titulo=titulo,
            descripcion=descripcion,
            fecha_subida=fecha_subida,
            tipo=tipo,
            tematica=tematica
        )

    def __str__(self):
        return (
            f"ID: {self.id}, Título: {self.titulo}, Descripción: {self.descripcion}, "
            f"Fecha subida: {self.fecha_subida}, Tipo: {self.tipo}, Temática: {self.tematica}"
        )
