from abc import ABC, abstractmethod
from dominios.log_sistema import LogSistema

class LogSistema(ABC):
    @abstractmethod
    def crear_log(self, datos) -> LogSistema:
        pass