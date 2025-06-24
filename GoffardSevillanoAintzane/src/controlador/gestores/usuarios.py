from dominios.cliente import Cliente
from gestores.base_gestor import BaseGestor

class Usuarios(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="usuario",
            fields=[
                "id_usuario", "id_persona", "fecha_nacimiento", "rol", "preferencias", "password"
            ],
            id_field="id_usuario"
        )