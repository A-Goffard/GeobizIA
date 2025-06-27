from src.controlador.dominios.log_sistema import Log_Sistema
from src.controlador.gestores.logs_sistema import Logs_Sistema

def crear_log_sistema(id_log_sistema, usuario_id, fecha=None, accion=None, descripcion=None, nivel=None):
    """
    Crea un nuevo log_sistema en la base de datos.

    Args:
        id_log_sistema (int): ID del log del sistema.
        usuario_id (int): ID del usuario asociado.
        fecha (str, optional): Fecha del log.
        accion (str, optional): Acción realizada.
        descripcion (str, optional): Descripción del log.
        nivel (str, optional): Nivel del log (ej. 'INFO', 'ERROR').

    Returns:
        Log_Sistema: Objeto Log_Sistema creado, o None si falla.
    """
    gestor = Logs_Sistema()
    return gestor.agregar(id_log_sistema=id_log_sistema, usuario_id=usuario_id, fecha=fecha, accion=accion, descripcion=descripcion, nivel=nivel)

def leer_log_sistema(id_log_sistema):
    """
    Lee un log_sistema por su ID.

    Args:
        id_log_sistema (int): ID del log del sistema.

    Returns:
        Log_Sistema: Objeto Log_Sistema si se encuentra, o None si no.
    """
    gestor = Logs_Sistema()
    return gestor.buscar(id_log_sistema)

def actualizar_log_sistema(id_log_sistema, usuario_id=None, fecha=None, accion=None, descripcion=None, nivel=None):
    """
    Actualiza un log_sistema existente.

    Args:
        id_log_sistema (int): ID del log del sistema.
        usuario_id (int, optional): Nuevo ID del usuario asociado.
        fecha (str, optional): Nueva fecha.
        accion (str, optional): Nueva acción.
        descripcion (str, optional): Nueva descripción.
        nivel (str, optional): Nuevo nivel.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Logs_Sistema()
    return gestor.actualizar(id_log_sistema, usuario_id=usuario_id, fecha=fecha, accion=accion, descripcion=descripcion, nivel=nivel)

def eliminar_log_sistema(id_log_sistema):
    """
    Elimina un log_sistema por su ID.

    Args:
        id_log_sistema (int): ID del log del sistema.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Logs_Sistema()
    return gestor.eliminar(id_log_sistema)