import pytest
from src.controlador.gestores.plantilla_tipo_publicacion import PlantillaTipoPublicacionGestor

@pytest.fixture
def gestor():
    return PlantillaTipoPublicacionGestor()

def test_agregar_y_buscar(gestor):
    id_plantilla = 1
    id_tipo_publicacion = 2
    agregado = gestor.agregar(id_plantilla, id_tipo_publicacion)
    assert agregado is not None

    encontrado = gestor.buscar(id_plantilla, id_tipo_publicacion)
    assert encontrado is not None
    assert encontrado.id_plantilla == id_plantilla
    assert encontrado.id_tipo_publicacion == id_tipo_publicacion

def test_eliminar(gestor):
    id_plantilla = 3
    id_tipo_publicacion = 4
    gestor.agregar(id_plantilla, id_tipo_publicacion)
    eliminado = gestor.eliminar(id_plantilla, id_tipo_publicacion)
    assert eliminado
    no_existe = gestor.buscar(id_plantilla, id_tipo_publicacion)
    assert no_existe is None
