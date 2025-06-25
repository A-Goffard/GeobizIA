from dominios.plantilla import Plantilla
from gestores.base_gestor import BaseGestor

class Plantillas(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="plantilla",
            fields=[
                "id_plantilla", "titulo", "tipo", "contenido_base", "fecha_creacion", "ultima_modificacion"
            ],
            id_field="id_plantilla"
        )
