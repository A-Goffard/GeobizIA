class Tipo_Publicacion:
    def __init__(self, id_tipo_publicacion, nombre=None):
        self._id_tipo_publicacion = id_tipo_publicacion
        self._nombre = nombre

    @staticmethod
    def crear(id_tipo_publicacion, nombre=None):
        return Tipo_Publicacion(id_tipo_publicacion, nombre)

    @property
    def id_tipo_publicacion(self):
        return self._id_tipo_publicacion

    @id_tipo_publicacion.setter
    def id_tipo_publicacion(self, id_tipo_publicacion):
        self._id_tipo_publicacion = id_tipo_publicacion

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"ID: {self.id_tipo_publicacion}, Nombre: {self.nombre or 'N/A'}"