from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.usuario import Usuario

class Usuarios(BaseGestor[Usuario]):
    def __init__(self):
        super().__init__(
            table_name="usuario",
            fields=["id_usuario", "id_persona", "fecha_nacimiento", "rol", "preferencias", "password"],
            id_field="id_usuario",
            domain_class=Usuario
        )

    def agregar(self, **kwargs):
        """
        Agrega un nuevo usuario, validando la clave foránea id_persona.

        Args:
            **kwargs: Diccionario con los valores de los campos (id_usuario, id_persona, etc.).

        Returns:
            Usuario: Objeto Usuario creado, o None si falla.
        """
        if "id_persona" in kwargs and not self.validar_clave_foranea("id_persona", kwargs["id_persona"], "persona", "id_persona"):
            print(f"Error: El id_persona {kwargs['id_persona']} no existe en la tabla persona.")
            return None
        return super().agregar(**kwargs)