class Auditoria_Publicacion:
    def __init__(
        self,
        id_auditoria_publicacion,
        publicacion_id,
        generador_ia_id,
        fecha_generacion,
        usuario_id,
        parametros_entrada,
        resultado,
        observaciones
    ):
        self._id_auditoria_publicacion = id_auditoria_publicacion
        self._publicacion_id = publicacion_id
        self._generador_ia_id = generador_ia_id
        self._fecha_generacion = fecha_generacion
        self._usuario_id = usuario_id
        self._parametros_entrada = parametros_entrada
        self._resultado = resultado
        self._observaciones = observaciones

    @property
    def id_auditoria_publicacion(self):
        return self._id_auditoria_publicacion

    @id_auditoria_publicacion.setter
    def id_auditoria_publicacion(self, value):
        self._id_auditoria_publicacion = value

    @property
    def publicacion_id(self):
        return self._publicacion_id

    @publicacion_id.setter
    def publicacion_id(self, value):
        self._publicacion_id = value

    @property
    def generador_ia_id(self):
        return self._generador_ia_id

    @generador_ia_id.setter
    def generador_ia_id(self, value):
        self._generador_ia_id = value

    @property
    def fecha_generacion(self):
        return self._fecha_generacion

    @fecha_generacion.setter
    def fecha_generacion(self, value):
        self._fecha_generacion = value

    @property
    def usuario_id(self):
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, value):
        self._usuario_id = value

    @property
    def parametros_entrada(self):
        return self._parametros_entrada

    @parametros_entrada.setter
    def parametros_entrada(self, value):
        self._parametros_entrada = value

    @property
    def resultado(self):
        return self._resultado

    @resultado.setter
    def resultado(self, value):
        self._resultado = value

    @property
    def observaciones(self):
        return self._observaciones

    @observaciones.setter
    def observaciones(self, value):
        self._observaciones = value

    # @staticmethod
    # def crear(
    #     id_auditoria_publicacion,
    #     publicacion_id,
    #     generador_ia_id,
    #     fecha_generacion,
    #     usuario_id,
    #     parametros_entrada,
    #     resultado,
    #     observaciones
    # ):
    #     return Auditoria_Publicacion(
    #         id_auditoria_publicacion,
    #         publicacion_id,
    #         generador_ia_id,
    #         fecha_generacion,
    #         usuario_id,
    #         parametros_entrada,
    #         resultado,
    #         observaciones
    #     )

    def __str__(self):
        return (
            f"ID Auditoría: {self.id_auditoria_publicacion}, "
            f"Publicación ID: {self.publicacion_id}, Generador IA ID: {self.generador_ia_id}, "
            f"Fecha: {self.fecha_generacion}, Usuario ID: {self.usuario_id}, "
            f"Parámetros: {self.parametros_entrada}, Resultado: {self.resultado}, "
            f"Observaciones: {self.observaciones}"
        )