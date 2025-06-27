from src.controlador.crud.crud_tipo_publicacion_redsocial import CRUDTipoPublicacionRedSocial
from src.controlador.dominios.tipo_publicacion_redsocial import TipoPublicacionRedSocial
from src.controlador.base_gestor import BaseGestor

class GestorTipoPublicacionRedSocial(BaseGestor):
    def __init__(self):
        super().__init__()
        self.crud = CRUDTipoPublicacionRedSocial()

    def agregar(self, id_tipo_publicacion: int, id_red_social: int) -> bool:
        # Validar que no exista ya esta relación para evitar duplicados
        if self.crud.buscar((id_tipo_publicacion, id_red_social)):
            return False
        return self.crud.agregar(id_tipo_publicacion, id_red_social)

    def eliminar(self, id_tipo_publicacion: int, id_red_social: int) -> bool:
        return self.crud.eliminar(id_tipo_publicacion, id_red_social)

    def buscar(self, clave: tuple) -> TipoPublicacionRedSocial | None:
        return self.crud.buscar(clave)

    def listar(self, filtro: dict = None) -> list[TipoPublicacionRedSocial]:
        return self.crud.listar(filtro)
