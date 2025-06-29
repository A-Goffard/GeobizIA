from src.controlador.crud.crud_persona import CrudPersona
from src.controlador.validaciones.validar_persona import validar_datos_persona

class Personas:
    def __init__(self):
        self.crud = CrudPersona()

    def agregar(self, **kwargs):
        id_persona = kwargs.get("id_persona")
        if id_persona is not None and self.crud.existe(id_persona):
            print(f"Error: Ya existe una persona con id_persona={id_persona}.")
            return None
        valido, msg = validar_datos_persona(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_persona):
        if not self.crud.existe(id_persona):
            print(f"Error: No existe una persona con id_persona={id_persona}.")
            return False
        return self.crud.eliminar(id_persona)

    def buscar(self, id_persona):
        return self.crud.leer(id_persona)

    def actualizar(self, id_persona, **kwargs):
        valido, msg = validar_datos_persona(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_persona, **kwargs)

    def existe(self, id_persona):
        return self.crud.existe(id_persona)

    def listar(self):
        return self.crud.listar()