class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_fin, responsable, estado, objetivos, actividades, presupuesto):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._responsable = responsable
        self._estado = estado
        self._objetivos = objetivos  # Lista de objetivos o string
        self._actividades = actividades  # Lista de actividades asociadas
        self._presupuesto = presupuesto

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self._fecha_inicio = value

    @property
    def fecha_fin(self):
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, value):
        self._fecha_fin = value

    @property
    def responsable(self):
        return self._responsable

    @responsable.setter
    def responsable(self, value):
        self._responsable = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def objetivos(self):
        return self._objetivos

    @objetivos.setter
    def objetivos(self, value):
        self._objetivos = value

    @property
    def actividades(self):
        return self._actividades

    @actividades.setter
    def actividades(self, value):
        self._actividades = value

    @property
    def presupuesto(self):
        return self._presupuesto

    @presupuesto.setter
    def presupuesto(self, value):
        self._presupuesto = value

    def __str__(self):
        return (
            f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, "
            f"Fecha inicio: {self.fecha_inicio}, Fecha fin: {self.fecha_fin}, Responsable: {self.responsable}, "
            f"Estado: {self.estado}, Objetivos: {self.objetivos}, Actividades: {self.actividades}, "
            f"Presupuesto: {self.presupuesto}"
        )
