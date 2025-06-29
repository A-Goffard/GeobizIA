from .base_crud import BaseCRUD
from src.controlador.dominios.tema_ambiental import Tema_Ambiental

class CrudTemaAmbiental(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="tema_ambiental",
            fields=["id_tema_ambiental", "nombre", "descripcion", "relevancia"],
            id_field="id_tema_ambiental"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Tema_Ambiental)

    def leer(self, id_tema_ambiental):
        return self.select_by_id(id_tema_ambiental, Tema_Ambiental)

    def actualizar(self, id_tema_ambiental, **kwargs):
        return self.update(id_tema_ambiental, kwargs)

    def eliminar(self, id_tema_ambiental):
        return self.delete(id_tema_ambiental)

    def existe(self, id_tema_ambiental):
        return self.exists(id_tema_ambiental)

    def listar(self):
        return self.select_all(Tema_Ambiental)