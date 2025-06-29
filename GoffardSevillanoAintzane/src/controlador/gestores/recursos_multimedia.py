from src.controlador.crud.crud_recurso_multimedia import CrudRecursoMultimedia
from src.controlador.validaciones.validar_recurso_multimedia import validar_datos_recurso_multimedia

class RecursosMultimedia:
    def __init__(self):
        self.crud = CrudRecursoMultimedia()

    def agregar(self, **kwargs):
        id_recurso_multimedia = kwargs.get("id_recurso_multimedia")
        if id_recurso_multimedia is not None and self.crud.existe(id_recurso_multimedia):
            print(f"Error: Ya existe un recurso_multimedia con id_recurso_multimedia={id_recurso_multimedia}.")
            return None
        valido, msg = validar_datos_recurso_multimedia(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_recurso_multimedia):
        if not self.crud.existe(id_recurso_multimedia):
            print(f"Error: No existe un recurso_multimedia con id_recurso_multimedia={id_recurso_multimedia}.")
            return False
        return self.crud.eliminar(id_recurso_multimedia)

    def buscar(self, id_recurso_multimedia):
        return self.crud.leer(id_recurso_multimedia)

    def actualizar(self, id_recurso_multimedia, **kwargs):
        valido, msg = validar_datos_recurso_multimedia(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_recurso_multimedia, **kwargs)

    def existe(self, id_recurso_multimedia):
        return self.crud.existe(id_recurso_multimedia)

    def listar(self):
        return self.crud.listar()
