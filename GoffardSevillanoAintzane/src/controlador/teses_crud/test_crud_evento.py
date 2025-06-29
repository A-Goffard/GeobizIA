import pytest
from src.controlador.gestores.eventos import Eventos

@pytest.fixture
def gestor():
    return Eventos()

def test_crud_evento(gestor):
    # Crear un evento
    evento = gestor.agregar(
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

    # Leer el evento
    evento_leido = gestor.buscar(1)
    assert evento_leido.nombre == "Conferencia de Tecnología"

    # Actualizar el evento
    actualizado = gestor.actualizar(1, nombre="Conferencia de Tecnología Actualizada", tipo="Conferencia Internacional")
    assert actualizado
    assert gestor.buscar(1).nombre == "Conferencia de Tecnología Actualizada"
    assert gestor.buscar(1).tipo == "Conferencia Internacional"

    # Eliminar el evento
    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

if __name__ == "__main__":
    pytest.main()