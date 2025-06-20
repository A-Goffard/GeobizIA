class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto):
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
    def poblacion(self):
        return self._poblacion
    
    @poblacion.setter
    def poblacion(self, value):
        self._poblacion = value
        
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
    def presupuesto(self):
        return self._presupuesto

    @presupuesto.setter
    def presupuesto(self, value):
        self._presupuesto = value

    def __str__(self):
        return (
            f"ID: {self.id_proyecto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, "
            f"Fecha inicio: {self.fecha_inicio}, Fecha fin: {self.fecha_fin}, Población: {self.poblacion}, Responsable: {self.responsable}, "
            f"Estado: {self.estado}, Objetivos: {self.objetivos}, "
            f"Presupuesto: {self.presupuesto}"
        )
        self._presupuesto = value

    def __str__(self):
        return (
            f"ID: {self.id_proyecto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, "
            f"Fecha inicio: {self.fecha_inicio}, Fecha fin: {self.fecha_fin}, Población: {self.poblacion}, Responsable: {self.responsable}, "
            f"Estado: {self.estado}, Objetivos: {self.objetivos}, Actividades: {self.actividades}, "
            f"Presupuesto: {self.presupuesto}"
        )
