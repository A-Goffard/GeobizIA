class Proyecto:
    def __init__(self, id_proyecto, nombre=None, descripcion=None, fecha_inicio=None, fecha_fin=None, poblacion=None, responsable=None, estado=None, objetivos=None, presupuesto=None):
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._poblacion = poblacion
        self._responsable = responsable
        self._estado = estado
        self._objetivos = objetivos
        self._presupuesto = presupuesto

    @property
    def id_proyecto(self):
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, id_proyecto):
        self._id_proyecto = id_proyecto

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
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    @property
    def fecha_fin(self):
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, fecha_fin):
        self._fecha_fin = fecha_fin

    @property
    def poblacion(self):
        return self._poblacion

    @poblacion.setter
    def poblacion(self, poblacion):
        self._poblacion = poblacion

    @property
    def responsable(self):
        return self._responsable

    @responsable.setter
    def responsable(self, responsable):
        self._responsable = responsable

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def objetivos(self):
        return self._objetivos

    @objetivos.setter
    def objetivos(self, objetivos):
        self._objetivos = objetivos

    @property
    def presupuesto(self):
        return self._presupuesto

    @presupuesto.setter
    def presupuesto(self, presupuesto):
        self._presupuesto = presupuesto

    # @staticmethod
    # def crear(id_proyecto, nombre=None, descripcion=None, fecha_inicio=None, fecha_fin=None, poblacion=None, responsable=None, estado=None, objetivos=None, presupuesto=None):
    #     return Proyecto(id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto)

    def __str__(self):
        return (
            f"ID: {self.id_proyecto}, Nombre: {self.nombre or 'N/A'}, Descripción: {self.descripcion or 'N/A'}, "
            f"Fecha Inicio: {self.fecha_inicio or 'N/A'}, Fecha Fin: {self.fecha_fin or 'N/A'}, "
            f"Población: {self.poblacion or 'N/A'}, Responsable: {self.responsable or 'N/A'}, "
            f"Estado: {self.estado or 'N/A'}, Objetivos: {self.objetivos or 'N/A'}, "
            f"Presupuesto: {self.presupuesto or 'N/A'}"
        )