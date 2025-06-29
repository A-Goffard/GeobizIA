from src.controlador.crud.crud_programacion import CrudProgramacion
from src.controlador.validaciones.validar_programacion import validar_datos_programacion

class Programaciones:
    def __init__(self):
        self.crud = CrudProgramacion()

    def agregar(self, **kwargs):
        id_programacion = kwargs.get("id_programacion")
        if id_programacion is not None and self.crud.existe(id_programacion):
            print(f"Error: Ya existe una programación con id_programacion={id_programacion}.")
            return None
        valido, msg = validar_datos_programacion(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_programacion):
        if not self.crud.existe(id_programacion):
            print(f"Error: No existe una programación con id_programacion={id_programacion}.")
            return False
        return self.crud.eliminar(id_programacion)

    def buscar(self, id_programacion):
        return self.crud.leer(id_programacion)

    def actualizar(self, id_programacion, **kwargs):
        valido, msg = validar_datos_programacion(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_programacion, **kwargs)

    def existe(self, id_programacion):
        return self.crud.existe(id_programacion)

    def listar(self):
        return self.crud.listar()