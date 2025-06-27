from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.cliente import Cliente

class Clientes(BaseGestor[Cliente]):
    def __init__(self):
        super().__init__(
            table_name="cliente",
            fields=["id_cliente", "id_persona", "tipo", "razon_social", "nif", "fecha_registro"],
            id_field="id_cliente",
            domain_class=Cliente
        )

    def agregar(self, **kwargs):
        if "id_persona" in kwargs and not self.validar_clave_foranea("id_persona", kwargs["id_persona"], "persona", "id_persona"):
            print(f"Error: El id_persona {kwargs['id_persona']} no existe en la tabla persona.")
            return None
        return super().agregar(**kwargs)