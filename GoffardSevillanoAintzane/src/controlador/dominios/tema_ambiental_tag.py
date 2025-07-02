class TemaAmbientalTag:
    def __init__(self, id_tema_ambiental, id_tag):
        self.id_tema_ambiental = id_tema_ambiental
        self.id_tag = id_tag

    @property
    def id_tema_ambiental(self):
        return self._id_tema_ambiental
    @id_tema_ambiental.setter
    def id_tema_ambiental(self, id_tema_ambiental):
        self._id_tema_ambiental = id_tema_ambiental
        
    @property
    def id_tag(self):
        return self._id_tag

    @id_tag.setter
    def id_tag(self, id_tag):
        self._id_tag = id_tag

    # @staticmethod
    # def crear(id_tema_ambiental, id_tag):
    #     return TemaAmbientalTag(id_tema_ambiental, id_tag)

    def __repr__(self):
        return f"TemaAmbientalTag(id_tema_ambiental={self.id_tema_ambiental}, id_tag={self.id_tag})"
        return self._id_tag

    def __eq__(self, other):
        if isinstance(other, TemaAmbientalTag):
            return (self.id_tema_ambiental == other.id_tema_ambiental and
                    self.id_tag == other.id_tag)
        return False

    def __hash__(self):
        return hash((self.id_tema_ambiental, self.id_tag))

    def __str__(self):
        return f"TemaAmbientalTag(TemaAmbiental ID={self.id_tema_ambiental}, Tag ID={self.id_tag})"
