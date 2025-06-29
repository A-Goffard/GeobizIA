from src.controlador.crud.crud_actividad import CrudActividad
from src.controlador.validaciones.validar_actividad import validar_datos_actividad

class Actividades:
    def __init__(self):
        self.crud = CrudActividad()

    def agregar(self, **kwargs):
        id_actividad = kwargs.get("id_actividad")
        if id_actividad is not None and self.crud.existe(id_actividad):
            print(f"Error: Ya existe una actividad con id_actividad={id_actividad}.")
            return None
        valido, msg = validar_datos_actividad(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_actividad):
        if not self.crud.existe(id_actividad):
            print(f"Error: No existe una actividad con id_actividad={id_actividad}.")
            return False
        return self.crud.eliminar(id_actividad)

    def buscar(self, id_actividad):
        return self.crud.leer(id_actividad)

    def actualizar(self, id_actividad, **kwargs):
        valido, msg = validar_datos_actividad(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_actividad, **kwargs)

    def existe(self, id_actividad):
        return self.crud.existe(id_actividad)

    def listar(self):
        return self.crud.listar()