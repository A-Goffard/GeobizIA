from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.auditoria_publicacion import Auditoria_Publicacion

class Auditorias_Publicacion(BaseGestor[Auditoria_Publicacion]):
    def __init__(self):
        super().__init__(
            table_name="auditoria_publicacion",
            fields=["id_auditoria", "id_publicacion", "usuario_id", "fecha", "accion", "descripcion", "nivel"],
            id_field="id_auditoria",
            domain_class=Auditoria_Publicacion
        )

    def agregar(self, **kwargs):
        """
        Agrega un nuevo registro de auditoria_publicacion, validando las claves foráneas id_publicacion y usuario_id.

        Args:
            **kwargs: Diccionario con los valores de los campos (id_auditoria, id_publicacion, usuario_id, etc.).

        Returns:
            Auditoria_Publicacion: Objeto Auditoria_Publicacion creado, o None si falla.
        """
        if "id_publicacion" in kwargs and not self.validar_clave_foranea("id_publicacion", kwargs["id_publicacion"], "publicacion", "id_publicacion"):
            print(f"Error: El id_publicacion {kwargs['id_publicacion']} no existe en la tabla publicacion.")
            return None
        if "usuario_id" in kwargs and not self.validar_clave_foranea("usuario_id", kwargs["usuario_id"], "usuario", "id_usuario"):
            print(f"Error: El usuario_id {kwargs['usuario_id']} no existe en la tabla usuario.")
            return None
        return super().agregar(**kwargs)