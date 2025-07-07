import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.facturas import Facturas
from GeobizIA.controlador.gestores.clientes import Clientes
from GeobizIA.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    gestor = Facturas()
    # Elimina la factura con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

@pytest.fixture
def gestor_clientes():
    gestor = Clientes()
    # Elimina el cliente con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

@pytest.fixture
def gestor_personas():
    gestor = Personas()
    # Elimina la persona con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

def test_crud_factura(gestor, gestor_clientes, gestor_personas):
    persona = gestor_personas.agregar(
        id_persona=17,
        nombre="Ana",
        apellido="Gómez",
        email="ana.gomez@example.com",
        telefono="987654321",
        dni="87654321F",
        direccion="Calle Luna 789",
        cp="28006",
        poblacion="Barcelona",
        pais="España"
    )
    assert persona is not None

    cliente = gestor_clientes.agregar(
        id_cliente=17,
        id_persona=17,
        tipo="Premium",
        razon_social="Consultoría Gómez S.L.",
        nif="B12345678",
        fecha_registro="2025-06-27"
    )
    assert cliente is not None

    factura = gestor.agregar(
        id_factura=17,
        id_cliente=17,
        tipo="Factura Ordinaria",
        nombre="Consultoría Gómez S.L.",
        direccion="Calle Luna 789, Barcelona",
        nif="B12345678",
        fecha_facturacion="2025-06-27",
        fecha_vencimiento="2025-07-27",
        concepto="Servicios de consultoría",
        responsable="Juan Pérez",
        iva=21.0,
        coste_total=1210.0,
        base_imponible=1000.0,
        numero_factura="FAC-2025-001",
        tipo_pago="Transferencia",
        irpf=15.0
    )
    assert factura is not None

    factura_leida = gestor.buscar(17)
    assert factura_leida.tipo == "Factura Ordinaria"

    actualizado = gestor.actualizar(17, tipo="Factura Rectificativa", nombre="Consultoría Gómez S.L. Actualizada")
    assert actualizado
    assert gestor.buscar(17).tipo == "Factura Rectificativa"

    eliminado = gestor.eliminar(17)
    assert eliminado
    assert gestor.buscar(17) is None

    gestor_clientes.eliminar(17)
    gestor_personas.eliminar(17)