from src.controlador.gestores.documentos_tag import DocumentosTag

def crear_relacion_documento_tag(id_documento: int, id_tag: int):
    gestor = DocumentosTag()
    return gestor.agregar(id_documento=id_documento, id_tag=id_tag)

def eliminar_relacion_documento_tag(id_documento: int, id_tag: int):
    gestor = DocumentosTag()
    return gestor.eliminar(id_documento, id_tag)

def buscar_relacion_documento_tag(id_documento: int, id_tag: int):
    gestor = DocumentosTag()
    return gestor.buscar((id_documento, id_tag))

def listar_relaciones_por_documento(id_documento: int):
    gestor = DocumentosTag()
    return gestor.listar(filtro={"id_documento": id_documento})

def listar_relaciones_por_tag(id_tag: int):
    gestor = DocumentosTag()
    return gestor.listar(filtro={"id_tag": id_tag})
