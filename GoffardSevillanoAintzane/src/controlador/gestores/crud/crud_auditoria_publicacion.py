from src.controlador.dominios.auditoria_publicacion import Auditoria_Publicacion
from src.controlador.gestores.auditorias_publicacion import Auditorias_Publicacion

def crear_auditoria_publicacion(id_auditoria, id_publicacion, usuario_id, fecha=None, accion=None, descripcion=None, nivel=None):
    """
    Crea un nuevo registro de auditoria_publicacion en la base de datos.

    Args:
        id_auditoria (int): ID de la auditoría.
        id_publicacion (int): ID de la publicación asociada.
        usuario_id (int): ID del usuario asociado.
        fecha (str, optional): Fecha de la auditoría.
        accion (str, optional): Acción realizada.
        descripcion (str, optional): Descripción de la auditoría.
        nivel (str, optional): Nivel de la auditoría (ej. 'INFO', 'ERROR').

    Returns:
        Auditoria_Publicacion: Objeto Auditoria_Publicacion creado, o None si falla.
    """
    gestor = Auditorias_Publicacion()
    return gestor.agregar(id_auditoria=id_auditoria, id_publicacion=id_publicacion, usuario_id=usuario_id, fecha=fecha, accion=accion, descripcion=descripcion, nivel=nivel)

def leer_auditoria_publicacion(id_auditoria):
    """
    Lee un registro de auditoria_publicacion por su ID.

    Args:
        id_auditoria (int): ID de la auditoría.

    Returns:
        Auditoria_Publicacion: Objeto Auditoria_Publicacion si se encuentra, o None si no.
    """
    gestor = Auditorias_Publicacion()
    return gestor.buscar(id_auditoria)

def actualizar_auditoria_publicacion(id_auditoria, id_publicacion=None, usuario_id=None, fecha=None, accion=None, descripcion=None, nivel=None):
    """
    Actualiza un registro de auditoria_publicacion existente.

    Args:
        id_auditoria (int): ID de la auditoría.
        id_publicacion (int, optional): Nuevo ID de la publicación asociada.
        usuario_id (int, optional): Nuevo ID del usuario asociado.
        fecha (str, optional): Nueva fecha.
        accion (str, optional): Nueva acción.
        descripcion (str, optional): Nueva descripción.
        nivel (str, optional): Nuevo nivel.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Auditorias_Publicacion()
    return gestor.actualizar(id_auditoria, id_publicacion=id_publicacion, usuario_id=usuario_id, fecha=fecha, accion=accion, descripcion=descripcion, nivel=nivel)

def eliminar_auditoria_publicacion(id_auditoria):
    """
    Elimina un registro de auditoria_publicacion por su ID.

    Args:
        id_auditoria (int): ID de la auditoría.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Auditorias_Publicacion()
    return gestor.eliminar(id_auditoria)