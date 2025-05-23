class Rol:
    def __init__(self, nombre, tareas_permitidas):
        self._nombre = nombre
        self._tareas_permitidas = tareas_permitidas

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tareas_permitidas(self):
        return self._tareas_permitidas

    @tareas_permitidas.setter
    def tareas_permitidas(self, tareas_permitidas):
        self._tareas_permitidas = tareas_permitidas

    @staticmethod
    def crear_rol(nombre, tareas_permitidas):
        return Rol(
            nombre=nombre,
            tareas_permitidas=tareas_permitidas
        )

    def __str__(self):
        return f"Nombre: {self.nombre}, Tareas permitidas: {self.tareas_permitidas}"


