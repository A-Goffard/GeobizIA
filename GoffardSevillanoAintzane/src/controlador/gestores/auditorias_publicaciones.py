from dominios.auditoria_publicacion import AuditoriaPublicacion
from gestores.base_gestor import BaseGestor

class AuditoriasPublicaciones(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="auditoria_publicacion",
            fields=[
                "id_auditoria_publicacion", "publicacion_id", "generador_ia_id", "fecha_generacion", "usuario_id", "parametros_entrada", "resultado", "observaciones"
            ],
            id_field="id_auditoria_publicacion"
        )