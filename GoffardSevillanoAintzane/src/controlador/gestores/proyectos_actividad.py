from src.controlador.crud.crud_proyecto_actividad import CrudProyectoActividad
from src.controlador.validaciones.validar_proyecto_actividad import validar_datos_proyecto_actividad

class ProyectoActividadGestor:
    def __init__(self):
        self.crud = CrudProyectoActividad()

    def agregar(self, id_proyecto, id_actividad):
        if self.crud.buscar(id_proyecto, id_actividad):
            print(f"Error: Ya existe la relación proyecto_actividad ({id_proyecto}, {id_actividad}).")
            return None
        datos = {"id_proyecto": id_proyecto, "id_actividad": id_actividad}
        valido, msg = validar_datos_proyecto_actividad(datos)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(id_proyecto, id_actividad)

    def eliminar(self, id_proyecto, id_actividad):
        if not self.crud.buscar(id_proyecto, id_actividad):
            print(f"Error: No existe la relación proyecto_actividad ({id_proyecto}, {id_actividad}).")
            return False
        return self.crud.eliminar(id_proyecto, id_actividad)

    def buscar(self, id_proyecto, id_actividad):
        return self.crud.buscar(id_proyecto, id_actividad)

    def listar(self):
        return self.crud.listar()
