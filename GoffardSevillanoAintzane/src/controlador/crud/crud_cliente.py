from .base_crud import BaseCRUD
from src.controlador.dominios.cliente import Cliente

class CrudCliente(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="cliente",
            fields=["id_cliente", "id_persona", "tipo", "razon_social", "nif", "fecha_registro"],
            id_field="id_cliente"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Cliente)

    def leer(self, id_cliente):
        return self.select_by_id(id_cliente, Cliente)

    def actualizar(self, id_cliente, **kwargs):
        return self.update(id_cliente, kwargs)

    def eliminar(self, id_cliente):
        return self.delete(id_cliente)

    def existe(self, id_cliente):
        return self.exists(id_cliente)

    def listar(self):
        return self.select_all(Cliente)