import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.actividades_fecha import ActividadesFechaGestor
from GeobizIA.controlador.gestores.actividades import Actividades
from GeobizIA.controlador.gestores.fechas_actividad import Fechas_Actividad

@pytest.fixture
def gestor():
    gestor = ActividadesFechaGestor()
    # Elimina la relación con id_actividad=1 y id_fecha=1 si existe
    gestor.eliminar(1, 1)
    return gestor

@pytest.fixture
def gestor_actividades():
    gestor = Actividades()
    # Elimina la actividad con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

@pytest.fixture
def gestor_fechas():
    gestor = Fechas_Actividad()
    # Elimina la fecha de actividad con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

def test_crud_actividad_fecha(gestor, gestor_actividades, gestor_fechas):
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

    # No pases id_fecha, deja que la base de datos lo genere
    fecha = gestor_fechas.agregar(
        fecha="2025-12-31"
    )
    assert fecha is not None

    # Usa el id generado para la relación
    actividad_fecha = gestor.agregar(1, fecha.id_fecha)
    assert actividad_fecha is not None

    actividad_fecha_leida = gestor.buscar(1, fecha.id_fecha)
    assert actividad_fecha_leida is not None

    eliminado = gestor.eliminar(1, fecha.id_fecha)
    assert eliminado
    assert gestor.buscar(1, fecha.id_fecha) is None

    gestor_actividades.eliminar(1)
    gestor_fechas.eliminar(fecha.id_fecha)
