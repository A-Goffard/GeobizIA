from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.actividad import Actividad

class Actividades(BaseGestor[Actividad]):
    def __init__(self):
        super().__init__(
            table_name="actividad",
            fields=["id_actividad", "tipo", "nombre", "descripcion", "responsable", "duracion", "coste_economico", "coste_horas", "facturacion", "resultados", "valoracion", "observaciones"],
            id_field="id_actividad",
            domain_class=Actividad
        )