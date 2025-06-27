from src.controlador.dominios.tipo_publicacion import Tipo_Publicacion
from src.controlador.gestores.tipos_publicacion import Tipos_Publicacion

def crear_tipo_publicacion(id_tipo_publicacion, nombre=None, descripcion=None):
    """
    Crea un nuevo tipo_publicacion en la base de datos.

    Args:
        id_tipo_publicacion (int): ID del tipo de publicación.
        nombre (str, optional): Nombre del tipo de publicación.
        descripcion (str, optional): Descripción del tipo de publicación.

    Returns:
        Tipo_Publicacion: Objeto Tipo_Publicacion creado, o None si falla.
    """
    gestor = Tipos_Publicacion()
    return gestor.agregar(id_tipo_publicacion=id_tipo_publicacion, nombre=nombre, descripcion=descripcion)

def leer_tipo_publicacion(id_tipo_publicacion):
    """
    Lee un tipo_publicacion por su ID.

    Args:
        id_tipo_publicacion (int): ID del tipo de publicación.

    Returns:
        Tipo_Publicacion: Objeto Tipo_Publicacion si se encuentra, o None si no.
    """
    gestor = Tipos_Publicacion()
    return gestor.buscar(id_tipo_publicacion)

def actualizar_tipo_publicacion(id_tipo_publicacion, nombre=None, descripcion=None):
    """
    Actualiza un tipo_publicacion existente.

    Args:
        id_tipo_publicacion (int): ID del tipo de publicación.
        nombre (str, optional): Nuevo nombre.
        descripcion (str, optional): Nueva descripción.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Tipos_Publicacion()
    return gestor.actualizar(id_tipo_publicacion, nombre=nombre, descripcion=descripcion)

def eliminar_tipo_publicacion(id_tipo_publicacion):
    """
    Elimina un tipo_publicacion por su ID.

    Args:
        id_tipo_publicacion (int): ID del tipo de publicación.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Tipos_Publicacion()
    return gestor.eliminar(id_tipo_publicacion)