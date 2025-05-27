class RedSocial:
    def __init__(self, id, plataforma, nombre_cuenta, credenciales, empresa_id, preferencias_publicacion, estado_conexion, ultima_publicacion, relaciones):
        self._id = id
        self._plataforma = plataforma
        self._nombre_cuenta = nombre_cuenta
        self._credenciales = credenciales
        self._empresa_id = empresa_id
        self._preferencias_publicacion = preferencias_publicacion
        self._estado_conexion = estado_conexion
        self._ultima_publicacion = ultima_publicacion
        self._relaciones = relaciones if relaciones is not None else []

    @staticmethod
    def crear_red_social(id, plataforma, nombre_cuenta, credenciales, empresa_id, preferencias_publicacion, estado_conexion, ultima_publicacion, relaciones):
        return RedSocial(id, plataforma, nombre_cuenta, credenciales, empresa_id, preferencias_publicacion, estado_conexion, ultima_publicacion, relaciones)

    @property
    def id(self): return self._id
    @id.setter
    def id(self, id): self._id = id

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
    def empresa_id(self): return self._empresa_id
    @empresa_id.setter
    def empresa_id(self, empresa_id): self._empresa_id = empresa_id

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

    @property
    def relaciones(self): return self._relaciones
    @relaciones.setter
    def relaciones(self, relaciones): self._relaciones = relaciones

    def __str__(self):
        return (
            f"ID: {self.id}, Plataforma: {self.plataforma}, Cuenta: {self.nombre_cuenta}, "
            f"Empresa ID: {self.empresa_id}, Estado: {self.estado_conexion}, Última publicación: {self.ultima_publicacion}, "
            f"Relaciones: {self.relaciones}"
        )
