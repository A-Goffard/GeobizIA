from .base_crud import BaseCRUD
from src.controlador.dominios.empresa import Empresa

class CrudEmpresa(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="empresa",
            fields=["id_empresa", "nombre", "sector", "logo", "ubicacion"],
            id_field="id_empresa"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Empresa)

    def leer(self, id_empresa):
        return self.select_by_id(id_empresa, Empresa)

    def actualizar(self, id_empresa, **kwargs):
        return self.update(id_empresa, kwargs)

    def eliminar(self, id_empresa):
        return self.delete(id_empresa)

    def existe(self, id_empresa):
        return self.exists(id_empresa)

    def listar(self):
        return self.select_all(Empresa)