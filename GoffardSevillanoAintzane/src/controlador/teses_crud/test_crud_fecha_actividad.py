import pytest
from src.controlador.gestores.fechas_actividad import Fechas_Actividad

@pytest.fixture
def gestor():
    return Fechas_Actividad()

def test_crud_fecha_actividad(gestor):
    fecha_actividad = gestor.agregar(
        id_fecha=1,
        fecha="2025-07-01"
    )
    assert fecha_actividad is not None

    fecha_actividad_leida = gestor.buscar(1)
    assert fecha_actividad_leida.fecha == "2025-07-01"

    actualizado = gestor.actualizar(1, fecha="2025-07-02")
    assert actualizado
    assert gestor.buscar(1).fecha == "2025-07-02"

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None