from src.controlador.crud.crud_factura_actividad import CrudFacturaActividad
from src.controlador.validaciones.validar_factura_actividad import validar_datos_factura_actividad

class FacturaActividadGestor:
    def __init__(self):
        self.crud = CrudFacturaActividad()

    def agregar(self, id_factura, id_actividad):
        if self.crud.buscar(id_factura, id_actividad):
            print(f"Error: Ya existe la relación factura_actividad ({id_factura}, {id_actividad}).")
            return None
        datos = {"id_factura": id_factura, "id_actividad": id_actividad}
        valido, msg = validar_datos_factura_actividad(datos)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(id_factura, id_actividad)

    def eliminar(self, id_factura, id_actividad):
        if not self.crud.buscar(id_factura, id_actividad):
            print(f"Error: No existe la relación factura_actividad ({id_factura}, {id_actividad}).")
            return False
        return self.crud.eliminar(id_factura, id_actividad)

    def buscar(self, id_factura, id_actividad):
        return self.crud.buscar(id_factura, id_actividad)

    def listar(self):
        return self.crud.listar()
