from src.controlador.crud.crud_plantilla import CrudPlantilla
from src.controlador.validaciones.validar_plantilla import validar_datos_plantilla

class Plantillas:
    def __init__(self):
        self.crud = CrudPlantilla()

    def agregar(self, **kwargs):
        id_plantilla = kwargs.get("id_plantilla")
        if id_plantilla is not None and self.crud.existe(id_plantilla):
            print(f"Error: Ya existe una plantilla con id_plantilla={id_plantilla}.")
            return None
        valido, msg = validar_datos_plantilla(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_plantilla):
        if not self.crud.existe(id_plantilla):
            print(f"Error: No existe una plantilla con id_plantilla={id_plantilla}.")
            return False
        return self.crud.eliminar(id_plantilla)

    def buscar(self, id_plantilla):
        return self.crud.leer(id_plantilla)

    def actualizar(self, id_plantilla, **kwargs):
        valido, msg = validar_datos_plantilla(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_plantilla, **kwargs)

    def existe(self, id_plantilla):
        return self.crud.existe(id_plantilla)

    def listar(self):
        return self.crud.listar()