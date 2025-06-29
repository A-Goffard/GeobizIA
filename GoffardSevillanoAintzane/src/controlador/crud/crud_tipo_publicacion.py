from .base_crud import BaseCRUD
from src.controlador.dominios.tipo_publicacion import Tipo_Publicacion

class CrudTipoPublicacion(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="tipo_publicacion",
            fields=["id_tipo_publicacion", "nombre", "descripcion"],
            id_field="id_tipo_publicacion"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Tipo_Publicacion)

    def leer(self, id_tipo_publicacion):
        return self.select_by_id(id_tipo_publicacion, Tipo_Publicacion)

    def actualizar(self, id_tipo_publicacion, **kwargs):
        return self.update(id_tipo_publicacion, kwargs)

    def eliminar(self, id_tipo_publicacion):
        return self.delete(id_tipo_publicacion)

    def existe(self, id_tipo_publicacion):
        return self.exists(id_tipo_publicacion)

    def listar(self):
        return self.select_all(Tipo_Publicacion)