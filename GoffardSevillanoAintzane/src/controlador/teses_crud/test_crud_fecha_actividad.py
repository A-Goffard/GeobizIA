import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.fechas_actividad import Fechas_Actividad

@pytest.fixture
def gestor():
    gestor = Fechas_Actividad()
    # Elimina la fecha de actividad con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

def test_crud_fecha_actividad(gestor):
    # Crear una fecha de actividad (sin id_fecha, lo asigna la BD)
    fecha_actividad = gestor.agregar(
        fecha="2025-07-01"
    )
    assert fecha_actividad is not None

    id_fecha = fecha_actividad.id_fecha

    fecha_actividad_leida = gestor.buscar(id_fecha)
    assert fecha_actividad_leida.fecha == "2025-07-01"

    actualizado = gestor.actualizar(id_fecha, fecha="2025-07-02")
    assert actualizado
    assert gestor.buscar(id_fecha).fecha == "2025-07-02"

    eliminado = gestor.eliminar(id_fecha)
    assert eliminado
    assert gestor.buscar(id_fecha) is None