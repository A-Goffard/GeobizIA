import bcrypt

class Usuario:
    def __init__(self, id_usuario, id_persona, fecha_nacimiento=None, rol=None, preferencias=None, password=None):
        self._id_usuario = id_usuario
        self._id_persona = id_persona
        self._fecha_nacimiento = fecha_nacimiento
        self._rol = rol
        self._preferencias = preferencias
        # Almacenamos la contraseña como se recibe. El hasheo se hará en el gestor o con set_password.
        self._password = password

    def set_password(self, plain_password):
        """Hashea la contraseña y la guarda."""
        if plain_password:
            self._password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        else:
            self._password = None

    def check_password(self, plain_password):
        """Verifica si la contraseña en texto plano coincide con el hash."""
        if self._password is None or not plain_password:
            return False
        return bcrypt.checkpw(plain_password.encode('utf-8'), self._password.encode('utf-8'))

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    @property
    def preferencias(self):
        return self._preferencias

    @preferencias.setter
    def preferencias(self, preferencias):
        self._preferencias = preferencias

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        # Permitir asignar un hash directamente (ej. desde la BD)
        self._password = password

    def __str__(self):
        # No mostrar nunca la contraseña en el __str__
        return f"ID: {self.id_usuario}, ID Persona: {self.id_persona}, Fecha Nacimiento: {self.fecha_nacimiento or 'N/A'}, Rol: {self.rol or 'N/A'}, Preferencias: {self.preferencias or 'N/A'}"