from abc import ABC
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class BaseGestor(ABC, Generic[T]):
    def __init__(self, table_name=None, fields=None, id_field=None):
        self.table_name = table_name
        self.fields = fields
        self.id_field = id_field
        self.lista: List[T] = []

    def agregar(self, elemento: T) -> bool:
        if elemento not in self.lista:
            self.lista.append(elemento)
            return True
        return False

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

    def actualizar(self, elemento_viejo: T, elemento_nuevo: T) -> bool:
        try:
            idx = self.lista.index(elemento_viejo)
            self.lista[idx] = elemento_nuevo
            return True
        except ValueError:
            return False

    def existe(self, elemento: T) -> bool:
        return elemento in self.lista

    def cantidad_elementos(self) -> int:
        return len(self.lista)

    def mostrar_elemento(self, elemento: T) -> str:
        return str(elemento)

    def existe(self, elemento: T) -> bool:
        return elemento in self.lista

    def cantidad_elementos(self) -> int:
        return len(self.lista)

    def mostrar_elemento(self, elemento: T) -> str:
        return str(elemento)
    def cantidad_elementos(self) -> int:
        return len(self.lista)

    def mostrar_elemento(self, elemento: T) -> str:
        return str(elemento)
