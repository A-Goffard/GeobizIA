from dominios.tags_palabras_clave import Tag
from gestores.base_gestor import BaseGestor

class Tags(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="tag",
            fields=[
                "id_tag", "palabra_clave", "categoria", "frecuencia_uso"
            ],
            id_field="id_tag"
        )
