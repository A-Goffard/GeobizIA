# from .base_crud import BaseCRUD
# from src.controlador.dominios.plantilla import Plantilla

# class CrudPlantilla(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="plantilla",
#             fields=["id_plantilla", "titulo", "tipo", "contenido_base", "fecha_creacion", "ultima_modificacion"],
#             id_field="id_plantilla"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Plantilla)

#     def leer(self, id_plantilla):
#         return self.select_by_id(id_plantilla, Plantilla)

#     def actualizar(self, id_plantilla, **kwargs):
#         return self.update(id_plantilla, kwargs)

#     def eliminar(self, id_plantilla):
#         return self.delete(id_plantilla)

#     def existe(self, id_plantilla):
#         return self.exists(id_plantilla)

#     def listar(self):
#         return self.select_all(Plantilla)