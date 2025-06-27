from src.controlador.dominios.persona import Persona
from src.controlador.gestores.personas import Personas

def crear_persona(id_persona, nombre=None, apellido=None, email=None, telefono=None, dni=None, direccion=None, cp=None, poblacion=None, pais=None):
    """
    Crea una nueva persona en la base de datos.

    Args:
        id_persona (int): ID de la persona.
        nombre (str, optional): Nombre de la persona.
        apellido (str, optional): Apellido de la persona.
        email (str, optional): Email de la persona.
        telefono (str, optional): Teléfono de la persona.
        dni (str, optional): DNI de la persona.
        direccion (str, optional): Dirección de la persona.
        cp (str, optional): Código postal de la persona.
        poblacion (str, optional): Población de la persona.
        pais (str, optional): País de la persona.

    Returns:
        Persona: Objeto Persona creado, o None si falla.
    """
    gestor = Personas()
    return gestor.agregar(id_persona=id_persona, nombre=nombre, apellido=apellido, email=email, telefono=telefono, dni=dni, direccion=direccion, cp=cp, poblacion=poblacion, pais=pais)

def leer_persona(id_persona):
    """
    Lee una persona por su ID.

    Args:
        id_persona (int): ID de la persona.

    Returns:
        Persona: Objeto Persona si se encuentra, o None si no.
    """
    gestor = Personas()
    return gestor.buscar(id_persona)

def actualizar_persona(id_persona, nombre=None, apellido=None, email=None, telefono=None, dni=None, direccion=None, cp=None, poblacion=None, pais=None):
    """
    Actualiza una persona existente.

    Args:
        id_persona (int): ID de la persona.
        nombre (str, optional): Nuevo nombre.
        apellido (str, optional): Nuevo apellido.
        email (str, optional): Nuevo email.
        telefono (str, optional): Nuevo teléfono.
        dni (str, optional): Nuevo DNI.
        direccion (str, optional): Nueva dirección.
        cp (str, optional): Nuevo código postal.
        poblacion (str, optional): Nueva población.
        pais (str, optional): Nuevo país.

    Returns:
        bool: True si se actualizó, False si no.
    """
    gestor = Personas()
    return gestor.actualizar(id_persona, nombre=nombre, apellido=apellido, email=email, telefono=telefono, dni=dni, direccion=direccion, cp=cp, poblacion=poblacion, pais=pais)

def eliminar_persona(id_persona):
    """
    Elimina una persona por su ID.

    Args:
        id_persona (int): ID de la persona.

    Returns:
        bool: True si se eliminó, False si no.
    """
    gestor = Personas()
    return gestor.eliminar(id_persona)