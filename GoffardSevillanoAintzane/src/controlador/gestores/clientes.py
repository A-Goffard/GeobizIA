from src.controlador.crud.crud_cliente import CrudCliente
from src.controlador.validaciones.validar_cliente import validar_datos_cliente

class Clientes:
    def __init__(self):
        self.crud = CrudCliente()

    def agregar(self, **kwargs):
        id_cliente = kwargs.get("id_cliente")
        if id_cliente is not None and self.crud.existe(id_cliente):
            print(f"Error: Ya existe un cliente con id_cliente={id_cliente}.")
            return None
        valido, msg = validar_datos_cliente(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_cliente):
        if not self.crud.existe(id_cliente):
            print(f"Error: No existe un cliente con id_cliente={id_cliente}.")
            return False
        return self.crud.eliminar(id_cliente)

    def buscar(self, id_cliente):
        return self.crud.leer(id_cliente)

    def actualizar(self, id_cliente, **kwargs):
        valido, msg = validar_datos_cliente(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_cliente, **kwargs)

    def existe(self, id_cliente):
        return self.crud.existe(id_cliente)

    def listar(self):
        return self.crud.listar()