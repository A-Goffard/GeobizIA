from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.documento_tag import DocumentoTag

class DocumentosTag(BaseGestor[DocumentoTag]):
    def __init__(self):
        super().__init__(
            table_name="documento_tag",
            fields=["id_documento", "id_tag"],
            id_fields=["id_documento", "id_tag"],
            domain_class=DocumentoTag
        )

    # Aquí puedes añadir validaciones específicas para asegurarte
    # que el id_documento y el id_tag existen en sus tablas correspondientes
