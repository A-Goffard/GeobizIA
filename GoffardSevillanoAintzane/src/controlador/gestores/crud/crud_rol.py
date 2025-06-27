from src.controlador.dominios.rol import Rol
from src.controlador.gestores.roles import Roles

def crear_rol(nombre):
    """
    Crea un nuevo rol en la base de datos.

    Args:
        nombre (str): Nombre del rol.

    Returns:
        Rol: Objeto Rol creado, o None si falla.
    """
    gestor = Roles()
    return gestor.agregar(nombre=nombre)

def leer_rol(id_rol):
    """
    Lee un rol por su ID.

    Args:
        id_rol (int): ID del rol.

    Returns:
        Rol: Objeto Rol si se encuentra, o None si no.
    """
    gestor = Roles()
    return gestor.buscar(id_rol)

def actualizar_rol(id_rol, nombre=None):
    """
    Actualiza un rol existente.

    Args:
        id_rol (int): ID del rol.
        nombre (str, optional): Nuevo nombre del rol.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Roles()
    return gestor.actualizar(id_rol, nombre=nombre)

def eliminar_rol(id_rol):
    """
    Elimina un rol por su ID.

    Args:
        id_rol (int): ID del rol.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Roles()
    return gestor.eliminar(id_rol)