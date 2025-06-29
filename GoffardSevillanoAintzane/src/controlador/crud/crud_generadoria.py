from .base_crud import BaseCRUD
from src.controlador.dominios.generadoria import GeneradorIA

class CrudGeneradorIA(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="generadoria",
            fields=[
                "id_generador_ia", "nombre", "descripcion", "empresa_id",
                "configuraciones", "ejemplos_estilo", "ultima_generacion"
            ],
            id_field="id_generador_ia"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, GeneradorIA)

    def leer(self, id_generador_ia):
        return self.select_by_id(id_generador_ia, GeneradorIA)

    def actualizar(self, id_generador_ia, **kwargs):
        return self.update(id_generador_ia, kwargs)

    def eliminar(self, id_generador_ia):
        return self.delete(id_generador_ia)

    def existe(self, id_generador_ia):
        return self.exists(id_generador_ia)

    def listar(self):
        return self.select_all(GeneradorIA)