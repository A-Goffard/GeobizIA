import pytest
from src.controlador.gestores.actividad_eventos import ActividadEventosGestor
from src.controlador.gestores.actividades import Actividades
from src.controlador.gestores.eventos import Eventos

@pytest.fixture
def gestor():
    return ActividadEventosGestor()

@pytest.fixture
def gestor_actividades():
    return Actividades()

@pytest.fixture
def gestor_eventos():
    return Eventos()

def test_crud_actividad_evento(gestor, gestor_actividades, gestor_eventos):
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

    evento = gestor_eventos.agregar(
        id_evento=1,
        nombre="Conferencia de Tecnología",
        tipo="Conferencia",
        lugar="Centro de Convenciones",
        fecha_comienzo="2025-07-01",
        fecha_final="2025-07-03",
        poblacion="Madrid",
        tematica="Innovación Tecnológica"
    )
    assert evento is not None

    relacion = gestor.agregar(1, 1)
    assert relacion is not None

    encontrada = gestor.buscar(1, 1)
    assert encontrada is not None

    eliminado = gestor.eliminar(1, 1)
    assert eliminado
    assert gestor.buscar(1, 1) is None

    gestor_actividades.eliminar(1)
    gestor_eventos.eliminar(1)
