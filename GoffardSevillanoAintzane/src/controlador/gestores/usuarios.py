from dominios.cliente import Cliente
from gestores.base_gestor import BaseGestor

class Usuarios(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="usuario",
            fields=[
                "id_usuario", "nombre", "apellido", "email", "telefono", "fecha_nacimiento",
                "direccion", "dni", "cp", "poblacion", "pais", "rol", "preferencias", "password"
            ],
            id_field="id_usuario"
        )