import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    return Personas()

def test_crud_persona(gestor):
    # Crear una persona
    persona = gestor.agregar(
        id_persona=1,
        nombre="Juan",
        apellido="Pérez",
        email="juan.perez@example.com",
        telefono="123456789",
        dni="12345678A",
        direccion="Calle Falsa 123",
        cp="28001",
        poblacion="Madrid",
        pais="España"
    )
    assert persona is not None
    print(f"Persona creada: {persona}")

    # Leer la persona
    persona_leida = gestor.buscar(1)
    assert persona_leida is not None
    print(f"Persona leída: {persona_leida}")

    # Actualizar la persona
    actualizado = gestor.actualizar(
        1,
        nombre="María",
        apellido="López",
        email="maria.lopez@example.com"
    )
    assert actualizado
    persona_leida = gestor.buscar(1)
    assert persona_leida.nombre == "María"
    assert persona_leida.apellido == "López"
    assert persona_leida.email == "maria.lopez@example.com"
    print(f"Persona después de actualizar: {persona_leida}")

    # Eliminar la persona
    eliminado = gestor.eliminar(1)
    assert eliminado
    persona_leida = gestor.buscar(1)
    assert persona_leida is None
    print(f"Persona después de eliminar: {persona_leida}")
