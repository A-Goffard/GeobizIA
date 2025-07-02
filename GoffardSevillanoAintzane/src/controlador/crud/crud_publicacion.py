# from .base_crud import BaseCRUD
# from src.controlador.dominios.publicacion import Publicacion

# class CrudPublicacion(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="publicacion",
#             fields=[
#                 "id_publicacion",
#                 "titulo",
#                 "contenido",
#                 "autor",
#                 "fecha_creacion",
#                 "estado",
#                 "tags",
#                 "palabras_clave",
#                 "generada_por_ia",
#                 "id_generador_ia",
#                 "feedback_empresa",
#                 "id_tipo_publicacion",
#                 "id_plantilla"
#             ],
#             id_field="id_publicacion"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Publicacion)

#     def leer(self, id_publicacion):
#         return self.select_by_id(id_publicacion, Publicacion)

#     def actualizar(self, id_publicacion, **kwargs):
#         return self.update(id_publicacion, kwargs)

#     def eliminar(self, id_publicacion):
#         return self.delete(id_publicacion)

#     def existe(self, id_publicacion):
#         return self.exists(id_publicacion)

#     def listar(self):
#         return self.select_all(Publicacion)