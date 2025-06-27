from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.empresa import Empresa

class Empresas(BaseGestor[Empresa]):
    def __init__(self):
        super().__init__(
            table_name="empresa",
            fields=["id_empresa", "id_persona", "razon_social", "nif", "sector", "tamano", "fecha_registro"],
            id_field="id_empresa",
            domain_class=Empresa
        )

    def agregar(self, **kwargs):
        """
        Agrega una nueva empresa, validando la clave foránea id_persona.

        Args:
            **kwargs: Diccionario con los valores de los campos (id_empresa, id_persona, etc.).

        Returns:
            Empresa: Objeto Empresa creado, o None si falla.
        """
        if "id_persona" in kwargs and not self.validar_clave_foranea("id_persona", kwargs["id_persona"], "persona", "id_persona"):
            print(f"Error: El id_persona {kwargs['id_persona']} no existe en la tabla persona.")
            return None
        return super().agregar(**kwargs)