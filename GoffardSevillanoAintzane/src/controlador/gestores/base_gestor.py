from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class BaseGestor(ABC, Generic[T]):
    def __init__(self):
        self.lista: List[T] = []

    def agregar(self, elemento: T) -> bool:
        self.lista.append(elemento)
        return True

    def eliminar(self, id_elemento: int) -> bool:
        for item in self.lista:
            if hasattr(item, 'id') and item.id == id_elemento:
                self.lista.remove(item)
                return True
        return False

    def buscar(self, id_elemento: int) -> Optional[T]:
        for item in self.lista:
            if hasattr(item, 'id') and item.id == id_elemento:
                return item
        return None

    def mostrar_todos_los_elem(self) -> List[T]:
        return self.lista.copy()

    def esta_vacia(self) -> bool:
        return len(self.lista) == 0

    def cantidad_elementos(self) -> int:
        return len(self.lista)

    @abstractmethod
    def mostrar_elemento(self, elemento: T) -> str:
        pass
