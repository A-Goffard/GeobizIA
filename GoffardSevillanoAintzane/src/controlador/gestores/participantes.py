from dominios.participante import Participante
from gestores.base_gestor import BaseGestor

class Participantes(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="participante",
            fields=[
                "id_participante", "nombre", "apellido", "email", "telefono", "numero_personas_juntas", "rol", "como_conocer", "actividad_id", "fecha_registro"
            ],
            id_field="id_participante"
        )