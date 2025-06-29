from src.controlador.crud.crud_documento_tag import CrudDocumentoTag
from src.controlador.validaciones.validar_documento_tag import validar_datos_documento_tag

class DocumentosTagGestor:
    def __init__(self):
        self.crud = CrudDocumentoTag()

    def agregar(self, id_documento, id_tag):
        if self.crud.buscar(id_documento, id_tag):
            print(f"Error: Ya existe la relación documento_tag ({id_documento}, {id_tag}).")
            return None
        datos = {"id_documento": id_documento, "id_tag": id_tag}
        valido, msg = validar_datos_documento_tag(datos)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(id_documento, id_tag)

    def eliminar(self, id_documento, id_tag):
        if not self.crud.buscar(id_documento, id_tag):
            print(f"Error: No existe la relación documento_tag ({id_documento}, {id_tag}).")
            return False
        return self.crud.eliminar(id_documento, id_tag)

    def buscar(self, id_documento, id_tag):
        return self.crud.buscar(id_documento, id_tag)

    def listar(self):
        return self.crud.listar()
