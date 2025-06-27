class GeneradorIA:
    def __init__(self, id_generador_IA, id_usuario, nombre=None, descripcion=None, tipo=None):
        self._id_generador_IA = id_generador_IA
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._descripcion = descripcion
        self._tipo = tipo

    @property
    def id_generador_IA(self):
        return self._id_generador_IA

    @id_generador_IA.setter
    def id_generador_IA(self, id_generador_IA):
        self._id_generador_IA = id_generador_IA

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

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
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @staticmethod
    def crear(id_generador_IA, id_usuario, nombre=None, descripcion=None, tipo=None):
        return GeneradorIA(id_generador_IA, id_usuario, nombre, descripcion, tipo)

    def __str__(self):
        return f"ID: {self.id_generador_IA}, ID Usuario: {self.id_usuario}, Nombre: {self.nombre or 'N/A'}, Descripción: {self.descripcion or 'N/A'}, Tipo: {self.tipo or 'N/A'}"