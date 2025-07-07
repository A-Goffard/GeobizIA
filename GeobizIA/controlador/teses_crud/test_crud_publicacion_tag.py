import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.dominios.publicacion_tag import PublicacionTag
from GeobizIA.controlador.gestores.publicacion_tags import PublicacionTags
from GeobizIA.controlador.gestores.publicaciones import Publicaciones
from GeobizIA.controlador.gestores.tags import Tags

@pytest.fixture
def gestor():
    gestor = PublicacionTags()
    # Elimina la relación con id_publicacion=1 y id_tag=1 si existe
    gestor.eliminar(1, 1)
    return gestor

@pytest.fixture
def gestor_publicaciones():
    gestor = Publicaciones()
    # Elimina la publicación con id=1 si existe
    gestor.eliminar(1)
    return gestor

@pytest.fixture
def gestor_tags():
    gestor = Tags()
    # Elimina el tag con id=1 si existe
    gestor.eliminar(1)
    return gestor

def test_crud_publicacion_tag(gestor, gestor_publicaciones, gestor_tags):
    # Crear publicación y tag necesarios
    gestor_publicaciones.eliminar(1)
    # Elimina primero los registros dependientes de tag
    import pyodbc
    from GeobizIA.modelo.database.db_conexion import get_connection, close_connection
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM tema_ambiental_tag WHERE id_tag = ?", (1,))
        cursor.execute("DELETE FROM recurso_multimedia_tag WHERE id_tag = ?", (1,))
        conn.commit()
    finally:
        close_connection(conn, cursor)
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
