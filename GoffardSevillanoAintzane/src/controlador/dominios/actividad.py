class Actividad:
    def __init__(self, id, tipo, nombre, fecha_ejecucion, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, modificaciones):
        self._id = id
        self._tipo = tipo
        self._nombre = nombre
        self._fecha_ejecucion = fecha_ejecucion
        self._descripcion = descripcion
        self._responsable = responsable
        self._duracion = duracion
        self._coste_economico = coste_economico
        self._coste_horas = coste_horas
        self._facturacion = facturacion
        self._resultados = resultados
        self._valoracion = valoracion
        self._modificaciones = modificaciones

    @staticmethod
    def crear_actividad(id, tipo, nombre, fecha_ejecucion, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, modificaciones):
        return Actividad(
            id=id,
            tipo=tipo,
            nombre=nombre,
            fecha_ejecucion=fecha_ejecucion,
            descripcion=descripcion,
            responsable=responsable,
            duracion=duracion,
            coste_economico=coste_economico,
            coste_horas=coste_horas,
            facturacion=facturacion,
            resultados=resultados,
            valoracion=valoracion,
            modificaciones=modificaciones
        )

    @property
    def id(self):
        return self._id

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo
        
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fecha_ejecucion(self):
        return self._fecha_ejecucion

    @fecha_ejecucion.setter
    def fecha_ejecucion(self, fecha_ejecucion):
        self._fecha_ejecucion = fecha_ejecucion

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def responsable(self):
        return self._responsable

    @responsable.setter
    def responsable(self, responsable):
        self._responsable = responsable

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion

    @property
    def coste_economico(self):
        return self._coste_economico

    @coste_economico.setter
    def coste_economico(self, coste_economico):
        self._coste_economico = coste_economico

    @property
    def coste_horas(self):
        return self._coste_horas

    @coste_horas.setter
    def coste_horas(self, coste_horas):
        self._coste_horas = coste_horas

    @property
    def facturacion(self):
        return self._facturacion

    @facturacion.setter
    def facturacion(self, facturacion):
        self._facturacion = facturacion

    @property
    def resultados(self):
        return self._resultados

    @resultados.setter
    def resultados(self, resultados):
        self._resultados = resultados

    @property
    def valoracion(self):
        return self._valoracion

    @valoracion.setter
    def valoracion(self, valoracion):
        self._valoracion = valoracion

    @property
    def modificaciones(self):
        return self._modificaciones

    @modificaciones.setter
    def modificaciones(self, modificaciones):
        self._modificaciones = modificaciones

    def __str__(self):
        return (
            f"ID: {self.id}, Tipo: {self.tipo}, Nombre: {self.nombre}, Fecha ejecución: {self.fecha_ejecucion}, "
            f"Descripción: {self.descripcion}, Responsable: {self.responsable}, Duración: {self.duracion}, "
            f"Coste económico: {self.coste_economico}, Coste horas: {self.coste_horas}, Facturación: {self.facturacion}, "
            f"Resultados: {self.resultados}, Valoración: {self.valoracion}, Modificaciones: {self.modificaciones}"
        )
