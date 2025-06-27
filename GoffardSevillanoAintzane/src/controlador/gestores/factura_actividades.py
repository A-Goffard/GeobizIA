from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.factura_actividad import FacturaActividad

class FacturaActividades(BaseGestor[FacturaActividad]):
    def __init__(self):
        super().__init__(
            table_name="factura_actividad",
            fields=["id_factura_actividad", "actividad_id", "factura_id", "monto", "fecha"],
            id_field="id_factura_actividad",
            domain_class=FacturaActividad
        )

    def agregar(self, **kwargs):
        if "actividad_id" in kwargs and not self.validar_clave_foranea("actividad_id", kwargs["actividad_id"], "actividad", "id_actividad"):
            print(f"Error: El actividad_id {kwargs['actividad_id']} no existe en la tabla actividad.")
            return None
        if "factura_id" in kwargs and not self.validar_clave_foranea("factura_id", kwargs["factura_id"], "factura", "id_factura"):
            print(f"Error: El factura_id {kwargs['factura_id']} no existe en la tabla factura.")
            return None
        return super().agregar(**kwargs)

    def actualizar(self, id_objeto, **kwargs):
        if "actividad_id" in kwargs and not self.validar_clave_foranea("actividad_id", kwargs["actividad_id"], "actividad", "id_actividad"):
            print(f"Error: El actividad_id {kwargs['actividad_id']} no existe en la tabla actividad.")
            return None
        if "factura_id" in kwargs and not self.validar_clave_foranea("factura_id", kwargs["factura_id"], "factura", "id_factura"):
            print(f"Error: El factura_id {kwargs['factura_id']} no existe en la tabla factura.")
            return None
        return super().actualizar(id_objeto, **kwargs)
