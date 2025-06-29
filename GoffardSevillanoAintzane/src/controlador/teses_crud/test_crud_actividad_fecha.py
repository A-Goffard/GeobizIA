import pytest
from src.controlador.gestores.actividades_fecha import ActividadesFechaGestor
from src.controlador.gestores.actividades import Actividades
from src.controlador.gestores.fechas_actividad import Fechas_Actividad

@pytest.fixture
def gestor():
    return ActividadesFechaGestor()

@pytest.fixture
def gestor_actividades():
    return Actividades()

@pytest.fixture
def gestor_fechas():
    return Fechas_Actividad()

def test_crud_actividad_fecha(gestor, gestor_actividades, gestor_fechas):
    actividad = gestor_actividades.agregar(
        id_actividad=1,
        tipo="Conferencia",
        nombre="Evento Anual",
        descripcion="Evento de tecnología",
        responsable="Juan Pérez",
        duracion="2 horas",
        coste_economico=1000.0,
        coste_horas=20.0,
        facturacion=1500.0,
        resultados="Éxito",
        valoracion="Positiva",
        observaciones="Ninguna"
    )
    assert actividad is not None

    fecha = gestor_fechas.agregar(
        id_fecha=1,
        fecha="2025-12-31"
    )
    assert fecha is not None

    actividad_fecha = gestor.agregar(1, 1)
    assert actividad_fecha is not None

    actividad_fecha_leida = gestor.buscar(1, 1)
    assert actividad_fecha_leida is not None

    eliminado = gestor.eliminar(1, 1)
    assert eliminado
    assert gestor.buscar(1, 1) is None

    gestor_actividades.eliminar(1)
    gestor_fechas.eliminar(1)
