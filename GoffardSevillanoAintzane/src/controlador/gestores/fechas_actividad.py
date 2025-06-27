from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.fecha_actividad import FechaActividad

class FechasActividad(BaseGestor[FechaActividad]):
    def __init__(self):
        super().__init__(
            table_name="fecha_actividad",
            fields=["id_fecha", "fecha"],
            id_field="id_fecha",
            domain_class=FechaActividad
        )