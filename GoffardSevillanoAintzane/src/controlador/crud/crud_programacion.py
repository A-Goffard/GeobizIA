from .base_crud import BaseCRUD
from src.controlador.dominios.programacion import Programacion

class CrudProgramacion(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="programacion",
            fields=[
                "id_programacion", "publicacion_id", "red_social_id",
                "fecha_programada", "estado", "notificaciones", "responsable"
            ],
            id_field="id_programacion"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Programacion)

    def leer(self, id_programacion):
        return self.select_by_id(id_programacion, Programacion)

    def actualizar(self, id_programacion, **kwargs):
        return self.update(id_programacion, kwargs)

    def eliminar(self, id_programacion):
        return self.delete(id_programacion)

    def existe(self, id_programacion):
        return self.exists(id_programacion)

    def listar(self):
        return self.select_all(Programacion)

