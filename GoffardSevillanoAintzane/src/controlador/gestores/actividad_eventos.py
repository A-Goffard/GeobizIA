from src.controlador.crud.crud_actividad_evento import CrudActividadEvento
from src.controlador.validaciones.validar_actividad_evento import validar_datos_actividad_evento

class ActividadEventosGestor:
    def __init__(self):
        self.crud = CrudActividadEvento()

    def agregar(self, id_actividad, id_evento):
        if self.crud.buscar(id_actividad, id_evento):
            print(f"Error: Ya existe la relación actividad_evento ({id_actividad}, {id_evento}).")
            return None
        datos = {"id_actividad": id_actividad, "id_evento": id_evento}
        valido, msg = validar_datos_actividad_evento(datos)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(id_actividad, id_evento)

    def eliminar(self, id_actividad, id_evento):
        if not self.crud.buscar(id_actividad, id_evento):
            print(f"Error: No existe la relación actividad_evento ({id_actividad}, {id_evento}).")
            return False
        return self.crud.eliminar(id_actividad, id_evento)

    def buscar(self, id_actividad, id_evento):
        return self.crud.buscar(id_actividad, id_evento)

    def listar(self):
        return self.crud.listar()
