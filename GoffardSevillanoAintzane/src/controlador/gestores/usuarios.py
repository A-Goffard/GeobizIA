from src.controlador.crud.crud_usuario import CrudUsuario
from src.controlador.validaciones.validar_usuario import validar_datos_usuario

class Usuarios:
    def __init__(self):
        self.crud = CrudUsuario()

    def agregar(self, **kwargs):
        # Validación de existencia previa
        id_usuario = kwargs.get("id_usuario")
        if id_usuario is not None and self.crud.existe(id_usuario):
            print(f"Error: Ya existe un usuario con id_usuario={id_usuario}.")
            return None
        valido, msg = validar_datos_usuario(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_usuario):
        if not self.crud.existe(id_usuario):
            print(f"Error: No existe un usuario con id_usuario={id_usuario}.")
            return False
        return self.crud.eliminar(id_usuario)

    def buscar(self, id_usuario):
        return self.crud.leer(id_usuario)

    def actualizar(self, id_usuario, **kwargs):
        valido, msg = validar_datos_usuario(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_usuario, **kwargs)

    def existe(self, id_usuario):
        return self.crud.existe(id_usuario)

    def listar(self):
        return self.crud.listar()