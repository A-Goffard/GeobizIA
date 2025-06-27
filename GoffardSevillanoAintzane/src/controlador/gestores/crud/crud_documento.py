from src.controlador.dominios.documento import Documento
from src.controlador.gestores.documentos import Documentos

def crear_documento(id_documento, titulo=None, descripcion=None, fecha_subida=None, tipo=None, tematica=None):
    """
    Crea un nuevo documento en la base de datos.

    Args:
        id_documento (int): ID del documento.
        titulo (str, optional): Título del documento.
        descripcion (str, optional): Descripción del documento.
        fecha_subida (str, optional): Fecha de subida del documento.
        tipo (str, optional): Tipo del documento.
        tematica (str, optional): Temática del documento.

    Returns:
        Documento: Objeto Documento creado, o None si falla.
    """
    gestor = Documentos()
    return gestor.agregar(id_documento=id_documento, titulo=titulo, descripcion=descripcion, fecha_subida=fecha_subida, tipo=tipo, tematica=tematica)

def leer_documento(id_documento):
    """
    Lee un documento por su ID.

    Args:
        id_documento (int): ID del documento.

    Returns:
        Documento: Objeto Documento si se encuentra, o None si no.
    """
    gestor = Documentos()
    return gestor.buscar(id_documento)

def actualizar_documento(id_documento, titulo=None, descripcion=None, fecha_subida=None, tipo=None, tematica=None):
    """
    Actualiza un documento existente.

    Args:
        id_documento (int): ID del documento.
        titulo (str, optional): Nuevo título.
        descripcion (str, optional): Nueva descripción.
        fecha_subida (str, optional): Nueva fecha de subida.
        tipo (str, optional): Nuevo tipo.
        tematica (str, optional): Nueva temática.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Documentos()
    return gestor.actualizar(id_documento, titulo=titulo, descripcion=descripcion, fecha_subida=fecha_subida, tipo=tipo, tematica=tematica)

def eliminar_documento(id_documento):
    """
    Elimina un documento por su ID.

    Args:
        id_documento (int): ID del documento.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Documentos()
    return gestor.eliminar(id_documento)