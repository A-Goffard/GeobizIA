from gestores.base_gestor import BaseGestor

class RedesSociales(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="redsocial",
            fields=[
                "id_red_social", "plataforma", "nombre_cuenta", "credenciales", "preferencias_publicacion", "estado_conexion", "ultima_publicacion"
            ],
            id_field="id_red_social"
        )
