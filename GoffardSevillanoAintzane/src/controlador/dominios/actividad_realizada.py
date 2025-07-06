class ActividadRealizada:
    def __init__(self, id_actividad_realizada=None, id_actividad=None, fecha=None, asistentes=None, coste_economico=None, facturacion=None, observaciones=None, id_evento=None, id_proyecto=None):
        self._id_actividad_realizada = id_actividad_realizada
        self._id_actividad = id_actividad
        self._fecha = fecha
        self._asistentes = asistentes
        self._coste_economico = coste_economico
        self._facturacion = facturacion
        self._observaciones = observaciones
        self._id_evento = id_evento
        self._id_proyecto = id_proyecto

    @property
    def id_actividad_realizada(self):
        return self._id_actividad_realizada

    @id_actividad_realizada.setter
    def id_actividad_realizada(self, value):
        self._id_actividad_realizada = value

    @property
    def id_actividad(self):
        return self._id_actividad

    @id_actividad.setter
    def id_actividad(self, value):
        self._id_actividad = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def asistentes(self):
        return self._asistentes

    @asistentes.setter
    def asistentes(self, value):
        self._asistentes = value

    @property
    def coste_economico(self):
        return self._coste_economico

    @coste_economico.setter
    def coste_economico(self, value):
        self._coste_economico = value

    @property
    def facturacion(self):
        return self._facturacion

    @facturacion.setter
    def facturacion(self, value):
        self._facturacion = value

    @property
    def observaciones(self):
        return self._observaciones

    @observaciones.setter
    def observaciones(self, value):
        self._observaciones = value

    @property
    def id_evento(self):
        return self._id_evento

    @id_evento.setter
    def id_evento(self, value):
        self._id_evento = value

    @property
    def id_proyecto(self):
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, value):
        self._id_proyecto = value

    def to_dict(self):
        return {
            "id_actividad_realizada": self.id_actividad_realizada,
            "id_actividad": self.id_actividad,
            "fecha": self.fecha,
            "asistentes": self.asistentes,
            "coste_economico": self.coste_economico,
            "facturacion": self.facturacion,
            "observaciones": self.observaciones,
            "id_evento": self.id_evento,
            "id_proyecto": self.id_proyecto
        }
