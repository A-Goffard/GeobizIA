from dominios.actividad import Actividad
from gestores.base_gestor import BaseGestor

class Actividades(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="actividad",
            fields=[
                "id_actividad", "tipo", "nombre", "descripcion", "responsable", "duracion", "coste_economico", "coste_horas", "facturacion", "resultados", "valoracion", "modificaciones"
            ],
            id_field="id_actividad"
        )
