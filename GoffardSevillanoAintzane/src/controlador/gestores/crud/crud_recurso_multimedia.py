from src.controlador.dominios.recurso_multimedia import RecursoMultimedia
from src.controlador.gestores.recursos_multimedia import RecursosMultimedia

def crear_recurso_multimedia(tipo, titulo, fecha_subida, autor):
    gestor = RecursosMultimedia()
    return gestor.agregar(tipo=tipo, titulo=titulo, fecha_subida=fecha_subida, autor=autor)

def leer_recurso_multimedia(id_recurso_multimedia):
    gestor = RecursosMultimedia()
    return gestor.buscar(id_recurso_multimedia)

def actualizar_recurso_multimedia(id_recurso_multimedia, **kwargs):
    gestor = RecursosMultimedia()
    return gestor.actualizar(id_recurso_multimedia, **kwargs)

def eliminar_recurso_multimedia(id_recurso_multimedia):
    gestor = RecursosMultimedia()
    return gestor.eliminar(id_recurso_multimedia)
