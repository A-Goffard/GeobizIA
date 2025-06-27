import pytest
from src.controlador.gestores.publicacion_tags import PublicacionTags
from src.controlador.dominios.publicacion_tag import PublicacionTag

@pytest.fixture
def gestor():
    return PublicacionTags()

def test_agregar_y_buscar(gestor):
    pt = gestor.agregar(id_publicacion=1, id_tag=1)
    assert pt is not None
    assert pt.id_publicacion == 1
    assert pt.id_tag == 1

    pt_encontrado = gestor.buscar(1, 1)
    assert pt_encontrado is not None
    assert pt_encontrado.id_publicacion == 1
    assert pt_encontrado.id_tag == 1

def test_eliminar(gestor):
    gestor.agregar(id_publicacion=2, id_tag=2)
    eliminado = gestor.eliminar(2, 2)
    assert eliminado

    pt_no_existe = gestor.buscar(2, 2)
    assert pt_no_existe is None

def test_listar_todos(gestor):
    gestor.agregar(id_publicacion=3, id_tag=3)
    todos = gestor.mostrar_todos_los_elem()
    assert any(isinstance(pt, PublicacionTag) for pt in todos)
