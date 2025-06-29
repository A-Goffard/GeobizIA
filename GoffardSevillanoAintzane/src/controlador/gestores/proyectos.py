from src.controlador.crud.crud_proyecto import CrudProyecto
from src.controlador.validaciones.validar_proyecto import validar_datos_proyecto

class Proyectos:
    def __init__(self):
        self.crud = CrudProyecto()

    def agregar(self, **kwargs):
        id_proyecto = kwargs.get("id_proyecto")
        if id_proyecto is not None and self.crud.existe(id_proyecto):
            print(f"Error: Ya existe un proyecto con id_proyecto={id_proyecto}.")
            return None
        valido, msg = validar_datos_proyecto(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_proyecto):
        if not self.crud.existe(id_proyecto):
            print(f"Error: No existe un proyecto con id_proyecto={id_proyecto}.")
            return False
        return self.crud.eliminar(id_proyecto)

    def buscar(self, id_proyecto):
        return self.crud.leer(id_proyecto)

    def actualizar(self, id_proyecto, **kwargs):
        valido, msg = validar_datos_proyecto(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_proyecto, **kwargs)

    def existe(self, id_proyecto):
        return self.crud.existe(id_proyecto)

    def listar(self):
        return self.crud.listar()