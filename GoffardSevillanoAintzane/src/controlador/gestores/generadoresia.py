from gestores.base_gestor import BaseGestor

class GeneradoresIA(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="generadoria",
            fields=[
                "id_generador_ia", "nombre", "descripcion", "empresa_id", "configuraciones", "ejemplos_estilo", "ultima_generacion"
            ],
            id_field="id_generador_ia"
        )
