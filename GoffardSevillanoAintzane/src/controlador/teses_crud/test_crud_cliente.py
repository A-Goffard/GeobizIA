import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from src.controlador.gestores.clientes import Clientes
from src.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    return Clientes()

@pytest.fixture
def gestor_personas():
    return Personas()

def test_crud_cliente(gestor, gestor_personas):
    # Crear persona necesaria para la clave foránea
    persona = gestor_personas.agregar(
        id_persona=1,
        nombre="Ana",
        apellido="Gómez",
        email="ana.gomez@example.com",
        telefono="987654321",
        dni="87654321B",
        direccion="Avenida Siempre Viva 456",
        cp="28002",
        poblacion="Barcelona",
        pais="España"
    )
    assert persona is not None

    cliente = gestor.agregar(
        id_cliente=1,
        id_persona=1,
        tipo="Empresa",
        razon_social="Cliente S.L.",
        nif="B12345678",
        fecha_registro="2025-06-29"
    )
    assert cliente is not None

    cliente_leido = gestor.buscar(1)
    assert cliente_leido.tipo == "Empresa"

    actualizado = gestor.actualizar(1, tipo="Particular")
    assert actualizado
    assert gestor.buscar(1).tipo == "Particular"

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

    # Limpieza: eliminar la persona creada
    gestor_personas.eliminar(1)
