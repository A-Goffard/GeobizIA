# from .base_crud import BaseCRUD
# from src.controlador.dominios.redsocial import RedSocial

# class CrudRedSocial(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="redsocial",
#             fields=[
#                 "id_red_social", "plataforma", "nombre_cuenta", "credenciales",
#                 "preferencias_publicacion", "estado_conexion", "ultima_publicacion"
#             ],
#             id_field="id_red_social"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, RedSocial)

#     def leer(self, id_red_social):
#         return self.select_by_id(id_red_social, RedSocial)

#     def actualizar(self, id_red_social, **kwargs):
#         return self.update(id_red_social, kwargs)

#     def eliminar(self, id_red_social):
#         return self.delete(id_red_social)

#     def existe(self, id_red_social):
#         return self.exists(id_red_social)

#     def listar(self):
#         return self.select_all(RedSocial)
