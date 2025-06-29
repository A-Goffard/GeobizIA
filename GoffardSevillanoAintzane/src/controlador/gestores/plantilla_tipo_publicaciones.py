from src.controlador.crud.crud_plantilla_tipo_publicacion import CrudPlantillaTipoPublicacion
from src.controlador.validaciones.validar_plantilla_tipo_publicacion import validar_datos_plantilla_tipo_publicacion

class PlantillaTipoPublicacionGestor:
    def __init__(self):
        self.crud = CrudPlantillaTipoPublicacion()

    def agregar(self, id_plantilla, id_tipo_publicacion):
        if self.crud.buscar(id_plantilla, id_tipo_publicacion):
            print(f"Error: Ya existe la relación plantilla_tipo_publicacion ({id_plantilla}, {id_tipo_publicacion}).")
            return None
        datos = {"id_plantilla": id_plantilla, "id_tipo_publicacion": id_tipo_publicacion}
        valido, msg = validar_datos_plantilla_tipo_publicacion(datos)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(id_plantilla, id_tipo_publicacion)

    def eliminar(self, id_plantilla, id_tipo_publicacion):
        if not self.crud.buscar(id_plantilla, id_tipo_publicacion):
            print(f"Error: No existe la relación plantilla_tipo_publicacion ({id_plantilla}, {id_tipo_publicacion}).")
            return False
        return self.crud.eliminar(id_plantilla, id_tipo_publicacion)

    def buscar(self, id_plantilla, id_tipo_publicacion):
        return self.crud.buscar(id_plantilla, id_tipo_publicacion)

    def listar(self):
        return self.crud.listar()
