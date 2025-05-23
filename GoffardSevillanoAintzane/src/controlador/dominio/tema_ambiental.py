class TemaAmbiental:
    def __init__(self, id, nombre, descripcion, relevancia, relacion_actividades, relacion_publicaciones):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._relevancia = relevancia
        self._relacion_actividades = relacion_actividades
        self._relacion_publicaciones = relacion_publicaciones

    @property
    def id(self):
        return self._id

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

    @staticmethod
    def crear_tema_ambiental(id, nombre, descripcion, relevancia, relacion_actividades, relacion_publicaciones):
        return TemaAmbiental(
            id=id,
            nombre=nombre,
            descripcion=descripcion,
            relevancia=relevancia,
            relacion_actividades=relacion_actividades,
            relacion_publicaciones=relacion_publicaciones
        )

    def __str__(self):
        return (
            f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, "
            f"Relevancia: {self.relevancia}, Relación actividades: {self._relacion_actividades}, "
            f"Relación publicaciones: {self._relacion_publicaciones}"
        )
