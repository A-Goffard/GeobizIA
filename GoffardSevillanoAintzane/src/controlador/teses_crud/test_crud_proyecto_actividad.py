import pytest
from src.controlador.gestores.proyectos_actividad import ProyectoActividadGestor
from src.controlador.gestores.proyectos import Proyectos
from src.controlador.gestores.actividades import Actividades

@pytest.fixture
def gestor():
    return ProyectoActividadGestor()

@pytest.fixture
def gestor_proyectos():
    return Proyectos()

@pytest.fixture
def gestor_actividades():
    return Actividades()

def test_crud_proyecto_actividad(gestor, gestor_proyectos, gestor_actividades):
    proyecto = gestor_proyectos.agregar(
        id_proyecto=1,
        nombre="Proyecto Test",
        descripcion="Test",
        fecha_inicio="2025-01-01",
        fecha_fin="2025-12-31",
        poblacion="Madrid",
        responsable="Juan",
        estado="Activo",
        objetivos="Test",
        presupuesto=1000.0
    )
    assert proyecto is not None

    actividad = gestor_actividades.agregar(
        id_actividad=101,
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

    relacion = gestor.agregar(1, 101)
    assert relacion is not None

    encontrada = gestor.buscar(1, 101)
    assert encontrada is not None

    eliminado = gestor.eliminar(1, 101)
    assert eliminado
    assert gestor.buscar(1, 101) is None

    gestor_proyectos.eliminar(1)
    gestor_actividades.eliminar(101)
