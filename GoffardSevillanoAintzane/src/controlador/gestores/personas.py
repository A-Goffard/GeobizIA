from abc import ABC, abstractmethod
from dominios.persona import Persona
from gestores.base_gestor import BaseGestor

class PersonaFactory(ABC):
    @abstractmethod
    def crear_persona(self, datos) -> Persona:
        pass

class Personas(BaseGestor):
    def mostrar_elemento(self, elemento):
        return str(elemento)