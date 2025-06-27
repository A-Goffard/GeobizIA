from src.controlador.gestores.publicacion_tags import PublicacionTags


def agregar_publicacion_tag(publicacion_tags: PublicacionTags, id_publicacion, id_tag):
    return publicacion_tags.agregar(id_publicacion=id_publicacion, id_tag=id_tag)

def eliminar_publicacion_tag(publicacion_tags: PublicacionTags, id_publicacion, id_tag):
    return publicacion_tags.eliminar(id_publicacion, id_tag)

def buscar_publicacion_tag(publicacion_tags: PublicacionTags, id_publicacion, id_tag):
    return publicacion_tags.buscar(id_publicacion, id_tag)

def listar_todos_publicacion_tags(publicacion_tags: PublicacionTags):
    # En este caso, BaseGestor.mostrar_todos_los_elem funciona bien aunque id_field vacío
    return publicacion_tags.mostrar_todos_los_elem()
