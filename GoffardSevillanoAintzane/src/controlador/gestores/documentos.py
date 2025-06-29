from src.controlador.crud.crud_documento import CrudDocumento
from src.controlador.validaciones.validar_documento import validar_datos_documento

class Documentos:
    def __init__(self):
        self.crud = CrudDocumento()

    def agregar(self, **kwargs):
        id_documento = kwargs.get("id_documento")
        if id_documento is not None and self.crud.existe(id_documento):
            print(f"Error: Ya existe un documento con id_documento={id_documento}.")
            return None
        valido, msg = validar_datos_documento(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_documento):
        if not self.crud.existe(id_documento):
            print(f"Error: No existe un documento con id_documento={id_documento}.")
            return False
        return self.crud.eliminar(id_documento)

    def buscar(self, id_documento):
        return self.crud.leer(id_documento)

    def actualizar(self, id_documento, **kwargs):
        valido, msg = validar_datos_documento(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_documento, **kwargs)

    def existe(self, id_documento):
        return self.crud.existe(id_documento)

    def listar(self):
        return self.crud.listar()