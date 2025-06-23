from dominios.cliente import Cliente
from gestores.base_gestor import BaseGestor

class Clientes(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="cliente",
            fields=[
                "id_cliente", "tipo", "nombre", "apellido", "razon_social", "nif", "dni", "email", "telefono", "direccion", "cp", "poblacion", "pais", "fecha_registro"
            ],
            id_field="id_cliente"
        )