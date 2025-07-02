class Tag:
    def __init__(self, id_tag, palabra_clave, categoria, frecuencia_uso=0):
        self._id_tag = id_tag
        self._palabra_clave = palabra_clave
        self._categoria = categoria
        self._frecuencia_uso = frecuencia_uso

    @property
    def id_tag(self):
        return self._id_tag

    @id_tag.setter
    def id_tag(self, value):
        self._id_tag = value

    @property
    def palabra_clave(self):
        return self._palabra_clave

    @palabra_clave.setter
    def palabra_clave(self, value):
        self._palabra_clave = value

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def frecuencia_uso(self):
        return self._frecuencia_uso

    @frecuencia_uso.setter
    def frecuencia_uso(self, value):
        self._frecuencia_uso = value

    @staticmethod
    def crear(id_tag, palabra_clave, categoria, frecuencia_uso=0):
        return Tag(id_tag, palabra_clave, categoria, frecuencia_uso)

    def __str__(self):
        return f"ID: {self.id_tag}, Palabra Clave: {self.palabra_clave}, Categoría: {self.categoria}, Frecuencia: {self.frecuencia_uso}"
