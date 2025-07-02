# from .base_crud import BaseCRUD
# from src.controlador.dominios.fecha_actividad import Fecha_Actividad

# class CrudFechaActividad(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="fecha_actividad",
#             fields=["id_fecha", "fecha"],
#             id_field="id_fecha"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Fecha_Actividad)

#     def leer(self, id_fecha):
#         return self.select_by_id(id_fecha, Fecha_Actividad)

#     def actualizar(self, id_fecha, **kwargs):
#         return self.update(id_fecha, kwargs)

#     def eliminar(self, id_fecha):
#         return self.delete(id_fecha)

#     def existe(self, id_fecha):
#         return self.exists(id_fecha)

#     def listar(self):
#         return self.select_all(Fecha_Actividad)