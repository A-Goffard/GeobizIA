from abc import ABC, abstractmethod

class BaseGestor(ABC):
    def __init__(self):
        self.lista = []

    def agregar(self, item):
        self.lista.append(item)
        return f"{item.__class__.__name__} agregado exitosamente."

    def modificar(self, id_item, **kwargs):
        for item in self.lista:
            if hasattr(item, 'id') and item.id == id_item:
                for key, value in kwargs.items():
                    if hasattr(item, key):
                        setattr(item, key, value)
                return f"{item.__class__.__name__} modificado exitosamente."
        return f"No se encontró el {item.__class__.__name__} con ID '{id_item}'."

    def buscar(self, id_item):
        for item in self.lista:
            if hasattr(item, 'id') and item.id == id_item:
                return item
        return None

    def eliminar(self, id_item):
        for item in self.lista:
            if hasattr(item, 'id') and item.id == id_item:
                self.lista.remove(item)
                return f"{item.__class__.__name__} eliminado."
        return f"No se encontró el {item.__class__.__name__} con ID '{id_item}'."
