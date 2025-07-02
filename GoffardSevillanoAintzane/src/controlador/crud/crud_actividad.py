# from .base_crud import BaseCRUD
# from src.controlador.dominios.actividad import Actividad

# class CrudActividad(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="actividad",
#             fields=[
#                 "id_actividad", "tipo", "nombre", "descripcion", "responsable",
#                 "duracion", "coste_economico", "coste_horas", "facturacion",
#                 "resultados", "valoracion", "observaciones"
#             ],
#             id_field="id_actividad"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Actividad)

#     def leer(self, id_actividad):
#         return self.select_by_id(id_actividad, Actividad)

#     def actualizar(self, id_actividad, **kwargs):
#         return self.update(id_actividad, kwargs)

#     def eliminar(self, id_actividad):
#         return self.delete(id_actividad)

#     def existe(self, id_actividad):
#         return self.exists(id_actividad)

#     def listar(self):
#         return self.select_all(Actividad)