from .base_crud import BaseCRUD
from src.controlador.dominios.auditoria_publicacion import Auditoria_Publicacion

class CrudAuditoriaPublicacion(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="auditoria_publicacion",
            fields=[
                "id_auditoria_publicacion", "publicacion_id", "generador_ia_id",
                "fecha_generacion", "usuario_id", "parametros_entrada",
                "resultado", "observaciones"
            ],
            id_field="id_auditoria_publicacion"
        )

    def crear(self, **kwargs):
        return self.insert(kwargs, Auditoria_Publicacion)

    def leer(self, id_auditoria_publicacion):
        return self.select_by_id(id_auditoria_publicacion, Auditoria_Publicacion)

    def actualizar(self, id_auditoria_publicacion, **kwargs):
        return self.update(id_auditoria_publicacion, kwargs)

    def eliminar(self, id_auditoria_publicacion):
        return self.delete(id_auditoria_publicacion)

    def existe(self, id_auditoria_publicacion):
        return self.exists(id_auditoria_publicacion)

    def listar(self):
        return self.select_all(Auditoria_Publicacion)