from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.log_sistema import Log_Sistema

class Logs_Sistema(BaseGestor[Log_Sistema]):
    def __init__(self):
        super().__init__(
            table_name="log_sistema",
            fields=["id_log_sistema", "fecha", "usuario_id", "accion", "descripcion", "nivel"],
            id_field="id_log_sistema",
            domain_class=Log_Sistema
        )

    def agregar(self, **kwargs):
        """
        Agrega un nuevo log_sistema, validando la clave foránea usuario_id.

        Args:
            **kwargs: Diccionario con los valores de los campos (id_log_sistema, usuario_id, etc.).

        Returns:
            Log_Sistema: Objeto Log_Sistema creado, o None si falla.
        """
        if "usuario_id" in kwargs and not self.validar_clave_foranea("usuario_id", kwargs["usuario_id"], "usuario", "id_usuario"):
            print(f"Error: El usuario_id {kwargs['usuario_id']} no existe en la tabla usuario.")
            return None
        return super().agregar(**kwargs)