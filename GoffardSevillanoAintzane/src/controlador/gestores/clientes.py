from dominios.cliente import Cliente
from gestores.base_gestor import BaseGestor

class Clientes(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="cliente",
            fields=[
                "id_cliente", "id_persona", "tipo", "razon_social", "nif", "fecha_registro"
            ],
            id_field="id_cliente"
        )