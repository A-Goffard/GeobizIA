from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class BaseGestor(ABC, Generic[T]):
    def __init__(self, table_name: str, id_field: str, domain_class: type):
        self.table_name = table_name
        self.id_field = id_field
        self.domain_class = domain_class

    @abstractmethod
    def agregar(self, elemento: T) -> Optional[T]:
        pass

    @abstractmethod
    def eliminar(self, id_elemento) -> bool:
        pass

    @abstractmethod
    def buscar(self, id_elemento) -> Optional[T]:
        pass

    @abstractmethod
    def mostrar_todos_los_elem(self) -> List[T]:
        pass

    @abstractmethod
    def existe(self, id_elemento) -> bool:
        pass

    @abstractmethod
    def cantidad_elementos(self) -> int:
        pass

    @abstractmethod
    def mostrar_elemento(self, elemento: T) -> str:
        pass

    @abstractmethod
    def actualizar(self, elemento: T) -> bool:
        pass