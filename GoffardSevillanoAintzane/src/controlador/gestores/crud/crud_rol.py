from dominios.rol import Rol
from gestores.roles import Roles

def crear_rol(id_rol, nombre, descripcion):
    """
    Crea un nuevo rol en la base de datos.

    Args:
        id_rol (int): ID del rol.
        nombre (str): Nombre del rol.
        descripcion (str): Descripción del rol.

    Returns:
        Rol: Objeto Rol creado, o None si falla.
    """
    gestor = Roles()
    return gestor.agregar(id_rol=id_rol, nombre=nombre, descripcion=descripcion)

def leer_rol(id_rol):
    """
    Lee un rol de la base de datos por su ID.

    Args:
        id_rol (int): ID del rol a buscar.

    Returns:
        Rol: Objeto Rol si se encuentra, o None si no.
    """
    gestor = Roles()
    return gestor.buscar(id_rol)

def actualizar_rol(id_rol, nombre=None, descripcion=None):
    """
    Actualiza un rol existente en la base de datos.

    Args:
        id_rol (int): ID del rol a actualizar.
        nombre (str, optional): Nuevo nombre del rol.
        descripcion (str, optional): Nueva descripción del rol.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Roles()
    return gestor.actualizar(id_rol, nombre=nombre, descripcion=descripcion)

def eliminar_rol(id_rol):
    """
    Elimina un rol de la base de datos por su ID.

    Args:
        id_rol (int): ID del rol a eliminar.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Roles()
    return gestor.eliminar(id_rol)