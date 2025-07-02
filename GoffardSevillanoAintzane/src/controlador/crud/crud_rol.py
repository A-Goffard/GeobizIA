# from .base_crud import BaseCRUD
# from src.controlador.dominios.rol import Rol

# class CrudRol(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="rol",
#             fields=["id_rol", "nombre", "descripcion"],
#             id_field="id_rol"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Rol)

#     def leer(self, id_rol):
#         return self.select_by_id(id_rol, Rol)

#     def actualizar(self, id_rol, **kwargs):
#         return self.update(id_rol, kwargs)

#     def eliminar(self, id_rol):
#         return self.delete(id_rol)

#     def existe(self, id_rol):
#         return self.exists(id_rol)

#     def listar(self):
#         return self.select_all(Rol)