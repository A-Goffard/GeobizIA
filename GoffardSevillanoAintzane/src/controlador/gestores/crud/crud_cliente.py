from src.controlador.dominios.cliente import Cliente
from src.controlador.gestores.clientes import Clientes

def crear_cliente(id_cliente, id_persona, tipo=None, razon_social=None, nif=None, fecha_registro=None):
    """
    Crea un nuevo cliente en la base de datos.

    Args:
        id_cliente (int): ID del cliente.
        id_persona (int): ID de la persona asociada.
        tipo (str, optional): Tipo de cliente (ej. 'Individual', 'Empresa').
        razon_social (str, optional): Razón social del cliente.
        nif (str, optional): NIF del cliente.
        fecha_registro (str, optional): Fecha de registro del cliente.

    Returns:
        Cliente: Objeto Cliente creado, o None si falla.
    """
    gestor = Clientes()
    return gestor.agregar(id_cliente=id_cliente, id_persona=id_persona, tipo=tipo, razon_social=razon_social, nif=nif, fecha_registro=fecha_registro)

def leer_cliente(id_cliente):
    """
    Lee un cliente por su ID.

    Args:
        id_cliente (int): ID del cliente.

    Returns:
        Cliente: Objeto Cliente si se encuentra, o None si no.
    """
    gestor = Clientes()
    return gestor.buscar(id_cliente)

def actualizar_cliente(id_cliente, id_persona=None, tipo=None, razon_social=None, nif=None, fecha_registro=None):
    """
    Actualiza un cliente existente.

    Args:
        id_cliente (int): ID del cliente.
        id_persona (int, optional): Nuevo ID de la persona asociada.
        tipo (str, optional): Nuevo tipo de cliente.
        razon_social (str, optional): Nueva razón social.
        nif (str, optional): Nuevo NIF.
        fecha_registro (str, optional): Nueva fecha de registro.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Clientes()
    return gestor.actualizar(id_cliente, id_persona=id_persona, tipo=tipo, razon_social=razon_social, nif=nif, fecha_registro=fecha_registro)

def eliminar_cliente(id_cliente):
    """
    Elimina un cliente por su ID.

    Args:
        id_cliente (int): ID del cliente.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Clientes()
    return gestor.eliminar(id_cliente)