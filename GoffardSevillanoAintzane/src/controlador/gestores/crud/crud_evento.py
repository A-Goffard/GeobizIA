from src.controlador.dominios.evento import Evento
from src.controlador.gestores.eventos import Eventos

def crear_evento(id_evento, nombre=None, tipo=None, lugar=None, fecha_comienzo=None, fecha_final=None, poblacion=None, tematica=None):
    """
    Crea un nuevo evento en la base de datos.

    Args:
        id_evento (int): ID del evento.
        nombre (str, optional): Nombre del evento.
        tipo (str, optional): Tipo del evento.
        lugar (str, optional): Lugar del evento.
        fecha_comienzo (str, optional): Fecha de comienzo del evento.
        fecha_final (str, optional): Fecha de finalización del evento.
        poblacion (str, optional): Población del evento.
        tematica (str, optional): Temática del evento.

    Returns:
        Evento: Objeto Evento creado, o None si falla.
    """
    gestor = Eventos()
    return gestor.agregar(id_evento=id_evento, nombre=nombre, tipo=tipo, lugar=lugar, fecha_comienzo=fecha_comienzo, fecha_final=fecha_final, poblacion=poblacion, tematica=tematica)

def leer_evento(id_evento):
    """
    Lee un evento por su ID.

    Args:
        id_evento (int): ID del evento.

    Returns:
        Evento: Objeto Evento si se encuentra, o None si no.
    """
    gestor = Eventos()
    return gestor.buscar(id_evento)

def actualizar_evento(id_evento, nombre=None, tipo=None, lugar=None, fecha_comienzo=None, fecha_final=None, poblacion=None, tematica=None):
    """
    Actualiza un evento existente.

    Args:
        id_evento (int): ID del evento.
        nombre (str, optional): Nuevo nombre.
        tipo (str, optional): Nuevo tipo.
        lugar (str, optional): Nuevo lugar.
        fecha_comienzo (str, optional): Nueva fecha de comienzo.
        fecha_final (str, optional): Nueva fecha de finalización.
        poblacion (str, optional): Nueva población.
        tematica (str, optional): Nueva temática.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Eventos()
    return gestor.actualizar(id_evento, nombre=nombre, tipo=tipo, lugar=lugar, fecha_comienzo=fecha_comienzo, fecha_final=fecha_final, poblacion=poblacion, tematica=tematica)

def eliminar_evento(id_evento):
    """
    Elimina un evento por su ID.

    Args:
        id_evento (int): ID del evento.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Eventos()
    return gestor.eliminar(id_evento)