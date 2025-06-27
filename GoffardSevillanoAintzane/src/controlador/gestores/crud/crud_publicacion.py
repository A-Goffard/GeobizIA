from src.controlador.dominios.publicacion import Publicacion
from src.controlador.gestores.publicaciones import Publicaciones

def crear_publicacion(id_publicacion, id_generador_IA, id_tipo_publicacion, contenido=None, fecha_creacion=None):
    """
    Crea una nueva publicación en la base de datos.

    Args:
        id_publicacion (int): ID de la publicación.
        id_generador_IA (int): ID del generador_IA asociado.
        id_tipo_publicacion (int): ID del tipo de publicación asociado.
        contenido (str, optional): Contenido de la publicación.
        fecha_creacion (str, optional): Fecha de creación de la publicación.

    Returns:
        Publicacion: Objeto Publicacion creado, o None si falla.
    """
    gestor = Publicaciones()
    return gestor.agregar(id_publicacion=id_publicacion, id_generador_IA=id_generador_IA, id_tipo_publicacion=id_tipo_publicacion, contenido=contenido, fecha_creacion=fecha_creacion)

def leer_publicacion(id_publicacion):
    """
    Lee una publicación por su ID.

    Args:
        id_publicacion (int): ID de la publicación.

    Returns:
        Publicacion: Objeto Publicacion si se encuentra, o None si no.
    """
    gestor = Publicaciones()
    return gestor.buscar(id_publicacion)

def actualizar_publicacion(id_publicacion, id_generador_IA=None, id_tipo_publicacion=None, contenido=None, fecha_creacion=None):
    """
    Actualiza una publicación existente.

    Args:
        id_publicacion (int): ID de la publicación.
        id_generador_IA (int, optional): Nuevo ID del generador_IA asociado.
        id_tipo_publicacion (int, optional): Nuevo ID del tipo de publicación asociado.
        contenido (str, optional): Nuevo contenido.
        fecha_creacion (str, optional): Nueva fecha de creación.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Publicaciones()
    return gestor.actualizar(id_publicacion, id_generador_IA=id_generador_IA, id_tipo_publicacion=id_tipo_publicacion, contenido=contenido, fecha_creacion=fecha_creacion)

def eliminar_publicacion(id_publicacion):
    """
    Elimina una publicación por su ID.

    Args:
        id_publicacion (int): ID de la publicación.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Publicaciones()
    return gestor.eliminar(id_publicacion)