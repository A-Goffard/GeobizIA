from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.publicacion import Publicacion

class Publicaciones(BaseGestor[Publicacion]):
    def __init__(self):
        super().__init__(
            table_name="publicacion",
            fields=["id_publicacion", "id_generador_IA", "id_tipo_publicacion", "contenido", "fecha_creacion"],
            id_field="id_publicacion",
            domain_class=Publicacion
        )

    def agregar(self, **kwargs):
        """
        Agrega una nueva publicación, validando las claves foráneas id_generador_IA y id_tipo_publicacion.

        Args:
            **kwargs: Diccionario con los valores de los campos (id_publicacion, id_generador_IA, id_tipo_publicacion, etc.).

        Returns:
            Publicacion: Objeto Publicacion creado, o None si falla.
        """
        if "id_generador_IA" in kwargs and not self.validar_clave_foranea("id_generador_IA", kwargs["id_generador_IA"], "generador_IA", "id_generador_IA"):
            print(f"Error: El id_generador_IA {kwargs['id_generador_IA']} no existe en la tabla generador_IA.")
            return None
        if "id_tipo_publicacion" in kwargs and not self.validar_clave_foranea("id_tipo_publicacion", kwargs["id_tipo_publicacion"], "tipo_publicacion", "id_tipo_publicacion"):
            print(f"Error: El id_tipo_publicacion {kwargs['id_tipo_publicacion']} no existe en la tabla tipo_publicacion.")
            return None
        return super().agregar(**kwargs)