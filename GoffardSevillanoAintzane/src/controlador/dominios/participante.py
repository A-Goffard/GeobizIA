from .persona import Persona

class Participante(Persona):
    def __init__(self, id_participante, nombre, apellido, email, telefono, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro):
        super().__init__(id_participante, nombre, apellido, email, telefono)
        self._numero_personas_juntas = numero_personas_juntas
        self._rol = rol
        self._como_conocer = como_conocer
        self._actividad_id = actividad_id
        self._fecha_registro = fecha_registro

    @staticmethod
    def crear_participante(id_participante, nombre, apellido, email, telefono, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro):
        return Participante(
            id_participante=id_participante,
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            numero_personas_juntas=numero_personas_juntas,
            rol=rol,
            como_conocer=como_conocer,
            actividad_id=actividad_id,
            fecha_registro=fecha_registro
        )

    @property
    def id_participante(self):
        return self._id_participante

    @id_participante.setter
    def id_participante(self, id_participante):
        self._id_participante = id_participante

    @property
    def numero_personas_juntas(self):
        return self._numero_personas_juntas

    @numero_personas_juntas.setter
    def numero_personas_juntas(self, value):
        self._numero_personas_juntas = value

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    @property
    def como_conocer(self):
        return self._como_conocer

    @como_conocer.setter
    def como_conocer(self, como_conocer):
        self._como_conocer = como_conocer

    @property
    def actividad_id(self):
        return self._actividad_id

    @actividad_id.setter
    def actividad_id(self, actividad_id):
        self._actividad_id = actividad_id

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    def get_tipo(self):
        return "Participante"

    def __str__(self):
        return (
            f"ID: {self.id_participante}, Nombre: {self._nombre}, Apellido: {self._apellido}, "
            f"Email: {self._email}, Teléfono: {self._telefono}, Rol: {self.rol}, "
            f"Nº personas juntas: {self.numero_personas_juntas}, Cómo conocer: {self.como_conocer}, "
            f"Actividad ID: {self.actividad_id}, Fecha de Registro: {self.fecha_registro}"
        )
        return self._como_conocer

    @como_conocer.setter
    def como_conocer(self, como_conocer):
        self._como_conocer = como_conocer

    @property
    def actividad_id(self):
        return self._actividad_id

    @actividad_id.setter
    def actividad_id(self, actividad_id):
        self._actividad_id = actividad_id

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    def get_tipo(self):
        return "Participante"

    def __str__(self):
        return (
            f"ID: {self.id_participante}, Nombre: {self.nombre}, Apellido: {self.apellido}, "
            f"Correo: {self.correo}, Teléfono: {self.telefono}, Rol: {self.rol}, "
            f"Nº personas juntas: {self.numero_personas_juntas}, Cómo conocer: {self.como_conocer}, "
            f"Actividad ID: {self.actividad_id}, Fecha de Registro: {self.fecha_registro}"
        )
