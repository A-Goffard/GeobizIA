import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.dominios.publicacion_tag import PublicacionTag
from src.controlador.gestores.publicacion_tags import PublicacionTags
from src.controlador.gestores.publicaciones import Publicaciones
from src.controlador.gestores.tags import Tags

@pytest.fixture
def gestor():
    return PublicacionTags()

@pytest.fixture
def gestor_publicaciones():
    return Publicaciones()

@pytest.fixture
def gestor_tags():
    return Tags()

def test_crud_publicacion_tag(gestor, gestor_publicaciones, gestor_tags):
    # Crear publicación y tag necesarios
    gestor_publicaciones.eliminar(1)
    gestor_tags.eliminar(1)
    gestor.eliminar(1, 1)

    publicacion = gestor_publicaciones.agregar(
        id_publicacion=1,
        titulo="Test",
        contenido="Contenido",
        autor="Autor",
        fecha_creacion="2025-01-01",
        estado="borrador",
        tags="",
        palabras_clave="",
        generada_por_ia=False,
        id_generador_ia=None,
        feedback_empresa="",
        id_tipo_publicacion=None,
        id_plantilla=None
    )
    assert publicacion is not None

    tag = gestor_tags.agregar(
        id_tag=1,
        palabra_clave="clave",
        categoria="cat",
        frecuencia_uso=1
    )
    assert tag is not None

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

    gestor_publicaciones.eliminar(1)
    gestor_tags.eliminar(1)

def test_listar_todos(gestor, gestor_publicaciones, gestor_tags):
    # Crear publicación y tag necesarios
    gestor_publicaciones.eliminar(3)
    gestor_tags.eliminar(3)
    gestor.eliminar(3, 3)

    publicacion = gestor_publicaciones.agregar(
        id_publicacion=3,
        titulo="Test3",
        contenido="Contenido3",
        autor="Autor3",
        fecha_creacion="2025-01-03",
        estado="borrador",
        tags="",
        palabras_clave="",
        generada_por_ia=False,
        id_generador_ia=None,
        feedback_empresa="",
        id_tipo_publicacion=None,
        id_plantilla=None
    )
    assert publicacion is not None

    tag = gestor_tags.agregar(
        id_tag=3,
        palabra_clave="clave3",
        categoria="cat3",
        frecuencia_uso=1
    )
    assert tag is not None

    gestor.agregar(id_publicacion=3, id_tag=3)
    todos = gestor.mostrar_todos_los_elem()
    assert any(isinstance(pt, PublicacionTag) for pt in todos)

    gestor.eliminar(3, 3)
    gestor_publicaciones.eliminar(3)
    gestor_tags.eliminar(3)
