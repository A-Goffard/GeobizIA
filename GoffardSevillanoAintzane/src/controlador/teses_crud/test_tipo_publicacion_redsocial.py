import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.tipo_publicacion_redsocial import TipoPublicacionRedSocialGestor

@pytest.fixture
def gestor():
    return TipoPublicacionRedSocialGestor()

def test_crud_tipo_publicacion_redsocial(gestor):
    id_tipo_publicacion = 1
    id_red_social = 2

    agregado = gestor.agregar(id_tipo_publicacion, id_red_social)
    assert agregado is not None

    encontrado = gestor.buscar(id_tipo_publicacion, id_red_social)
    assert encontrado is not None
    assert encontrado.id_tipo_publicacion == id_tipo_publicacion
    assert encontrado.id_red_social == id_red_social

    eliminado = gestor.eliminar(id_tipo_publicacion, id_red_social)
    assert eliminado
    assert gestor.buscar(id_tipo_publicacion, id_red_social) is None