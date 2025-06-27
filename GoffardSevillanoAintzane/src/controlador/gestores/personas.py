from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.persona import Persona

class Personas(BaseGestor[Persona]):
    def __init__(self):
        super().__init__(
            table_name="persona",
            fields=["id_persona", "nombre", "apellido", "email", "telefono", "dni", "direccion", "cp", "poblacion", "pais"],
            id_field="id_persona",
            domain_class=Persona
        )