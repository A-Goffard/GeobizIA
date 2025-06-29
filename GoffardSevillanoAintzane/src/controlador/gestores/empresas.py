from src.controlador.crud.crud_empresa import CrudEmpresa
from src.controlador.validaciones.validar_empresa import validar_datos_empresa

class Empresas:
    def __init__(self):
        self.crud = CrudEmpresa()

    def agregar(self, **kwargs):
        id_empresa = kwargs.get("id_empresa")
        if id_empresa is not None and self.crud.existe(id_empresa):
            print(f"Error: Ya existe una empresa con id_empresa={id_empresa}.")
            return None
        valido, msg = validar_datos_empresa(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_empresa):
        if not self.crud.existe(id_empresa):
            print(f"Error: No existe una empresa con id_empresa={id_empresa}.")
            return False
        return self.crud.eliminar(id_empresa)

    def buscar(self, id_empresa):
        return self.crud.leer(id_empresa)

    def actualizar(self, id_empresa, **kwargs):
        valido, msg = validar_datos_empresa(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_empresa, **kwargs)

    def existe(self, id_empresa):
        return self.crud.existe(id_empresa)

    def listar(self):
        return self.crud.listar()