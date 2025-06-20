class RedSocial:
    def __init__(self, id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion):
        self._id_red_social = id_red_social
        self._plataforma = plataforma
        self._nombre_cuenta = nombre_cuenta
        self._credenciales = credenciales
        self._preferencias_publicacion = preferencias_publicacion
        self._estado_conexion = estado_conexion
        self._ultima_publicacion = ultima_publicacion

    @staticmethod
    def crear_red_social(id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion):
        return RedSocial(id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion)

    @property
    def id_red_social(self): return self._id_red_social
    @id_red_social.setter
    def id_red_social(self, id_red_social): self._id_red_social = id_red_social

    @property
    def plataforma(self): return self._plataforma
    @plataforma.setter
    def plataforma(self, plataforma): self._plataforma = plataforma

    @property
    def nombre_cuenta(self): return self._nombre_cuenta
    @nombre_cuenta.setter
    def nombre_cuenta(self, nombre_cuenta): self._nombre_cuenta = nombre_cuenta

    @property
    def credenciales(self): return self._credenciales
    @credenciales.setter
    def credenciales(self, credenciales): self._credenciales = credenciales

    @property
    def preferencias_publicacion(self): return self._preferencias_publicacion
    @preferencias_publicacion.setter
    def preferencias_publicacion(self, preferencias_publicacion): self._preferencias_publicacion = preferencias_publicacion

    @property
    def estado_conexion(self): return self._estado_conexion
    @estado_conexion.setter
    def estado_conexion(self, estado_conexion): self._estado_conexion = estado_conexion

    @property
    def ultima_publicacion(self): return self._ultima_publicacion
    @ultima_publicacion.setter
    def ultima_publicacion(self, ultima_publicacion): self._ultima_publicacion = ultima_publicacion

    def __str__(self):
        return (
            f"ID: {self.id_red_social}, Plataforma: {self.plataforma}, Cuenta: {self.nombre_cuenta}, "
            f"Estado: {self.estado_conexion}, Última publicación: {self.ultima_publicacion}"
        )
    def ultima_publicacion(self, ultima_publicacion): self._ultima_publicacion = ultima_publicacion

    @property
    def relaciones(self): return self._relaciones
    @relaciones.setter
    def relaciones(self, relaciones): self._relaciones = relaciones

    def __str__(self):
        return (
            f"ID: {self.id_red_social}, Plataforma: {self.plataforma}, Cuenta: {self.nombre_cuenta}, "
            f"Empresa ID: {self.empresa_id}, Estado: {self.estado_conexion}, Última publicación: {self.ultima_publicacion}, "
            f"Relaciones: {self.relaciones}"
        )
