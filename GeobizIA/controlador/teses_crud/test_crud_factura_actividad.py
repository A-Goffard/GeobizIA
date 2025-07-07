import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.factura_actividades import FacturaActividadGestor
from GeobizIA.controlador.gestores.facturas import Facturas
from GeobizIA.controlador.gestores.actividades import Actividades
from GeobizIA.controlador.gestores.clientes import Clientes
from GeobizIA.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    return FacturaActividadGestor()

@pytest.fixture
def gestor_facturas():
    gestor = Facturas()
    # Elimina la factura con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

@pytest.fixture
def gestor_actividades():
    gestor = Actividades()
    # Elimina la actividad con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

@pytest.fixture
def gestor_personas():
    # Elimina relaciones dependientes antes de eliminar la persona
    FacturaActividadGestor().eliminar(17, 17)
    Facturas().eliminar(17)
    Actividades().eliminar(17)
    Clientes().eliminar(17)
    gestor = Personas()
    gestor.eliminar(17)
    return gestor

@pytest.fixture
def gestor_clientes():
    gestor = Clientes()
    # Elimina el cliente con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

def test_crud_factura_actividad(gestor, gestor_facturas, gestor_actividades, gestor_clientes, gestor_personas):
    # Crear persona necesaria para el cliente solo si no existe
    persona = gestor_personas.buscar(17)
    if persona is None:
        persona = gestor_personas.agregar(
            id_persona=17,
            nombre="Persona Test",
            apellido="Apellido Test",
            email="persona@test.com",
            telefono="123456789",
            dni="X1234567T",
            direccion="Calle Persona",
            cp="28000",
            poblacion="Madrid",
            pais="España"
        )
    assert persona is not None

    # Crear cliente necesario para la factura solo si no existe
    cliente = gestor_clientes.buscar(17)
    if cliente is None:
        cliente = gestor_clientes.agregar(
            id_cliente=17,
            id_persona=17,
            tipo="Cliente Test",
            razon_social="Cliente Test S.L.",
            nif="X12345678",
            fecha_registro="2025-06-27"
        )
    assert cliente is not None

    # Crear actividad necesaria para la factura solo si no existe
    actividad = gestor_actividades.buscar(17)
    if actividad is None:
        actividad = gestor_actividades.agregar(
            id_actividad=17,
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

    # Crear factura necesaria para la relación solo si no existe
    factura = gestor_facturas.buscar(17)
    if factura is None:
        factura = gestor_facturas.agregar(
            id_factura=17,
            id_cliente=17,
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

    # Crear relación factura-actividad solo si no existe
    fa = gestor.buscar(17, 17)
    if fa is None:
        fa = gestor.agregar(17, 17)
    assert fa is not None

    # Buscar relación
    leida = gestor.buscar(17, 17)
    assert leida is not None

    # Eliminar relación
    eliminada = gestor.eliminar(17, 17)
    assert eliminada
    assert gestor.buscar(17, 17) is None

    gestor_actividades.eliminar(17)
    gestor_facturas.eliminar(17)
    gestor_clientes.eliminar(17)
    gestor_clientes.eliminar(17)
    gestor_personas.eliminar(17)
    
    assert eliminada
    assert gestor.buscar(17, 17) is None

    gestor_actividades.eliminar(17)
    gestor_facturas.eliminar(17)
    gestor_clientes.eliminar(17)
    gestor_clientes.eliminar(17)
    gestor_personas.eliminar(17)
