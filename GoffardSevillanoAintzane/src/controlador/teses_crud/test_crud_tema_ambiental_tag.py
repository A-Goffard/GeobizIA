import pytest
from src.controlador.gestores.temas_ambientales_tag import TemaAmbientalTagGestor


@pytest.fixture
def gestor():
    return TemaAmbientalTagGestor()


def test_crud_tema_ambiental_tag(gestor):
    # Crear relación
    relacion = gestor.agregar(1, 10)
    assert relacion is not None

    # Buscar relación
    encontrada = gestor.buscar(1, 10)
    assert encontrada is not None

    # Eliminar relación
    eliminado = gestor.eliminar(1, 10)
    assert eliminado
    assert gestor.buscar(1, 10) is None
    print(f"Eliminada relación: {eliminada}")

if __name__ == "__main__":
    test_crud_tema_ambiental_tag()
