from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.tema_ambiental import Tema_Ambiental

class Temas_Ambientales(BaseGestor[Tema_Ambiental]):
    def __init__(self):
        super().__init__(
            table_name="tema_ambiental",
            fields=["id_tema_ambiental", "nombre", "descripcion"],
            id_field="id_tema_ambiental",
            domain_class=Tema_Ambiental
        )