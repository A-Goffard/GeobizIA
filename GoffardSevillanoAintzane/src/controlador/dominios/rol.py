class Rol:
    def __init__(self, id_rol, nombre, descripcion):
        self._id_rol = id_rol
        self._nombre = nombre
        self._descripcion = descripcion

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self._id_rol = id_rol

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

    @staticmethod
    def crear_rol(id_rol, nombre, descripcion):
        return Rol(
            id_rol=id_rol,
            nombre=nombre,
            descripcion=descripcion
        )

    def __str__(self):
        return f"ID: {self.id_rol}, Nombre: {self.nombre}, Descripción: {self.descripcion}"


