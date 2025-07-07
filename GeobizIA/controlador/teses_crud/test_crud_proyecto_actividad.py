import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.proyectos_actividad import ProyectoActividadGestor
from GeobizIA.controlador.gestores.proyectos import Proyectos
from GeobizIA.controlador.gestores.actividades import Actividades

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
    # Limpieza previa en orden correcto
    gestor.eliminar(13, 111)  # Elimina la relación primero
    gestor_actividades.eliminar(111)  # Luego la actividad
    gestor_proyectos.eliminar(13)     # Luego el proyecto

    proyecto = gestor_proyectos.agregar(
        id_proyecto=13,
        nombre="Proyecto Test",
        descripcion="Test",
        fecha_inicio="2021-01-01",
        fecha_fin="2021-12-31",
        poblacion="Madrid",
        responsable="Juan",
        estado="Activo",
        objetivos="Test",
        presupuesto=1000.0
    )
    assert proyecto is not None

    actividad = gestor_actividades.agregar(
        id_actividad=111,
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

    relacion = gestor.agregar(13, 111)
    assert relacion is not None

    encontrada = gestor.buscar(13, 111)
    assert encontrada is not None

    eliminado = gestor.eliminar(13, 111)
    assert eliminado
    assert gestor.buscar(13, 111) is None

    gestor_actividades.eliminar(111)
    gestor_proyectos.eliminar(13)
