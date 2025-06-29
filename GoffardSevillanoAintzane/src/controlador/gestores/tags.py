from src.controlador.crud.crud_tag import CrudTag
from src.controlador.validaciones.validar_tag import validar_datos_tag

class Tags:
    def __init__(self):
        self.crud = CrudTag()

    def agregar(self, **kwargs):
        id_tag = kwargs.get("id_tag")
        if id_tag is not None and self.crud.existe(id_tag):
            print(f"Error: Ya existe un tag con id_tag={id_tag}.")
            return None
        valido, msg = validar_datos_tag(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_tag):
        if not self.crud.existe(id_tag):
            print(f"Error: No existe un tag con id_tag={id_tag}.")
            return False
        return self.crud.eliminar(id_tag)

    def buscar(self, id_tag):
        return self.crud.leer(id_tag)

    def actualizar(self, id_tag, **kwargs):
        valido, msg = validar_datos_tag(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_tag, **kwargs)

    def existe(self, id_tag):
        return self.crud.existe(id_tag)

    def listar(self):
        return self.crud.listar()
