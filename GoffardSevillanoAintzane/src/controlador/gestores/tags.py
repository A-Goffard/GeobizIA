from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.tag import Tag

class Tags(BaseGestor[Tag]):
    def __init__(self):
        super().__init__(
            table_name="tag",
            fields=["id_tag", "palabra_clave", "categoria", "frecuencia_uso"],
            id_field="id_tag",
            domain_class=Tag
        )
