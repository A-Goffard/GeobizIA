from gestores.base_gestor import BaseGestor

class Programaciones(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="programacion",
            fields=[
                "id_programacion", "publicacion_id", "red_social_id", "fecha_programada", "estado", "notificaciones", "responsable"
            ],
            id_field="id_programacion"
        )

