from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.tipo_publicacion import Tipo_Publicacion

class Tipos_Publicacion(BaseGestor[Tipo_Publicacion]):
    def __init__(self):
        super().__init__(
            table_name="tipo_publicacion",
            fields=["id_tipo_publicacion", "nombre", "descripcion"],
            id_field="id_tipo_publicacion",
            domain_class=Tipo_Publicacion
        )