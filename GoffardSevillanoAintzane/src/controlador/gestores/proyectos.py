from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.proyecto import Proyecto

class Proyectos(BaseGestor[Proyecto]):
    def __init__(self):
        super().__init__(
            table_name="proyecto",
            fields=["id_proyecto", "nombre", "descripcion", "fecha_inicio", "fecha_fin", "poblacion", "responsable", "estado", "objetivos", "presupuesto"],
            id_field="id_proyecto",
            domain_class=Proyecto
        )