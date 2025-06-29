from src.controlador.crud.crud_auditoria_publicacion import CrudAuditoriaPublicacion
from src.controlador.validaciones.validar_auditoria_publicacion import validar_datos_auditoria_publicacion

class Auditorias_Publicacion:
    def __init__(self):
        self.crud = CrudAuditoriaPublicacion()

    def agregar(self, **kwargs):
        id_auditoria_publicacion = kwargs.get("id_auditoria_publicacion")
        if id_auditoria_publicacion is not None and self.crud.existe(id_auditoria_publicacion):
            print(f"Error: Ya existe una auditoría con id_auditoria_publicacion={id_auditoria_publicacion}.")
            return None
        valido, msg = validar_datos_auditoria_publicacion(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_auditoria_publicacion):
        if not self.crud.existe(id_auditoria_publicacion):
            print(f"Error: No existe una auditoría con id_auditoria_publicacion={id_auditoria_publicacion}.")
            return False
        return self.crud.eliminar(id_auditoria_publicacion)

    def buscar(self, id_auditoria_publicacion):
        return self.crud.leer(id_auditoria_publicacion)

    def actualizar(self, id_auditoria_publicacion, **kwargs):
        valido, msg = validar_datos_auditoria_publicacion(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_auditoria_publicacion, **kwargs)

    def existe(self, id_auditoria_publicacion):
        return self.crud.existe(id_auditoria_publicacion)

    def listar(self):
        return self.crud.listar()