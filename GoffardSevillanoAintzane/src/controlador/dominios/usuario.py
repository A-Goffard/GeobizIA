from persona import Persona

class Usuario(Persona):

    def __init__(self, id, nombre, apellido, correo, telefono, fecha_nacimiento, direccion, dni, cp, poblacion, pais, rol, preferencias, password):
        super().__init__(id, nombre, apellido, correo, telefono)
        self._fecha_nacimiento = fecha_nacimiento
        self._direccion = direccion
        self._dni = dni
        self._cp = cp
        self._poblacion = poblacion
        self._pais = pais
        self._rol = rol
        self._preferencias = preferencias
        self._password = password

    @staticmethod
    def crear_usuario(id, dni, nombre, apellido, direccion, cp, poblacion, pais, fecha_nacimiento, email, telefono, preferencias, rol, password):
        return Usuario(
            id=id,
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            correo=email,
            telefono=telefono,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            cp=cp,
            poblacion=poblacion,
            pais=pais,
            rol=rol,
            preferencias=preferencias,
            password=password
        )
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, cp):
        self._cp = cp

    @property
    def poblacion(self):
        return self._poblacion

    @poblacion.setter
    def poblacion(self, poblacion):
        self._poblacion = poblacion

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        self._pais = pais

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def preferencias(self):
        return self._preferencias

    @preferencias.setter
    def preferencias(self, preferencias):
        self._preferencias = preferencias

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password

    def get_tipo(self) -> str:
        return "Usuario"
    
    def __str__(self):
        return (
            f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, "
            f"Correo: {self.correo}, Teléfono: {self.telefono}, Fecha nacimiento: {self.fecha_nacimiento}, "
            f"Dirección: {self.direccion}, DNI: {self.dni}, CP: {self.cp}, Población: {self.poblacion}, "
            f"País: {self.pais}, Rol: {self.rol}, Preferencias: {self.preferencias}, Contraseña: {self.password}"
        )


