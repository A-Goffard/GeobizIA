from dominios.log_sistema import LogSistema
from gestores.base_gestor import BaseGestor

class LogsSistema(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="log_sistema",
            fields=[
                "id_log_sistema", "fecha", "usuario_id", "accion", "descripcion", "nivel"
            ],
            id_field="id_log_sistema"
        )