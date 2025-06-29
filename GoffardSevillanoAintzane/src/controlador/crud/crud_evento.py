from .base_crud import BaseCRUD
from src.controlador.dominios.evento import Evento

class CrudEvento(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="evento",
            fields=[
                "id_evento", "nombre", "tipo", "lugar", "fecha_comienzo",
                "fecha_final", "poblacion", "tematica"
            ],
            id_field="id_evento"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Evento)

    def leer(self, id_evento):
        return self.select_by_id(id_evento, Evento)

    def actualizar(self, id_evento, **kwargs):
        return self.update(id_evento, kwargs)

    def eliminar(self, id_evento):
        return self.delete(id_evento)

    def existe(self, id_evento):
        return self.exists(id_evento)

    def listar(self):
        return self.select_all(Evento)