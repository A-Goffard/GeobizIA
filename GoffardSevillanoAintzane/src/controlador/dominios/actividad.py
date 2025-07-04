class Actividad:
    def __init__(self, id_actividad=None, tipo=None, nombre=None, descripcion=None, responsable=None, duracion=None, coste_economico=None, coste_horas=None, facturacion=None, resultados=None, valoracion=None, observaciones=None):
        self._id_actividad = id_actividad
        self._tipo = tipo
        self._nombre = nombre
        self._descripcion = descripcion
        self._responsable = responsable
        self._duracion = duracion
        self._coste_economico = coste_economico
        self._coste_horas = coste_horas
        self._facturacion = facturacion
        self._resultados = resultados
        self._valoracion = valoracion
        self._observaciones = observaciones

    @property
    def id_actividad(self):
        return self._id_actividad

    @id_actividad.setter
    def id_actividad(self, id_actividad):
        self._id_actividad = id_actividad

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

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
    def observaciones(self):
        return self._observaciones

    @observaciones.setter
    def observaciones(self, observaciones):
        self._observaciones = observaciones

    # @staticmethod
    # def crear(id_actividad, tipo=None, nombre=None, descripcion=None, responsable=None, duracion=None, coste_economico=None, coste_horas=None, facturacion=None, resultados=None, valoracion=None, observaciones=None):
    #     return Actividad(id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones)

    def __str__(self):
        return (f"ID: {self.id_actividad}, Tipo: {self.tipo or 'N/A'}, Nombre: {self.nombre or 'N/A'}, "
                f"Descripción: {self.descripcion or 'N/A'}, Responsable: {self.responsable or 'N/A'}, "
                f"Duración: {self.duracion or 'N/A'}, Coste Económico: {self.coste_economico or 'N/A'}, "
                f"Coste Horas: {self.coste_horas or 'N/A'}, Facturación: {self.facturacion or 'N/A'}, "
                f"Resultados: {self.resultados or 'N/A'}, Valoración: {self.valoracion or 'N/A'}, "
                f"Observaciones: {self.observaciones or 'N/A'}")

    def to_dict(self):
        return {
            "id_actividad": self.id_actividad,
            "tipo": self.tipo,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "responsable": self.responsable,
            "duracion": self.duracion,
            "coste_economico": self.coste_economico,
            "coste_horas": self.coste_horas,
            "facturacion": self.facturacion,
            "resultados": self.resultados,
            "valoracion": self.valoracion,
            "observaciones": self.observaciones
        }