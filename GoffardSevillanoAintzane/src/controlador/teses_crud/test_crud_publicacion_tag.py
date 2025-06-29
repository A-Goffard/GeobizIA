import pytest
from src.controlador.gestores.publicacion_tags import PublicacionTags

@pytest.fixture
def gestor():
    return PublicacionTags()

def test_crud_publicacion_tag(gestor):
    pt = gestor.agregar(id_publicacion=1, id_tag=1)
    assert pt is not None
    assert pt.id_publicacion == 1
    assert pt.id_tag == 1

    pt_encontrado = gestor.buscar(1, 1)
    assert pt_encontrado is not None
    assert pt_encontrado.id_publicacion == 1
    assert pt_encontrado.id_tag == 1

    eliminado = gestor.eliminar(1, 1)
    assert eliminado
    assert gestor.buscar(1, 1) is None
    eliminado = gestor.eliminar(2, 2)
    assert eliminado

    pt_no_existe = gestor.buscar(2, 2)
    assert pt_no_existe is None

def test_listar_todos(gestor):
    gestor.agregar(id_publicacion=3, id_tag=3)
    todos = gestor.mostrar_todos_los_elem()
    assert any(isinstance(pt, PublicacionTag) for pt in todos)
