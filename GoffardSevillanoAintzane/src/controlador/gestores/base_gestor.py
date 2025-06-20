from abc import ABC
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class BaseGestor(ABC, Generic[T]):
    def __init__(self):
        self.lista: List[T] = []

    def agregar(self, elemento: T) -> bool:
        self.lista.append(elemento)
        return True

    def eliminar(self, elemento: T) -> bool:
        if elemento in self.lista:
            self.lista.remove(elemento)
            return True
        return False

    def buscar(self, elemento: T) -> Optional[T]:
        for item in self.lista:
            if item == elemento:
                return item
        return None

    def mostrar_todos_los_elem(self) -> List[T]:
        return self.lista.copy()

    def existe(self, elemento: T) -> bool:
        return elemento in self.lista

    def cantidad_elementos(self) -> int:
        return len(self.lista)

    def mostrar_elemento(self, elemento: T) -> str:
        return str(elemento)
