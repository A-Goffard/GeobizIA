from src.controlador.dominios.empresa import Empresa
from src.controlador.gestores.empresas import Empresas

def crear_empresa(id_empresa, id_persona, razon_social=None, nif=None, sector=None, tamano=None, fecha_registro=None):
    """
    Crea una nueva empresa en la base de datos.

    Args:
        id_empresa (int): ID de la empresa.
        id_persona (int): ID de la persona asociada.
        razon_social (str, optional): Razón social de la empresa.
        nif (str, optional): NIF de la empresa.
        sector (str, optional): Sector de la empresa.
        tamano (str, optional): Tamaño de la empresa (ej. 'Pequeña', 'Mediana', 'Grande').
        fecha_registro (str, optional): Fecha de registro de la empresa.

    Returns:
        Empresa: Objeto Empresa creado, o None si falla.
    """
    gestor = Empresas()
    return gestor.agregar(id_empresa=id_empresa, id_persona=id_persona, razon_social=razon_social, nif=nif, sector=sector, tamano=tamano, fecha_registro=fecha_registro)

def leer_empresa(id_empresa):
    """
    Lee una empresa por su ID.

    Args:
        id_empresa (int): ID de la empresa.

    Returns:
        Empresa: Objeto Empresa si se encuentra, o None si no.
    """
    gestor = Empresas()
    return gestor.buscar(id_empresa)

def actualizar_empresa(id_empresa, id_persona=None, razon_social=None, nif=None, sector=None, tamano=None, fecha_registro=None):
    """
    Actualiza una empresa existente.

    Args:
        id_empresa (int): ID de la empresa.
        id_persona (int, optional): Nuevo ID de la persona asociada.
        razon_social (str, optional): Nueva razón social.
        nif (str, optional): Nuevo NIF.
        sector (str, optional): Nuevo sector.
        tamano (str, optional): Nuevo tamaño.
        fecha_registro (str, optional): Nueva fecha de registro.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Empresas()
    return gestor.actualizar(id_empresa, id_persona=id_persona, razon_social=razon_social, nif=nif, sector=sector, tamano=tamano, fecha_registro=fecha_registro)

def eliminar_empresa(id_empresa):
    """
    Elimina una empresa por su ID.

    Args:
        id_empresa (int): ID de la empresa.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Empresas()
    return gestor.eliminar(id_empresa)