from src.controlador.crud.crud_plantilla_tipo_publicacion import CRUDPlantillaTipoPublicacion
from src.controlador.dominios.plantilla_tipo_publicacion import PlantillaTipoPublicacion
from src.controlador.base_gestor import BaseGestor

class GestorPlantillaTipoPublicacion(BaseGestor):
    def __init__(self):
        super().__init__()
        self.crud = CRUDPlantillaTipoPublicacion()

    def agregar(self, id_plantilla: int, id_tipo_publicacion: int) -> bool:
        # Aquí puedes validar integridad referencial o reglas de negocio antes de insertar
        # Ejemplo: validar que no exista ya esa relación
        existe = self.crud.buscar((id_plantilla, id_tipo_publicacion))
        if existe:
            return False
        return self.crud.agregar(id_plantilla, id_tipo_publicacion)

    def eliminar(self, id_plantilla: int, id_tipo_publicacion: int) -> bool:
        return self.crud.eliminar(id_plantilla, id_tipo_publicacion)

    def buscar(self, clave: tuple) -> PlantillaTipoPublicacion | None:
        return self.crud.buscar(clave)

    def listar(self, filtro: dict = None) -> list[PlantillaTipoPublicacion]:
        return self.crud.listar(filtro)
