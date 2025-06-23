from dominios.recurso_multimedia import RecursoMultimedia
from gestores.base_gestor import BaseGestor

class RecursosMultimedia(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="recurso_multimedia",
            fields=[
                "id_recurso_multimedia", "tipo", "titulo", "fecha_subida", "autor", "relaciones"
            ],
            id_field="id_recurso_multimedia"
        )
