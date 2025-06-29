from src.controlador.crud.crud_tipo_publicacion_redsocial import CrudTipoPublicacionRedSocial
from src.controlador.validaciones.validar_tipo_publicacion_redsocial import validar_datos_tipo_publicacion_redsocial

class TipoPublicacionRedSocialGestor:
    def __init__(self):
        self.crud = CrudTipoPublicacionRedSocial()

    def agregar(self, id_tipo_publicacion, id_red_social):
        if self.crud.buscar(id_tipo_publicacion, id_red_social):
            print(f"Error: Ya existe la relación tipo_publicacion_redsocial ({id_tipo_publicacion}, {id_red_social}).")
            return None
        datos = {"id_tipo_publicacion": id_tipo_publicacion, "id_red_social": id_red_social}
        valido, msg = validar_datos_tipo_publicacion_redsocial(datos)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(id_tipo_publicacion, id_red_social)

    def eliminar(self, id_tipo_publicacion, id_red_social):
        if not self.crud.buscar(id_tipo_publicacion, id_red_social):
            print(f"Error: No existe la relación tipo_publicacion_redsocial ({id_tipo_publicacion}, {id_red_social}).")
            return False
        return self.crud.eliminar(id_tipo_publicacion, id_red_social)

    def buscar(self, id_tipo_publicacion, id_red_social):
        return self.crud.buscar(id_tipo_publicacion, id_red_social)

    def listar(self):
        return self.crud.listar()
