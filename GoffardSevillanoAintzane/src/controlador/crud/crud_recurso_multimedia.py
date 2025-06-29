from .base_crud import BaseCRUD
from src.controlador.dominios.recurso_multimedia import RecursoMultimedia

class CrudRecursoMultimedia(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="recurso_multimedia",
            fields=["id_recurso_multimedia", "tipo", "titulo", "fecha_subida", "autor"],
            id_field="id_recurso_multimedia"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, RecursoMultimedia)

    def leer(self, id_recurso_multimedia):
        return self.select_by_id(id_recurso_multimedia, RecursoMultimedia)

    def actualizar(self, id_recurso_multimedia, **kwargs):
        return self.update(id_recurso_multimedia, kwargs)

    def eliminar(self, id_recurso_multimedia):
        return self.delete(id_recurso_multimedia)

    def existe(self, id_recurso_multimedia):
        return self.exists(id_recurso_multimedia)

    def listar(self):
        return self.select_all(RecursoMultimedia)
