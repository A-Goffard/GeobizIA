from abc import ABC, abstractmethod
from Proyecto.dominios.auditoria_publicacion import AuditoriaPublicacion

class AuditoriaPublicacion(ABC):
    @abstractmethod
    def crear_auditoria(self, datos) -> AuditoriaPublicacion:
        pass