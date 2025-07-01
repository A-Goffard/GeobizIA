import pytest
from src.controlador.gestores.programaciones import Programaciones

@pytest.fixture
def gestor():
    return Programaciones()

def test_crud_programacion(gestor):
    # Crear una programación
    programacion = gestor.agregar(
        id_programacion=1,
        publicacion_id=1,
        red_social_id=1,
        fecha_programada="2025-07-10",
        estado="Programado",
        notificaciones="",
        responsable="María López"
    )
    assert programacion is not None

    # Leer programación
    programacion_leida = gestor.buscar(1)
    assert programacion_leida is not None

    # Actualizar programación
    actualizado = gestor.actualizar(1, estado="Reprogramado")
    assert actualizado
    assert gestor.buscar(1).estado == "Reprogramado"

    # Eliminar programación
    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None
    programacion_eliminada = gestor.buscar(programacion.id_programacion)
    print(f"Programación después de eliminar: {programacion_eliminada}")

if __name__ == "__main__":
    test_crud_programacion()
