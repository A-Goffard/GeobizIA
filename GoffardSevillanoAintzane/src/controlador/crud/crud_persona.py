# from .base_crud import BaseCRUD
# from src.controlador.dominios.persona import Persona

# class CrudPersona(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="persona",
#             fields=[
#                 "id_persona", "nombre", "apellido", "email", "telefono",
#                 "dni", "direccion", "cp", "poblacion", "pais"
#             ],
#             id_field="id_persona"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Persona)

#     def leer(self, id_persona):
#         return self.select_by_id(id_persona, Persona)

#     def actualizar(self, id_persona, **kwargs):
#         return self.update(id_persona, kwargs)

#     def eliminar(self, id_persona):
#         return self.delete(id_persona)

#     def existe(self, id_persona):
#         return self.exists(id_persona)

#     def listar(self):
#         return self.select_all(Persona)