class Tag:
    def __init__(self, id_tag, palabra_clave, categoria, frecuencia_uso):
        self._id_tag = id_tag
        self._palabra_clave = palabra_clave
        self._categoria = categoria
        self._frecuencia_uso = frecuencia_uso

    @staticmethod
    def crear_tag(id_tag, palabra_clave, categoria, frecuencia_uso):
        return Tag(id_tag, palabra_clave, categoria, frecuencia_uso)

    @property
    def id_tag(self): return self._id_tag
    @id_tag.setter
    def id_tag(self, id_tag): self._id_tag = id_tag

    @property
    def palabra_clave(self): return self._palabra_clave
    @palabra_clave.setter
    def palabra_clave(self, palabra_clave): self._palabra_clave = palabra_clave

    @property
    def categoria(self): return self._categoria
    @categoria.setter
    def categoria(self, categoria): self._categoria = categoria

    @property
    def frecuencia_uso(self): return self._frecuencia_uso
    @frecuencia_uso.setter
    def frecuencia_uso(self, frecuencia_uso): self._frecuencia_uso = frecuencia_uso

    def __str__(self):
        return (
            f"ID: {self.id_tag}, Palabra clave: {self.palabra_clave}, "
            f"Categoría: {self.categoria}, Frecuencia de uso: {self.frecuencia_uso}"
        )
    @frecuencia_uso.setter
    def frecuencia_uso(self, frecuencia_uso):
        self._frecuencia_uso = frecuencia_uso

    @staticmethod
    def crear_tag(id_tag, palabra_clave, categoria, frecuencia_uso):
        return Tag(
            id_tag=id_tag,
            palabra_clave=palabra_clave,
            categoria=categoria,
            frecuencia_uso=frecuencia_uso,
        )

    def __str__(self):
        return (
            f"ID: {self.id_tag}, Palabra clave: {self.palabra_clave}, Categoría: {self.categoria}, "
            f"Frecuencia de uso: {self.frecuencia_uso}"
        )
