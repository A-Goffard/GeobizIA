from src.controlador.dominios.fecha_actividad import Fecha_Actividad
from src.controlador.gestores.fechas_actividad import Fechas_Actividad

def crear_fecha_actividad(fecha=None):
    """
    Crea una nueva fecha_actividad en la base de datos.

    Args:
        fecha (str, optional): Fecha de la actividad.

    Returns:
        Fecha_Actividad: Objeto Fecha_Actividad creado, o None si falla.
    """
    gestor = Fechas_Actividad()
    return gestor.agregar(fecha=fecha)

def leer_fecha_actividad(id_fecha):
    """
    Lee una fecha_actividad por su ID.

    Args:
        id_fecha (int): ID de la fecha.

    Returns:
        Fecha_Actividad: Objeto Fecha_Actividad si se encuentra, o None si no.
    """
    gestor = Fechas_Actividad()
    return gestor.buscar(id_fecha)

def actualizar_fecha_actividad(id_fecha, fecha=None):
    """
    Actualiza una fecha_actividad existente.

    Args:
        id_fecha (int): ID de la fecha.
        fecha (str, optional): Nueva fecha.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Fechas_Actividad()
    return gestor.actualizar(id_fecha, fecha=fecha)

def eliminar_fecha_actividad(id_fecha):
    """
    Elimina una fecha_actividad por su ID.

    Args:
        id_fecha (int): ID de la fecha.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Fechas_Actividad()
    return gestor.eliminar(id_fecha)