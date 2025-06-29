from src.controlador.crud.crud_redsocial import CrudRedSocial
from src.controlador.validaciones.validar_redsocial import validar_datos_redsocial

class RedesSociales:
    def __init__(self):
        self.crud = CrudRedSocial()

    def agregar(self, **kwargs):
        id_red_social = kwargs.get("id_red_social")
        if id_red_social is not None and self.crud.existe(id_red_social):
            print(f"Error: Ya existe una red social con id_red_social={id_red_social}.")
            return None
        valido, msg = validar_datos_redsocial(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_red_social):
        if not self.crud.existe(id_red_social):
            print(f"Error: No existe una red social con id_red_social={id_red_social}.")
            return False
        return self.crud.eliminar(id_red_social)

    def buscar(self, id_red_social):
        return self.crud.leer(id_red_social)

    def actualizar(self, id_red_social, **kwargs):
        valido, msg = validar_datos_redsocial(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_red_social, **kwargs)

    def existe(self, id_red_social):
        return self.crud.existe(id_red_social)

    def listar(self):
        return self.crud.listar()
