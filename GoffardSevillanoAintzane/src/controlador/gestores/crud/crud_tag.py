from src.controlador.dominios.tag import Tag
from src.controlador.gestores.tags import Tags

def crear_tag(palabra_clave, categoria, frecuencia_uso=0):
    gestor = Tags()
    return gestor.agregar(palabra_clave=palabra_clave, categoria=categoria, frecuencia_uso=frecuencia_uso)

def leer_tag(id_tag):
    gestor = Tags()
    return gestor.buscar(id_tag)

def actualizar_tag(id_tag, palabra_clave=None, categoria=None, frecuencia_uso=None):
    gestor = Tags()
    return gestor.actualizar(id_tag, palabra_clave=palabra_clave, categoria=categoria, frecuencia_uso=frecuencia_uso)

def eliminar_tag(id_tag):
    gestor = Tags()
    return gestor.eliminar(id_tag)
