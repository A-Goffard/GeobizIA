from .persona import Persona

class Usuario(Persona):
    def __init__(self, id_usuario, id_persona, fecha_nacimiento, rol, preferencias, password, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais):
        super().__init__(id_persona, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais)
        self._id_usuario = id_usuario
        self._fecha_nacimiento = fecha_nacimiento
        self._rol = rol
        self._preferencias = preferencias
        self._password = password

    @staticmethod
    def crear_usuario(id_usuario, id_persona, fecha_nacimiento, rol, preferencias, password, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais):
        return Usuario(
            id_usuario=id_usuario,
            id_persona=id_persona,
            fecha_nacimiento=fecha_nacimiento,
            rol=rol,
            preferencias=preferencias,
            password=password,
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            dni=dni,
            direccion=direccion,
            cp=cp,
            poblacion=poblacion,
            pais=pais
        )

    @property
    def id_usuario(self): return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, id_usuario): self._id_usuario = id_usuario

    @property
    def fecha_nacimiento(self): return self._fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento): self._fecha_nacimiento = fecha_nacimiento

    @property
    def rol(self): return self._rol
    @rol.setter
    def rol(self, rol): self._rol = rol

    @property
    def preferencias(self): return self._preferencias
    @preferencias.setter
    def preferencias(self, preferencias): self._preferencias = preferencias

    @property
    def password(self): return self._password
    @password.setter
    def password(self, password): self._password = password

    def __str__(self):
        return (
            f"ID Usuario: {self.id_usuario}, Fecha nacimiento: {self.fecha_nacimiento}, "
            f"Rol: {self.rol}, Preferencias: {self.preferencias}, Contraseña: {self.password}, "
            f"{super().__str__()}"
        )
    @property
    def poblacion(self): return self._poblacion
    @poblacion.setter
    def poblacion(self, poblacion): self._poblacion = poblacion

    @property
    def pais(self): return self._pais
    @pais.setter
    def pais(self, pais): self._pais = pais

    @property
    def rol(self): return self._rol
    @rol.setter
    def rol(self, rol): self._rol = rol

    @property
    def preferencias(self): return self._preferencias
    @preferencias.setter
    def preferencias(self, preferencias): self._preferencias = preferencias

    @property
    def password(self): return self._password
    @password.setter
    def password(self, password): self._password = password

    def __str__(self):
        return (
            f"ID Usuario: {self.id_usuario}, ID Persona: {self.id_persona}, Fecha nacimiento: {self.fecha_nacimiento}, "
            f"Dirección: {self.direccion}, DNI: {self.dni}, CP: {self.cp}, Población: {self.poblacion}, "
            f"País: {self.pais}, Rol: {self.rol}, Preferencias: {self.preferencias}, Contraseña: {self.password}"
        )


