from src.controlador.dominios.actividad import Actividad
from src.controlador.gestores.actividades import Actividades

def crear_actividad(id_actividad, tipo=None, nombre=None, descripcion=None, responsable=None, duracion=None, coste_economico=None, coste_horas=None, facturacion=None, resultados=None, valoracion=None, observaciones=None):
    """
    Crea una nueva actividad en la base de datos.

    Args:
        id_actividad (int): ID de la actividad.
        tipo (str, optional): Tipo de actividad.
        nombre (str, optional): Nombre de la actividad.
        descripcion (str, optional): Descripción de la actividad.
        responsable (str, optional): Responsable de la actividad.
        duracion (str, optional): Duración de la actividad.
        coste_economico (float, optional): Coste económico de la actividad.
        coste_horas (float, optional): Coste en horas de la actividad.
        facturacion (float, optional): Facturación de la actividad.
        resultados (str, optional): Resultados de la actividad.
        valoracion (str, optional): Valoración de la actividad.
        observaciones (str, optional): Observaciones de la actividad.

    Returns:
        Actividad: Objeto Actividad creado, o None si falla.
    """
    gestor = Actividades()
    return gestor.agregar(id_actividad=id_actividad, tipo=tipo, nombre=nombre, descripcion=descripcion, responsable=responsable, duracion=duracion, coste_economico=coste_economico, coste_horas=coste_horas, facturacion=facturacion, resultados=resultados, valoracion=valoracion, observaciones=observaciones)

def leer_actividad(id_actividad):
    """
    Lee una actividad por su ID.

    Args:
        id_actividad (int): ID de la actividad.

    Returns:
        Actividad: Objeto Actividad si se encuentra, o None si no.
    """
    gestor = Actividades()
    return gestor.buscar(id_actividad)

def actualizar_actividad(id_actividad, tipo=None, nombre=None, descripcion=None, responsable=None, duracion=None, coste_economico=None, coste_horas=None, facturacion=None, resultados=None, valoracion=None, observaciones=None):
    """
    Actualiza una actividad existente.

    Args:
        id_actividad (int): ID de la actividad.
        tipo (str, optional): Nuevo tipo.
        nombre (str, optional): Nuevo nombre.
        descripcion (str, optional): Nueva descripción.
        responsable (str, optional): Nuevo responsable.
        duracion (str, optional): Nueva duración.
        coste_economico (float, optional): Nuevo coste económico.
        coste_horas (float, optional): Nuevo coste en horas.
        facturacion (float, optional): Nueva facturación.
        resultados (str, optional): Nuevos resultados.
        valoracion (str, optional): Nueva valoración.
        observaciones (str, optional): Nuevas observaciones.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Actividades()
    return gestor.actualizar(id_actividad, tipo=tipo, nombre=nombre, descripcion=descripcion, responsable=responsable, duracion=duracion, coste_economico=coste_economico, coste_horas=coste_horas, facturacion=facturacion, resultados=resultados, valoracion=valoracion, observaciones=observaciones)

def eliminar_actividad(id_actividad):
    """
    Elimina una actividad por su ID.

    Args:
        id_actividad (int): ID de la actividad.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Actividades()
    return gestor.eliminar(id_actividad)