from src.controlador.crud.crud_publicacion import CrudPublicacion
from src.controlador.validaciones.validar_publicacion import validar_datos_publicacion

class Publicaciones:
    def __init__(self):
        self.crud = CrudPublicacion()

    def agregar(self, **kwargs):
        id_publicacion = kwargs.get("id_publicacion")
        if id_publicacion is not None and self.crud.existe(id_publicacion):
            print(f"Error: Ya existe una publicación con id_publicacion={id_publicacion}.")
            return None
        valido, msg = validar_datos_publicacion(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_publicacion):
        if not self.crud.existe(id_publicacion):
            print(f"Error: No existe una publicación con id_publicacion={id_publicacion}.")
            return False
        return self.crud.eliminar(id_publicacion)

    def buscar(self, id_publicacion):
        return self.crud.leer(id_publicacion)

    def actualizar(self, id_publicacion, **kwargs):
        valido, msg = validar_datos_publicacion(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_publicacion, **kwargs)

    def existe(self, id_publicacion):
        return self.crud.existe(id_publicacion)

    def listar(self):
        return self.crud.listar()