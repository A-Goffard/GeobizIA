from src.controlador.crud.crud_evento import CrudEvento
from src.controlador.validaciones.validar_evento import validar_datos_evento

class Eventos:
    def __init__(self):
        self.crud = CrudEvento()

    def agregar(self, **kwargs):
        id_evento = kwargs.get("id_evento")
        if id_evento is not None and self.crud.existe(id_evento):
            print(f"Error: Ya existe un evento con id_evento={id_evento}.")
            return None
        valido, msg = validar_datos_evento(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_evento):
        if not self.crud.existe(id_evento):
            print(f"Error: No existe un evento con id_evento={id_evento}.")
            return False
        return self.crud.eliminar(id_evento)

    def buscar(self, id_evento):
        return self.crud.leer(id_evento)

    def actualizar(self, id_evento, **kwargs):
        valido, msg = validar_datos_evento(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_evento, **kwargs)

    def existe(self, id_evento):
        return self.crud.existe(id_evento)

    def listar(self):
        return self.crud.listar()