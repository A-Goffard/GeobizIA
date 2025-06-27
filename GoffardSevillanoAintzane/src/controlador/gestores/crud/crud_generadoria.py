from src.controlador.dominios.generadoria import GeneradorIA
from src.controlador.gestores.generadoresia import GeneradoresIA

def crear_generador_IA(id_generador_IA, id_usuario, nombre=None, descripcion=None, tipo=None):
    """
    Crea un nuevo generador_IA en la base de datos.

    Args:
        id_generador_IA (int): ID del generador_IA.
        id_usuario (int): ID del usuario asociado.
        nombre (str, optional): Nombre del generador_IA.
        descripcion (str, optional): Descripción del generador_IA.
        tipo (str, optional): Tipo del generador_IA.

    Returns:
        GeneradorIA: Objeto GeneradorIA creado, o None si falla.
    """
    gestor = GeneradoresIA()
    return gestor.agregar(id_generador_IA=id_generador_IA, id_usuario=id_usuario, nombre=nombre, descripcion=descripcion, tipo=tipo)

def leer_generador_IA(id_generador_IA):
    """
    Lee un generador_IA por su ID.

    Args:
        id_generador_IA (int): ID del generador_IA.

    Returns:
        GeneradorIA: Objeto GeneradorIA si se encuentra, o None si no.
    """
    gestor = GeneradoresIA()
    return gestor.buscar(id_generador_IA)

def actualizar_generador_IA(id_generador_IA, id_usuario=None, nombre=None, descripcion=None, tipo=None):
    """
    Actualiza un generador_IA existente.

    Args:
        id_generador_IA (int): ID del generador_IA.
        id_usuario (int, optional): Nuevo ID del usuario asociado.
        nombre (str, optional): Nuevo nombre.
        descripcion (str, optional): Nueva descripción.
        tipo (str, optional): Nuevo tipo.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = GeneradoresIA()
    return gestor.actualizar(id_generador_IA, id_usuario=id_usuario, nombre=nombre, descripcion=descripcion, tipo=tipo)

def eliminar_generador_IA(id_generador_IA):
    """
    Elimina un generador_IA por su ID.

    Args:
        id_generador_IA (int): ID del generador_IA.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = GeneradoresIA()
    return gestor.eliminar(id_generador_IA)