from gestores.base_gestor import BaseGestor

class Proyectos(BaseGestor):
    def __init__(self):
        super().__init__(
            table_name="proyecto",
            fields=[
                "id_proyecto", "nombre", "descripcion", "fecha_inicio", "fecha_fin", "poblacion", "responsable", "estado", "objetivos", "presupuesto"
            ],
            id_field="id_proyecto"
        )
