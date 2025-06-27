class Persona:
    def __init__(self, id_persona, nombre=None, apellido=None, email=None, telefono=None, dni=None, direccion=None, cp=None, poblacion=None, pais=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._dni = dni
        self._direccion = direccion
        self._cp = cp
        self._poblacion = poblacion
        self._pais = pais

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

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
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

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

    @staticmethod
    def crear(id_persona, nombre=None, apellido=None, email=None, telefono=None, dni=None, direccion=None, cp=None, poblacion=None, pais=None):
        return Persona(id_persona, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais)

    def __str__(self):
        return f"ID: {self.id_persona}, Nombre: {self.nombre or 'N/A'}, Apellido: {self.apellido or 'N/A'}, Email: {self.email or 'N/A'}, Teléfono: {self.telefono or 'N/A'}, DNI: {self.dni or 'N/A'}, Dirección: {self.direccion or 'N/A'}, CP: {self.cp or 'N/A'}, Población: {self.poblacion or 'N/A'}, País: {self.pais or 'N/A'}"