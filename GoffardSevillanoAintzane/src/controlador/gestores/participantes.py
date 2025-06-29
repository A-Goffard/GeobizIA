from src.controlador.crud.crud_participante import CrudParticipante
from src.controlador.validaciones.validar_participante import validar_datos_participante

class Participantes:
    def __init__(self):
        self.crud = CrudParticipante()

    def agregar(self, **kwargs):
        id_participante = kwargs.get("id_participante")
        if id_participante is not None and self.crud.existe(id_participante):
            print(f"Error: Ya existe un participante con id_participante={id_participante}.")
            return None
        valido, msg = validar_datos_participante(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_participante):
        if not self.crud.existe(id_participante):
            print(f"Error: No existe un participante con id_participante={id_participante}.")
            return False
        return self.crud.eliminar(id_participante)

    def buscar(self, id_participante):
        return self.crud.leer(id_participante)

    def actualizar(self, id_participante, **kwargs):
        valido, msg = validar_datos_participante(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_participante, **kwargs)

    def existe(self, id_participante):
        return self.crud.existe(id_participante)

    def listar(self):
        return self.crud.listar()