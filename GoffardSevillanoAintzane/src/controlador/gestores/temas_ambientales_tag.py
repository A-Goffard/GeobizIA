from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.tema_ambiental_tag import TemaAmbientalTag

class TemasAmbientalesTag(BaseGestor[TemaAmbientalTag]):
    def __init__(self):
        super().__init__(
            table_name="tema_ambiental_tag",
            fields=["id_tema_ambiental", "id_tag"],
            id_fields=["id_tema_ambiental", "id_tag"],
            domain_class=TemaAmbientalTag
        )

    # Podrías añadir validaciones para asegurar que id_tema_ambiental y id_tag existen en sus tablas referenciadas
