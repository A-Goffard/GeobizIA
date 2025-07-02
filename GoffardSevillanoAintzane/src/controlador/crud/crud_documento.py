# from .base_crud import BaseCRUD
# from src.controlador.dominios.documento import Documento

# class CrudDocumento(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="documento",
#             fields=["id_documento", "titulo", "descripcion", "fecha_subida", "tipo", "tematica"],
#             id_field="id_documento"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Documento)

#     def leer(self, id_documento):
#         return self.select_by_id(id_documento, Documento)

#     def actualizar(self, id_documento, **kwargs):
#         return self.update(id_documento, kwargs)

#     def eliminar(self, id_documento):
#         return self.delete(id_documento)

#     def existe(self, id_documento):
#         return self.exists(id_documento)

#     def listar(self):
#         return self.select_all(Documento)