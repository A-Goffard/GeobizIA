# from .base_crud import BaseCRUD
# from src.controlador.dominios.tag import Tag

# class CrudTag(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="tag",
#             fields=["id_tag", "palabra_clave", "categoria", "frecuencia_uso"],
#             id_field="id_tag"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Tag)

#     def leer(self, id_tag):
#         return self.select_by_id(id_tag, Tag)

#     def actualizar(self, id_tag, **kwargs):
#         return self.update(id_tag, kwargs)

#     def eliminar(self, id_tag):
#         return self.delete(id_tag)

#     def existe(self, id_tag):
#         return self.exists(id_tag)

#     def listar(self):
#         return self.select_all(Tag)
