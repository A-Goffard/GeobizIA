class DocumentoTag:
    def __init__(self, id_documento: int, id_tag: int):
        self._id_documento = id_documento
        self._id_tag = id_tag

    @property
    def id_documento(self):
        return self._id_documento

    @id_documento.setter
    def id_documento(self, value):
        self._id_documento = value

    @property
    def id_tag(self):
        return self._id_tag

    @id_tag.setter
    def id_tag(self, value):
        self._id_tag = value

    # @staticmethod
    # def crear(id_documento, id_tag):
    #     return DocumentoTag(id_documento, id_tag)

    def __str__(self):
        return f"ID Documento: {self.id_documento}, ID Tag: {self.id_tag}"
