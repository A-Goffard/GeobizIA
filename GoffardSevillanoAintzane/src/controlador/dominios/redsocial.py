class RedSocial:
    def __init__(self, id_red_social, plataforma, nombre_cuenta, credenciales=None, preferencias_publicacion=None, estado_conexion=None, ultima_publicacion=None):
        self._id_red_social = id_red_social
        self._plataforma = plataforma
        self._nombre_cuenta = nombre_cuenta
        self._credenciales = credenciales
        self._preferencias_publicacion = preferencias_publicacion
        self._estado_conexion = estado_conexion
        self._ultima_publicacion = ultima_publicacion

    @property
    def id_red_social(self):
        return self._id_red_social

    @id_red_social.setter
    def id_red_social(self, value):
        self._id_red_social = value

    @property
    def plataforma(self):
        return self._plataforma

    @plataforma.setter
    def plataforma(self, value):
        self._plataforma = value

    @property
    def nombre_cuenta(self):
        return self._nombre_cuenta

    @nombre_cuenta.setter
    def nombre_cuenta(self, value):
        self._nombre_cuenta = value

    @property
    def credenciales(self):
        return self._credenciales

    @credenciales.setter
    def credenciales(self, value):
        self._credenciales = value

    @property
    def preferencias_publicacion(self):
        return self._preferencias_publicacion

    @preferencias_publicacion.setter
    def preferencias_publicacion(self, value):
        self._preferencias_publicacion = value

    @property
    def estado_conexion(self):
        return self._estado_conexion

    @estado_conexion.setter
    def estado_conexion(self, value):
        self._estado_conexion = value

    @property
    def ultima_publicacion(self):
        return self._ultima_publicacion

    @ultima_publicacion.setter
    def ultima_publicacion(self, value):
        self._ultima_publicacion = value

    @staticmethod
    def crear(id_red_social, plataforma, nombre_cuenta, credenciales=None, preferencias_publicacion=None, estado_conexion=None, ultima_publicacion=None):
        return RedSocial(id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion)

    def __str__(self):
        return f"ID: {self.id_red_social}, Plataforma: {self.plataforma}, Cuenta: {self.nombre_cuenta}, Estado: {self.estado_conexion}"
