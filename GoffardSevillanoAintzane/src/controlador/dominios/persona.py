from abc import ABC, abstractmethod

# Clase base: Persona
class Persona(ABC):
    def __init__(self, id, nombre, apellido, email, telefono):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono

    @property
    def id(self): return self._id
    @id.setter 
    def id(self, id): self._id = id
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

    @staticmethod
    def crear_persona(id, nombre, apellido, email, telefono):
        return Persona(id, nombre, apellido, email, telefono)

    @abstractmethod
    def get_tipo(self) -> str:
        pass