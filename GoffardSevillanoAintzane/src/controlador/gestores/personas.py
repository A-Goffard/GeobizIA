from abc import ABC, abstractmethod
from Proyecto.dominios.persona import Persona

class PersonaFactory(ABC):
    @abstractmethod
    def crear_persona(self, datos) -> Persona:
        pass