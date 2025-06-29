import pytest
from src.controlador.gestores.facturas import Facturas
from src.controlador.gestores.clientes import Clientes
from src.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    return Facturas()

@pytest.fixture
def gestor_clientes():
    return Clientes()

@pytest.fixture
def gestor_personas():
    return Personas()

def test_crud_factura(gestor, gestor_clientes, gestor_personas):
    persona = gestor_personas.agregar(
        id_persona=1,
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
        id_cliente=1,
        id_persona=1,
        tipo="Premium",
        razon_social="Consultoría Gómez S.L.",
        nif="B12345678",
        fecha_registro="2025-06-27"
    )
    assert cliente is not None

    factura = gestor.agregar(
        id_factura=1,
        id_cliente=1,
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

    factura_leida = gestor.buscar(1)
    assert factura_leida.tipo == "Factura Ordinaria"

    actualizado = gestor.actualizar(1, tipo="Factura Rectificativa", nombre="Consultoría Gómez S.L. Actualizada")
    assert actualizado
    assert gestor.buscar(1).tipo == "Factura Rectificativa"

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

    gestor_clientes.eliminar(1)
    gestor_personas.eliminar(1)