from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.generadoria import GeneradorIA

class GeneradoresIA(BaseGestor[GeneradorIA]):
    def __init__(self):
        super().__init__(
            table_name="generador_IA",
            fields=["id_generador_IA", "id_usuario", "nombre", "descripcion", "tipo"],
            id_field="id_generador_IA",
            domain_class=GeneradorIA
        )

    def agregar(self, **kwargs):
        """
        Agrega un nuevo generador_IA, validando la clave foránea id_usuario.

        Args:
            **kwargs: Diccionario con los valores de los campos (id_generador_IA, id_usuario, etc.).

        Returns:
            GeneradorIA: Objeto GeneradorIA creado, o None si falla.
        """
        if "id_usuario" in kwargs and not self.validar_clave_foranea("id_usuario", kwargs["id_usuario"], "usuario", "id_usuario"):
            print(f"Error: El id_usuario {kwargs['id_usuario']} no existe en la tabla usuario.")
            return None
        return super().agregar(**kwargs)