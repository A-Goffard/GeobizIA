# from .base_crud import BaseCRUD
# from src.controlador.dominios.log_sistema import Log_Sistema

# class CrudLogSistema(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="log_sistema",
#             fields=["id_log_sistema", "fecha", "usuario_id", "accion", "descripcion", "nivel"],
#             id_field="id_log_sistema"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Log_Sistema)

#     def leer(self, id_log_sistema):
#         return self.select_by_id(id_log_sistema, Log_Sistema)

#     def actualizar(self, id_log_sistema, **kwargs):
#         return self.update(id_log_sistema, kwargs)

#     def eliminar(self, id_log_sistema):
#         return self.delete(id_log_sistema)

#     def existe(self, id_log_sistema):
#         return self.exists(id_log_sistema)

#     def listar(self):
#         return self.select_all(Log_Sistema)