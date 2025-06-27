from src.controlador.dominios.usuario import Usuario
from src.controlador.gestores.usuarios import Usuarios

def crear_usuario(id_usuario, id_persona, fecha_nacimiento=None, rol=None, preferencias=None, password=None):
    """
    Crea un nuevo usuario en la base de datos.

    Args:
        id_usuario (int): ID del usuario.
        id_persona (int): ID de la persona asociada.
        fecha_nacimiento (str, optional): Fecha de nacimiento del usuario.
        rol (str, optional): Rol del usuario.
        preferencias (str, optional): Preferencias del usuario.
        password (str, optional): Contraseña del usuario.

    Returns:
        Usuario: Objeto Usuario creado, o None si falla.
    """
    gestor = Usuarios()
    return gestor.agregar(id_usuario=id_usuario, id_persona=id_persona, fecha_nacimiento=fecha_nacimiento, rol=rol, preferencias=preferencias, password=password)

def leer_usuario(id_usuario):
    """
    Lee un usuario por su ID.

    Args:
        id_usuario (int): ID del usuario.

    Returns:
        Usuario: Objeto Usuario si se encuentra, o None si no.
    """
    gestor = Usuarios()
    return gestor.buscar(id_usuario)

def actualizar_usuario(id_usuario, id_persona=None, fecha_nacimiento=None, rol=None, preferencias=None, password=None):
    """
    Actualiza un usuario existente.

    Args:
        id_usuario (int): ID del usuario.
        id_persona (int, optional): Nuevo ID de la persona asociada.
        fecha_nacimiento (str, optional): Nueva fecha de nacimiento.
        rol (str, optional): Nuevo rol.
        preferencias (str, optional): Nuevas preferencias.
        password (str, optional): Nueva contraseña.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Usuarios()
    return gestor.actualizar(id_usuario, id_persona=id_persona, fecha_nacimiento=fecha_nacimiento, rol=rol, preferencias=preferencias, password=password)

def eliminar_usuario(id_usuario):
    """
    Elimina un usuario por su ID.

    Args:
        id_usuario (int): ID del usuario.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Usuarios()
    return gestor.eliminar(id_usuario)