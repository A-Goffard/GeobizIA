from dominios.publicacion import Publicacion
from gestores.base_gestor import BaseGestor

class Publicaciones(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="publicacion",
            fields=[
                "id_publicacion", "titulo", "contenido", "autor", "fecha_creacion", "estado", "tags", "palabras_clave", "generada_por_ia", "id_generador_ia", "feedback_empresa", "id_tipo_publicacion", "id_plantilla"
            ],
            id_field="id_publicacion"
        )
