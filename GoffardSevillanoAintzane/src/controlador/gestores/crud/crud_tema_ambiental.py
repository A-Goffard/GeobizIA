from src.controlador.dominios.tema_ambiental import Tema_Ambiental
from src.controlador.gestores.temas_ambientales import Temas_Ambientales

def crear_tema_ambiental(id_tema_ambiental, nombre=None, descripcion=None):
    """
    Crea un nuevo tema_ambiental en la base de datos.

    Args:
        id_tema_ambiental (int): ID del tema ambiental.
        nombre (str, optional): Nombre del tema ambiental.
        descripcion (str, optional): Descripción del tema ambiental.

    Returns:
        Tema_Ambiental: Objeto Tema_Ambiental creado, o None si falla.
    """
    gestor = Temas_Ambientales()
    return gestor.agregar(id_tema_ambiental=id_tema_ambiental, nombre=nombre, descripcion=descripcion)

def leer_tema_ambiental(id_tema_ambiental):
    """
    Lee un tema_ambiental por su ID.

    Args:
        id_tema_ambiental (int): ID del tema ambiental.

    Returns:
        Tema_Ambiental: Objeto Tema_Ambiental si se encuentra, o None si no.
    """
    gestor = Temas_Ambientales()
    return gestor.buscar(id_tema_ambiental)

def actualizar_tema_ambiental(id_tema_ambiental, nombre=None, descripcion=None):
    """
    Actualiza un tema_ambiental existente.

    Args:
        id_tema_ambiental (int): ID del tema ambiental.
        nombre (str, optional): Nuevo nombre.
        descripcion (str, optional): Nueva descripción.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Temas_Ambientales()
    return gestor.actualizar(id_tema_ambiental, nombre=nombre, descripcion=descripcion)

def eliminar_tema_ambiental(id_tema_ambiental):
    """
    Elimina un tema_ambiental por su ID.

    Args:
        id_tema_ambiental (int): ID del tema ambiental.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Temas_Ambientales()
    return gestor.eliminar(id_tema_ambiental)