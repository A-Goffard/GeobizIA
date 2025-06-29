from src.controlador.crud.crud_tema_ambiental_tag import CrudTemaAmbientalTag
from src.controlador.validaciones.validar_tema_ambiental_tag import validar_datos_tema_ambiental_tag

class TemaAmbientalTagGestor:
    def __init__(self):
        self.crud = CrudTemaAmbientalTag()

    def agregar(self, id_tema_ambiental, id_tag):
        if self.crud.buscar(id_tema_ambiental, id_tag):
            print(f"Error: Ya existe la relación tema_ambiental_tag ({id_tema_ambiental}, {id_tag}).")
            return None
        datos = {"id_tema_ambiental": id_tema_ambiental, "id_tag": id_tag}
        valido, msg = validar_datos_tema_ambiental_tag(datos)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(id_tema_ambiental, id_tag)

    def eliminar(self, id_tema_ambiental, id_tag):
        if not self.crud.buscar(id_tema_ambiental, id_tag):
            print(f"Error: No existe la relación tema_ambiental_tag ({id_tema_ambiental}, {id_tag}).")
            return False
        return self.crud.eliminar(id_tema_ambiental, id_tag)

    def buscar(self, id_tema_ambiental, id_tag):
        return self.crud.buscar(id_tema_ambiental, id_tag)

    def listar(self):
        return self.crud.listar()
