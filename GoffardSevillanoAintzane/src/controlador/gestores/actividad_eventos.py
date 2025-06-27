from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.actividad_evento import ActividadEvento

class ActividadEventos(BaseGestor[ActividadEvento]):
    def __init__(self):
        super().__init__(
            table_name="actividad_evento",
            fields=["id_actividad_evento", "actividad_id", "evento_id"],
            id_field="id_actividad_evento",
            domain_class=ActividadEvento
        )

    def agregar(self, **kwargs):
        if "actividad_id" in kwargs and not self.validar_clave_foranea("actividad_id", kwargs["actividad_id"], "actividad", "id_actividad"):
            print(f"Error: El actividad_id {kwargs['actividad_id']} no existe en la tabla actividad.")
            return None
        if "evento_id" in kwargs and not self.validar_clave_foranea("evento_id", kwargs["evento_id"], "evento", "id_evento"):
            print(f"Error: El evento_id {kwargs['evento_id']} no existe en la tabla evento.")
            return None
        return super().agregar(**kwargs)

    def actualizar(self, id_objeto, **kwargs):
        if "actividad_id" in kwargs and not self.validar_clave_foranea("actividad_id", kwargs["actividad_id"], "actividad", "id_actividad"):
            print(f"Error: El actividad_id {kwargs['actividad_id']} no existe en la tabla actividad.")
            return None
        if "evento_id" in kwargs and not self.validar_clave_foranea("evento_id", kwargs["evento_id"], "evento", "id_evento"):
            print(f"Error: El evento_id {kwargs['evento_id']} no existe en la tabla evento.")
            return None
        return super().actualizar(id_objeto, **kwargs)
