from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.programacion import Programacion

class Programaciones(BaseGestor[Programacion]):
    def __init__(self):
        super().__init__(
            table_name="programacion",
            fields=["id_programacion", "publicacion_id", "red_social_id", "fecha_programada", "estado", "notificaciones", "responsable"],
            id_field="id_programacion",
            domain_class=Programacion
        )

    def agregar(self, **kwargs):
            if "publicacion_id" in kwargs and not self.validar_clave_foranea("publicacion_id", kwargs["publicacion_id"], "publicacion", "id_publicacion"):
                print(f"Error: El publicacion_id {kwargs['publicacion_id']} no existe en la tabla publicacion.")
                return None
            if "red_social_id" in kwargs and not self.validar_clave_foranea("red_social_id", kwargs["red_social_id"], "redsocial", "id_red_social"):
                print(f"Error: El red_social_id {kwargs['red_social_id']} no existe en la tabla redsocial.")
                return None
            return super().agregar(**kwargs)

    def actualizar(self, id_programacion, **kwargs):
        if "publicacion_id" in kwargs and not self.validar_clave_foranea("publicacion_id", kwargs["publicacion_id"], "publicacion", "id_publicacion"):
            print(f"Error: El publicacion_id {kwargs['publicacion_id']} no existe en la tabla publicacion.")
            return False
        if "red_social_id" in kwargs and not self.validar_clave_foranea("red_social_id", kwargs["red_social_id"], "redsocial", "id_red_social"):
            print(f"Error: El red_social_id {kwargs['red_social_id']} no existe en la tabla redsocial.")
            return False
        return super().actualizar(id_programacion, **kwargs)