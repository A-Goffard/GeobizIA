from gestores.base_gestor import BaseGestor

class Empresas(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="empresa",
            fields=[
                "id_empresa", "nombre", "sector", "logo", "ubicacion"
            ],
            id_field="id_empresa"
        )
