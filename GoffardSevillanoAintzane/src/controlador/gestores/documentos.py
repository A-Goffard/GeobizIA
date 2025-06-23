from dominios.documento import Documento
from gestores.base_gestor import BaseGestor

class GestorDocumentos(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="documento",
            fields=[
                "id_documento", "titulo", "descripcion", "fecha_subida", "tipo", "tematica"
            ],
            id_field="id_documento"
        )
