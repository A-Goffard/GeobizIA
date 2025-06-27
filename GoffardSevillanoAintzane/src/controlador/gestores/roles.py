from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.rol import Rol

class Roles(BaseGestor[Rol]):
    def __init__(self):
        super().__init__(
            table_name="rol",
            fields=["id_rol", "nombre"],
            id_field="id_rol",
            domain_class=Rol
        )