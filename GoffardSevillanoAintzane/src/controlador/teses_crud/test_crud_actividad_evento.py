import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.actividad_eventos import ActividadEventosGestor
from src.controlador.gestores.actividades import Actividades
from src.controlador.gestores.eventos import Eventos

@pytest.fixture
def gestor():
    gestor = ActividadEventosGestor()
    # Elimina la relación con id_actividad=1 y id_evento=1 si existe
    gestor.eliminar(1, 1)  
    return gestor

@pytest.fixture
def gestor_actividades():
    gestor = Actividades()
    # Elimina la actividad con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

@pytest.fixture
def gestor_eventos():
    gestor = Eventos()
    # Elimina el evento con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

def test_crud_actividad_evento(gestor, gestor_actividades, gestor_eventos):
    actividad = gestor_actividades.buscar(1)
    if actividad is None:
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

    evento = gestor_eventos.buscar(1)
    if evento is None:
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
