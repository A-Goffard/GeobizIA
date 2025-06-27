from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.factura import Factura

class Facturas(BaseGestor[Factura]):
    def __init__(self):
        super().__init__(
            table_name="factura",
            fields=["id_factura", "id_cliente", "tipo", "nombre", "direccion", "nif", "fecha_facturacion", "fecha_vencimiento", "concepto", "responsable", "iva", "coste_total", "base_imponible", "numero_factura", "tipo_pago", "irpf"],
            id_field="id_factura",
            domain_class=Factura
        )

    def agregar(self, **kwargs):
        """
        Agrega una nueva factura, validando la clave foránea id_cliente.

        Args:
            **kwargs: Diccionario con los valores de los campos (id_factura, id_cliente, etc.).

        Returns:
            Factura: Objeto Factura creado, o None si falla.
        """
        if "id_cliente" in kwargs and not self.validar_clave_foranea("id_cliente", kwargs["id_cliente"], "cliente", "id_cliente"):
            print(f"Error: El id_cliente {kwargs['id_cliente']} no existe en la tabla cliente.")
            return None
        return super().agregar(**kwargs)