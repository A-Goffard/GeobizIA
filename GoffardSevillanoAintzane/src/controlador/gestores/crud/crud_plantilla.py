from src.controlador.dominios.plantilla import Plantilla
from src.controlador.gestores.plantillas import Plantillas

def crear_plantilla(id_plantilla, titulo=None, tipo=None, contenido_base=None, fecha_creacion=None, ultima_modificacion=None):
    """
    Crea una nueva plantilla en la base de datos.

    Args:
        id_plantilla (int): ID de la plantilla.
        titulo (str, optional): Título de la plantilla.
        tipo (str, optional): Tipo de la plantilla.
        contenido_base (str, optional): Contenido base de la plantilla.
        fecha_creacion (str, optional): Fecha de creación de la plantilla.
        ultima_modificacion (str, optional): Fecha de última modificación de la plantilla.

    Returns:
        Plantilla: Objeto Plantilla creado, o None si falla.
    """
    gestor = Plantillas()
    return gestor.agregar(id_plantilla=id_plantilla, titulo=titulo, tipo=tipo, contenido_base=contenido_base, fecha_creacion=fecha_creacion, ultima_modificacion=ultima_modificacion)

def leer_plantilla(id_plantilla):
    """
    Lee una plantilla por su ID.

    Args:
        id_plantilla (int): ID de la plantilla.

    Returns:
        Plantilla: Objeto Plantilla si se encuentra, o None si no.
    """
    gestor = Plantillas()
    return gestor.buscar(id_plantilla)

def actualizar_plantilla(id_plantilla, titulo=None, tipo=None, contenido_base=None, fecha_creacion=None, ultima_modificacion=None):
    """
    Actualiza una plantilla existente.

    Args:
        id_plantilla (int): ID de la plantilla.
        titulo (str, optional): Nuevo título.
        tipo (str, optional): Nuevo tipo.
        contenido_base (str, optional): Nuevo contenido base.
        fecha_creacion (str, optional): Nueva fecha de creación.
        ultima_modificacion (str, optional): Nueva fecha de última modificación.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Plantillas()
    return gestor.actualizar(id_plantilla, titulo=titulo, tipo=tipo, contenido_base=contenido_base, fecha_creacion=fecha_creacion, ultima_modificacion=ultima_modificacion)

def eliminar_plantilla(id_plantilla):
    """
    Elimina una plantilla por su ID.

    Args:
        id_plantilla (int): ID de la plantilla.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Plantillas()
    return gestor.eliminar(id_plantilla)