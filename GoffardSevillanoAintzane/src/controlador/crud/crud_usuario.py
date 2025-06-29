from .base_crud import BaseCRUD
from src.controlador.dominios.usuario import Usuario

class CrudUsuario(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="usuario",
            fields=["id_usuario", "id_persona", "fecha_nacimiento", "rol", "preferencias", "password"],
            id_field="id_usuario"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Usuario)

    def leer(self, id_usuario):
        return self.select_by_id(id_usuario, Usuario)

    def actualizar(self, id_usuario, **kwargs):
        return self.update(id_usuario, kwargs)

    def eliminar(self, id_usuario):
        return self.delete(id_usuario)

    def existe(self, id_usuario):
        return self.exists(id_usuario)

    def listar(self):
        return self.select_all(Usuario)