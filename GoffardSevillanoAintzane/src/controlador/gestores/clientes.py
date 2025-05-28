from abc import ABC, abstractmethod
from dominios.cliente import Cliente
from gestores.base_gestor import BaseGestor

class ClienteFactory(ABC):
    @abstractmethod
    def crear_cliente(self, datos) -> Cliente:
        pass

class Clientes(BaseGestor):
    def mostrar_elemento(self, elemento):
        return str(elemento)