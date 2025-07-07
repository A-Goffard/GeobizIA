import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.temas_ambientales import Temas_Ambientales

@pytest.fixture
def gestor():
    return Temas_Ambientales()

def test_crud_tema_ambiental(gestor):
    tema = gestor.agregar(
        id_tema_ambiental=3,
        nombre="Cambio Climático",
        descripcion="Tema relacionado con el calentamiento global y sus impactos",
        relevancia="Alta"
    )
    assert tema is not None

    tema_leido = gestor.buscar(3)
    assert tema_leido.nombre == "Cambio Climático"

    actualizado = gestor.actualizar(3, nombre="Cambio Climático Actualizado", relevancia="Media")
    assert actualizado
    assert gestor.buscar(3).nombre == "Cambio Climático Actualizado"
    assert gestor.buscar(3).relevancia == "Media"

    eliminado = gestor.eliminar(3)
    assert eliminado
    assert gestor.buscar(3) is None

if __name__ == "__main__":
    test_crud_tema_ambiental()