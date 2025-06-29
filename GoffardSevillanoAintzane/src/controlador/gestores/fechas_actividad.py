from src.controlador.crud.crud_fecha_actividad import CrudFechaActividad
from src.controlador.validaciones.validar_fecha_actividad import validar_datos_fecha_actividad

class Fechas_Actividad:
    def __init__(self):
        self.crud = CrudFechaActividad()

    def agregar(self, **kwargs):
        id_fecha = kwargs.get("id_fecha")
        if id_fecha is not None and self.crud.existe(id_fecha):
            print(f"Error: Ya existe una fecha_actividad con id_fecha={id_fecha}.")
            return None
        valido, msg = validar_datos_fecha_actividad(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_fecha):
        if not self.crud.existe(id_fecha):
            print(f"Error: No existe una fecha_actividad con id_fecha={id_fecha}.")
            return False
        return self.crud.eliminar(id_fecha)

    def buscar(self, id_fecha):
        return self.crud.leer(id_fecha)

    def actualizar(self, id_fecha, **kwargs):
        valido, msg = validar_datos_fecha_actividad(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_fecha, **kwargs)

    def existe(self, id_fecha):
        return self.crud.existe(id_fecha)

    def listar(self):
        return self.crud.listar()