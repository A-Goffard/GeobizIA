from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.recurso_multimedia import RecursoMultimedia

class RecursosMultimedia(BaseGestor[RecursoMultimedia]):
    def __init__(self):
        super().__init__(
            table_name="recurso_multimedia",
            fields=["id_recurso_multimedia", "tipo", "titulo", "fecha_subida", "autor"],
            id_field="id_recurso_multimedia",
            domain_class=RecursoMultimedia
        )
