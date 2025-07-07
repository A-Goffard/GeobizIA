class Tema_Ambiental:
    def __init__(self, id_tema_ambiental, nombre=None, descripcion=None, relevancia=None):
        self._id_tema_ambiental = id_tema_ambiental
        self._nombre = nombre
        self._descripcion = descripcion
        self._relevancia = relevancia

    @property
    def id_tema_ambiental(self):
        return self._id_tema_ambiental

    @id_tema_ambiental.setter
    def id_tema_ambiental(self, id_tema_ambiental):
        self._id_tema_ambiental = id_tema_ambiental

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def relevancia(self):
        return self._relevancia

    @relevancia.setter
    def relevancia(self, relevancia):
        self._relevancia = relevancia

    # @staticmethod
    # def crear(id_tema_ambiental, nombre=None, descripcion=None, relevancia=None):
    #     return Tema_Ambiental(id_tema_ambiental, nombre, descripcion, relevancia)

    def __str__(self):
        return (
            f"ID: {self.id_tema_ambiental}, Nombre: {self.nombre or 'N/A'}, "
            f"Descripción: {self.descripcion or 'N/A'}, Relevancia: {self.relevancia or 'N/A'}"
        )