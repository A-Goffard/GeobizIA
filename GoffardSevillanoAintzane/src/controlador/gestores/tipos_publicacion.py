from src.controlador.crud.crud_tipo_publicacion import CrudTipoPublicacion
from src.controlador.validaciones.validar_tipo_publicacion import validar_datos_tipo_publicacion

class Tipos_Publicacion:
    def __init__(self):
        self.crud = CrudTipoPublicacion()

    def agregar(self, **kwargs):
        id_tipo_publicacion = kwargs.get("id_tipo_publicacion")
        if id_tipo_publicacion is not None and self.crud.existe(id_tipo_publicacion):
            print(f"Error: Ya existe un tipo_publicacion con id_tipo_publicacion={id_tipo_publicacion}.")
            return None
        valido, msg = validar_datos_tipo_publicacion(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_tipo_publicacion):
        if not self.crud.existe(id_tipo_publicacion):
            print(f"Error: No existe un tipo_publicacion con id_tipo_publicacion={id_tipo_publicacion}.")
            return False
        return self.crud.eliminar(id_tipo_publicacion)

    def buscar(self, id_tipo_publicacion):
        return self.crud.leer(id_tipo_publicacion)

    def actualizar(self, id_tipo_publicacion, **kwargs):
        valido, msg = validar_datos_tipo_publicacion(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_tipo_publicacion, **kwargs)

    def existe(self, id_tipo_publicacion):
        return self.crud.existe(id_tipo_publicacion)

    def listar(self):
        return self.crud.listar()