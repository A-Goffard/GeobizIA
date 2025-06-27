from src.controlador.dominios.fecha_actividad import FechaActividad
from src.controlador.gestores.fechas_actividad import FechasActividad

def crear_fecha_actividad(fecha):
    """
    Crea una nueva fecha_actividad en la base de datos.

    Args:
        fecha (str): Fecha en formato 'YYYY-MM-DD'.

    Returns:
        FechaActividad: Objeto FechaActividad creado, o None si falla.
    """
    gestor = FechasActividad()
    return gestor.agregar(fecha=fecha)

def leer_fecha_actividad(id_fecha):
    """
    Lee una fecha_actividad por su ID.

    Args:
        id_fecha (int): ID de la fecha_actividad.

    Returns:
        FechaActividad: Objeto FechaActividad si se encuentra, o None si no.
    """
    gestor = FechasActividad()
    return gestor.buscar(id_fecha)

def actualizar_fecha_actividad(id_fecha, fecha=None):
    """
    Actualiza una fecha_actividad existente.

    Args:
        id_fecha (int): ID de la fecha_actividad.
        fecha (str, optional): Nueva fecha.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = FechasActividad()
    return gestor.actualizar(id_fecha, fecha=fecha)

def eliminar_fecha_actividad(id_fecha):
    """
    Elimina una fecha_actividad por su ID.

    Args:
        id_fecha (int): ID de la fecha_actividad.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = FechasActividad()
    return gestor.eliminar(id_fecha)