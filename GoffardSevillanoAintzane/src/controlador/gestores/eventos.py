from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.evento import Evento

class Eventos(BaseGestor[Evento]):
    def __init__(self):
        super().__init__(
            table_name="evento",
            fields=["id_evento", "nombre", "tipo", "lugar", "fecha_comienzo", "fecha_final", "poblacion", "tematica"],
            id_field="id_evento",
            domain_class=Evento
        )