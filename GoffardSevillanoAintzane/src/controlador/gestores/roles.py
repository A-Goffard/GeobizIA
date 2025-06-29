from src.controlador.crud.crud_rol import CrudRol
from src.controlador.validaciones.validar_rol import validar_datos_rol

class Roles:
    def __init__(self):
        self.crud = CrudRol()

    def agregar(self, **kwargs):
        id_rol = kwargs.get("id_rol")
        if id_rol is not None and self.crud.existe(id_rol):
            print(f"Error: Ya existe un rol con id_rol={id_rol}.")
            return None
        valido, msg = validar_datos_rol(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_rol):
        if not self.crud.existe(id_rol):
            print(f"Error: No existe un rol con id_rol={id_rol}.")
            return False
        return self.crud.eliminar(id_rol)

    def buscar(self, id_rol):
        return self.crud.leer(id_rol)

    def actualizar(self, id_rol, **kwargs):
        valido, msg = validar_datos_rol(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_rol, **kwargs)

    def existe(self, id_rol):
        return self.crud.existe(id_rol)

    def listar(self):
        return self.crud.listar()