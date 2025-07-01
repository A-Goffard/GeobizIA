from src.controlador.crud.crud_publicacion_tag import CrudPublicacionTag
from src.controlador.validaciones.validar_publicacion_tag import validar_datos_publicacion_tag

class PublicacionTags:
    def __init__(self):
        self.crud = CrudPublicacionTag()

    def agregar(self, **kwargs):
        id_publicacion = kwargs.get("id_publicacion")
        id_tag = kwargs.get("id_tag")
        # Comprobación de existencia por clave compuesta
        if id_publicacion is not None and id_tag is not None and self.crud.buscar(id_publicacion, id_tag):
            print(f"Error: Ya existe la relación publicacion_tag ({id_publicacion}, {id_tag}).")
            return None
        valido, msg = validar_datos_publicacion_tag(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(id_publicacion, id_tag)

    def eliminar(self, id_publicacion, id_tag):
        if not self.crud.buscar(id_publicacion, id_tag):
            print(f"Error: No existe la relación publicacion_tag ({id_publicacion}, {id_tag}).")
            return False
        return self.crud.eliminar(id_publicacion, id_tag)

    def buscar(self, id_publicacion, id_tag):
        return self.crud.buscar(id_publicacion, id_tag)

    def actualizar(self, id_publicacion, id_tag, **kwargs):
        # No suele haber actualización en tablas intermedias, pero si la hay, implementa aquí
        pass

    def listar(self):
        return self.crud.listar()

    def mostrar_todos_los_elem(self):
        return self.listar()