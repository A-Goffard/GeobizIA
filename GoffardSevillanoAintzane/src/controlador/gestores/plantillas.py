from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.plantilla import Plantilla

class Plantillas(BaseGestor[Plantilla]):
    def __init__(self):
        super().__init__(
            table_name="plantilla",
            fields=["id_plantilla", "titulo", "tipo", "contenido_base", "fecha_creacion", "ultima_modificacion"],
            id_field="id_plantilla",
            domain_class=Plantilla
        )