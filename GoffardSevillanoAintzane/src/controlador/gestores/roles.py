from .base_gestor import BaseGestor
from dominios.rol import Rol

class Roles(BaseGestor[Rol]):
    def __init__(self):
        super().__init__(
            table_name="rol",
            fields=["id_rol", "nombre", "descripcion"],
            id_field="id_rol",
            domain_class=Rol
        )