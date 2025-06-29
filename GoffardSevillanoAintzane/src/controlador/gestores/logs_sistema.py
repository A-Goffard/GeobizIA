from src.controlador.crud.crud_log_sistema import CrudLogSistema
from src.controlador.validaciones.validar_log_sistema import validar_datos_log_sistema

class LogsSistema:
    def __init__(self):
        self.crud = CrudLogSistema()

    def agregar(self, **kwargs):
        id_log_sistema = kwargs.get("id_log_sistema")
        if id_log_sistema is not None and self.crud.existe(id_log_sistema):
            print(f"Error: Ya existe un log_sistema con id_log_sistema={id_log_sistema}.")
            return None
        valido, msg = validar_datos_log_sistema(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_log_sistema):
        if not self.crud.existe(id_log_sistema):
            print(f"Error: No existe un log_sistema con id_log_sistema={id_log_sistema}.")
            return False
        return self.crud.eliminar(id_log_sistema)

    def buscar(self, id_log_sistema):
        return self.crud.leer(id_log_sistema)

    def actualizar(self, id_log_sistema, **kwargs):
        valido, msg = validar_datos_log_sistema(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_log_sistema, **kwargs)

    def existe(self, id_log_sistema):
        return self.crud.existe(id_log_sistema)

    def listar(self):
        return self.crud.listar()