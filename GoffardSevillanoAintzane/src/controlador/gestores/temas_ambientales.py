from dominios.tema_ambiental import TemaAmbiental
from gestores.base_gestor import BaseGestor

class TemasAmbientales(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="tema_ambiental",
            fields=[
                "id_tema_ambiental", "nombre", "descripcion", "relevancia", "relacion_actividades", "relacion_publicaciones"
            ],
            id_field="id_tema_ambiental"
        )
