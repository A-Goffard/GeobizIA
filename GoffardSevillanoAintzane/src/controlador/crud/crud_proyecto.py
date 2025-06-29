from .base_crud import BaseCRUD
from src.controlador.dominios.proyecto import Proyecto

class CrudProyecto(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="proyecto",
            fields=[
                "id_proyecto", "nombre", "descripcion", "fecha_inicio", "fecha_fin",
                "poblacion", "responsable", "estado", "objetivos", "presupuesto"
            ],
            id_field="id_proyecto"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Proyecto)

    def leer(self, id_proyecto):
        return self.select_by_id(id_proyecto, Proyecto)

    def actualizar(self, id_proyecto, **kwargs):
        return self.update(id_proyecto, kwargs)

    def eliminar(self, id_proyecto):
        return self.delete(id_proyecto)

    def existe(self, id_proyecto):
        return self.exists(id_proyecto)

    def listar(self):
        return self.select_all(Proyecto)
