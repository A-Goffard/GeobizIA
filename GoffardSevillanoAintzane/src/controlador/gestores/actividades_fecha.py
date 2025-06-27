from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.actividad_fecha import ActividadFecha

class ActividadesFecha(BaseGestor[ActividadFecha]):
    def __init__(self):
        super().__init__(
            table_name="actividad_fecha",
            fields=["id_actividad_fecha", "actividad_id", "fecha"],
            id_field="id_actividad_fecha",
            domain_class=ActividadFecha
        )

    def agregar(self, **kwargs):
        if "actividad_id" in kwargs and not self.validar_clave_foranea("actividad_id", kwargs["actividad_id"], "actividad", "id_actividad"):
            print(f"Error: El actividad_id {kwargs['actividad_id']} no existe en la tabla actividad.")
            return None
        return super().agregar(**kwargs)

    def actualizar(self, id_objeto, **kwargs):
        if "actividad_id" in kwargs and not self.validar_clave_foranea("actividad_id", kwargs["actividad_id"], "actividad", "id_actividad"):
            print(f"Error: El actividad_id {kwargs['actividad_id']} no existe en la tabla actividad.")
            return None
        return super().actualizar(id_objeto, **kwargs)
