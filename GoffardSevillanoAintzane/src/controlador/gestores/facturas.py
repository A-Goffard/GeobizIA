from dominios.factura import Factura
from gestores.base_gestor import BaseGestor

class Facturas(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="factura",
            fields=[
                "id_factura", "id_cliente", "fecha_facturacion", "fecha_vencimiento", "concepto", "responsable", "iva", "coste_total", "base_imponible", "numero_factura", "tipo_pago", "irpf"
            ],
            id_field="id_factura"
        )
