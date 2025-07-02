# from .base_crud import BaseCRUD
# from src.controlador.dominios.cliente import Cliente

# class CrudCliente(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="cliente",
#             fields=["id_cliente", "id_persona", "tipo", "razon_social", "nif", "fecha_registro"],
#             id_field="id_cliente"
#         )

#     def crear(self, cliente: Cliente):
#         values = vars(cliente)
#         return self.insert(values, Cliente)

#     def leer(self, cliente: Cliente):
#         return self.select_by_id(cliente.id_cliente, Cliente)

#     def actualizar(self, cliente: Cliente):
#         values = vars(cliente)
#         return self.update(cliente.id_cliente, values)

#     def eliminar(self, cliente: Cliente):
#         return self.delete(cliente.id_cliente)

#     def existe(self, id_cliente):
#         return self.exists(id_cliente)

#     def listar(self):
#         return self.select_all(Cliente)