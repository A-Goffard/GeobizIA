from src.controlador.crud.crud_actividad_fecha import CrudActividadFecha
from src.controlador.validaciones.validar_actividad_fecha import validar_datos_actividad_fecha

class ActividadesFechaGestor:
    def __init__(self):
        self.crud = CrudActividadFecha()

    def agregar(self, id_actividad, id_fecha):
        if self.crud.buscar(id_actividad, id_fecha):
            print(f"Error: Ya existe la relación actividad_fecha ({id_actividad}, {id_fecha}).")
            return None
        datos = {"id_actividad": id_actividad, "id_fecha": id_fecha}
        valido, msg = validar_datos_actividad_fecha(datos)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(id_actividad, id_fecha)

    def eliminar(self, id_actividad, id_fecha):
        if not self.crud.buscar(id_actividad, id_fecha):
            print(f"Error: No existe la relación actividad_fecha ({id_actividad}, {id_fecha}).")
            return False
        return self.crud.eliminar(id_actividad, id_fecha)

    def buscar(self, id_actividad, id_fecha):
        return self.crud.buscar(id_actividad, id_fecha)

    def listar(self):
        return self.crud.listar()
