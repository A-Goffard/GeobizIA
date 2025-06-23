from gestores.base_gestor import BaseGestor

class Eventos(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="evento",
            fields=[
                "id_evento", "nombre", "tipo", "lugar", "fecha_comienzo", "fecha_final", "poblacion", "tematica"
            ],
            id_field="id_evento"
        )
