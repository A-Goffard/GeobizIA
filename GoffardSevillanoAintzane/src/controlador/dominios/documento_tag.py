class DocumentoTag:
    def __init__(self, id_documento: int, id_tag: int):
        self._id_documento = id_documento
        self._id_tag = id_tag

    @property
    def id_documento(self):
        return self._id_documento

    @property
    def id_tag(self):
        return self._id_tag

    def __eq__(self, other):
        if isinstance(other, DocumentoTag):
            return (self.id_documento == other.id_documento and
                    self.id_tag == other.id_tag)
        return False

    def __hash__(self):
        return hash((self.id_documento, self.id_tag))

    def __str__(self):
        return f"DocumentoTag(Documento ID={self.id_documento}, Tag ID={self.id_tag})"
