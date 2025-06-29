from .base_crud import BaseCRUD
from src.controlador.dominios.factura import Factura

class CrudFactura(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="factura",
            fields=[
                "id_factura", "id_cliente", "tipo", "nombre", "direccion", "nif",
                "fecha_facturacion", "fecha_vencimiento", "concepto", "responsable",
                "iva", "coste_total", "base_imponible", "numero_factura", "tipo_pago", "irpf"
            ],
            id_field="id_factura"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Factura)

    def leer(self, id_factura):
        return self.select_by_id(id_factura, Factura)

    def actualizar(self, id_factura, **kwargs):
        return self.update(id_factura, kwargs)

    def eliminar(self, id_factura):
        return self.delete(id_factura)

    def existe(self, id_factura):
        return self.exists(id_factura)

    def listar(self):
        return self.select_all(Factura)