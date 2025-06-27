from src.controlador.gestores.temas_ambientales_tag import TemasAmbientalesTag

def crear_relacion_tema_tag(id_tema_ambiental: int, id_tag: int):
    gestor = TemasAmbientalesTag()
    return gestor.agregar(id_tema_ambiental=id_tema_ambiental, id_tag=id_tag)

def eliminar_relacion_tema_tag(id_tema_ambiental: int, id_tag: int):
    gestor = TemasAmbientalesTag()
    return gestor.eliminar(id_tema_ambiental, id_tag)

def buscar_relacion_tema_tag(id_tema_ambiental: int, id_tag: int):
    gestor = TemasAmbientalesTag()
    return gestor.buscar((id_tema_ambiental, id_tag))

def listar_relaciones_por_tema(id_tema_ambiental: int):
    gestor = TemasAmbientalesTag()
    return gestor.listar(filtro={"id_tema_ambiental": id_tema_ambiental})

def listar_relaciones_por_tag(id_tag: int):
    gestor = TemasAmbientalesTag()
    return gestor.listar(filtro={"id_tag": id_tag})
