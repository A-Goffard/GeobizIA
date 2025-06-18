from abc import ABC, abstractmethod

# Clase base: Persona
class Persona(ABC):
    def __init__(self, id_persona, nombre, apellido=None, email=None, telefono=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono

    @property
    def id_persona(self): return self._id_persona
    @id_persona.setter
    def id_persona(self, id_persona): self._id_persona = id_persona

    @property
    def nombre(self): return self._nombre
    @nombre.setter
    def nombre(self, nombre): self._nombre = nombre

    @property
    def apellido(self): return self._apellido
    @apellido.setter
    def apellido(self, apellido): self._apellido = apellido

    @property
    def email(self): return self._email
    @email.setter
    def email(self, email): self._email = email

    @property
    def telefono(self): return self._telefono
    @telefono.setter
    def telefono(self, telefono): self._telefono = telefono

    @abstractmethod
    def get_tipo(self) -> str:
        pass