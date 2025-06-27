from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.documento import Documento

class Documentos(BaseGestor[Documento]):
    def __init__(self):
        super().__init__(
            table_name="documento",
            fields=["id_documento", "titulo", "descripcion", "fecha_subida", "tipo", "tematica"],
            id_field="id_documento",
            domain_class=Documento
        )