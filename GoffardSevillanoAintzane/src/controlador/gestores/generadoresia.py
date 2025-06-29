from src.controlador.crud.crud_generadoria import CrudGeneradorIA
from src.controlador.validaciones.validar_generadoria import validar_datos_generadoria

class GeneradoresIA:
    def __init__(self):
        self.crud = CrudGeneradorIA()

    def agregar(self, **kwargs):
        id_generador_ia = kwargs.get("id_generador_ia")
        if id_generador_ia is not None and self.crud.existe(id_generador_ia):
            print(f"Error: Ya existe un generador IA con id_generador_ia={id_generador_ia}.")
            return None
        valido, msg = validar_datos_generadoria(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_generador_ia):
        if not self.crud.existe(id_generador_ia):
            print(f"Error: No existe un generador IA con id_generador_ia={id_generador_ia}.")
            return False
        return self.crud.eliminar(id_generador_ia)

    def buscar(self, id_generador_ia):
        return self.crud.leer(id_generador_ia)

    def actualizar(self, id_generador_ia, **kwargs):
        valido, msg = validar_datos_generadoria(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_generador_ia, **kwargs)

    def existe(self, id_generador_ia):
        return self.crud.existe(id_generador_ia)

    def listar(self):
        return self.crud.listar()