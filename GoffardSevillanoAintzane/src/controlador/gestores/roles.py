from dominios.rol import Rol
from gestores.base_gestor import BaseGestor

class Roles(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="roles",
            fields=[
                "nombre", "tareas_permitidas"
            ],
            id_field="nombre"
        )
