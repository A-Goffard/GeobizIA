from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.redsocial import RedSocial

class RedesSociales(BaseGestor[RedSocial]):
    def __init__(self):
        super().__init__(
            table_name="redsocial",
            fields=[
                "id_red_social", "plataforma", "nombre_cuenta", "credenciales",
                "preferencias_publicacion", "estado_conexion", "ultima_publicacion"
            ],
            id_field="id_red_social",
            domain_class=RedSocial
        )
