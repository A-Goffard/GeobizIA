import pytest
from src.controlador.gestores.factura_actividades import FacturaActividadGestor
from src.controlador.gestores.facturas import Facturas
from src.controlador.gestores.actividades import Actividades

@pytest.fixture
def gestor():
    return FacturaActividadGestor()

@pytest.fixture
def gestor_facturas():
    return Facturas()

@pytest.fixture
def gestor_actividades():
    return Actividades()

def test_crud_factura_actividad(gestor, gestor_facturas, gestor_actividades):
    # Crear actividad y factura necesarias para la relación
    actividad = gestor_actividades.agregar(
        id_actividad=1,
        tipo="Taller",
        nombre="Taller Test",
        descripcion="Test",
        responsable="Ana",
        duracion="1h",
        coste_economico=100.0,
        coste_horas=2.0,
        facturacion=200.0,
        resultados="OK",
        valoracion="Buena",
        observaciones="Ninguna"
    )
    assert actividad is not None

    factura = gestor_facturas.agregar(
        id_factura=1,
        id_cliente=1,  # Asegúrate de que el cliente 1 exista o crea uno si es necesario
        tipo="Factura Test",
        nombre="Cliente Test",
        direccion="Calle Test",
        nif="X12345678",
        fecha_facturacion="2025-06-27",
        fecha_vencimiento="2025-07-27",
        concepto="Test",
        responsable="Ana",
        iva=21.0,
        coste_total=100.0,
        base_imponible=80.0,
        numero_factura="TEST-001",
        tipo_pago="Transferencia",
        irpf=15.0
    )
    assert factura is not None

    # Crear relación factura-actividad
    fa = gestor.agregar(1, 1)
    assert fa is not None

    # Buscar relación
    leida = gestor.buscar(1, 1)
    assert leida is not None

    # Eliminar relación
    eliminada = gestor.eliminar(1, 1)
    assert eliminada
    assert gestor.buscar(1, 1) is None

    gestor_actividades.eliminar(1)
    gestor_facturas.eliminar(1)
