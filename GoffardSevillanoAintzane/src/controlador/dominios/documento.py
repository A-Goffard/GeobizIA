class Documento:
    def __init__(self, id_documento, titulo=None, descripcion=None, fecha_subida=None, tipo=None, tematica=None):
        self._id_documento = id_documento
        self._titulo = titulo
        self._descripcion = descripcion
        self._fecha_subida = fecha_subida
        self._tipo = tipo
        self._tematica = tematica

    @property
    def id_documento(self):
        return self._id_documento

    @id_documento.setter
    def id_documento(self, id_documento):
        self._id_documento = id_documento

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

    # @staticmethod
    # def crear(id_documento, titulo=None, descripcion=None, fecha_subida=None, tipo=None, tematica=None):
    #     return Documento(id_documento, titulo, descripcion, fecha_subida, tipo, tematica)

    def __str__(self):
        return (
            f"ID: {self.id_documento}, Título: {self.titulo or 'N/A'}, Descripción: {self.descripcion or 'N/A'}, "
            f"Fecha Subida: {self.fecha_subida or 'N/A'}, Tipo: {self.tipo or 'N/A'}, Temática: {self.tematica or 'N/A'}"
        )