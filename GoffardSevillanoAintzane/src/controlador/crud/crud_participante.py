# from .base_crud import BaseCRUD
# from src.controlador.dominios.participante import Participante

# class CrudParticipante(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="participante",
#             fields=[
#                 "id_participante", "id_persona", "numero_personas_juntas", "rol",
#                 "como_conocer", "actividad_id", "fecha_registro"
#             ],
#             id_field="id_participante"
#         )

#     def crear(self, **kwargs):
#         return self.insert(kwargs, Participante)

#     def leer(self, id_participante):
#         return self.select_by_id(id_participante, Participante)

#     def actualizar(self, id_participante, **kwargs):
#         return self.update(id_participante, kwargs)

#     def eliminar(self, id_participante):
#         return self.delete(id_participante)

#     def existe(self, id_participante):
#         return self.exists(id_participante)

#     def listar(self):
#         return self.select_all(Participante)
