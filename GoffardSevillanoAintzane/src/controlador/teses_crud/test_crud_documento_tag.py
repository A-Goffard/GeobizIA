import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.documentos_tag import DocumentosTagGestor
from src.controlador.gestores.documentos import Documentos
from src.controlador.gestores.tags import Tags

@pytest.fixture
def gestor():
    return DocumentosTagGestor()

@pytest.fixture(autouse=True)
def setup_documentos_tags():
    # Crear documentos y tags necesarios para los tests
    Documentos().agregar(
        id_documento=1,
        titulo="Doc1",
        descripcion="desc",
        fecha_subida="2025-01-01",
        tipo="tipo",
        tematica="tematica"
    )
    Documentos().agregar(
        id_documento=2,
        titulo="Doc2",
        descripcion="desc",
        fecha_subida="2025-01-01",
        tipo="tipo",
        tematica="tematica"
    )
    Tags().agregar(id_tag=10, palabra_clave="Tag10", categoria="General")
    Tags().agregar(id_tag=20, palabra_clave="Tag20", categoria="General")
    Tags().agregar(id_tag=21, palabra_clave="Tag21", categoria="General")
    Tags().agregar(id_tag=30, palabra_clave="Tag30", categoria="General")

def test_agregar_y_buscar(gestor):
    # Crear relación
    id_documento = 1
    id_tag = 10

    # Elimina la relación si ya existe
    gestor.eliminar(id_documento, id_tag)
    agregado = gestor.agregar(id_documento, id_tag)
    assert agregado is not None, "No se pudo agregar relación documento-tag"

    # Buscar relación
    resultado = gestor.buscar(id_documento, id_tag)
    assert resultado is not None, "No se encontró relación documento-tag"
    assert resultado.id_documento == id_documento
    assert resultado.id_tag == id_tag

def test_eliminar(gestor):
    id_documento = 2
    id_tag1 = 20
    id_tag2 = 21

    # Elimina relaciones si ya existen
    gestor.eliminar(id_documento, id_tag1)
    gestor.eliminar(id_documento, id_tag2)

    gestor.agregar(id_documento, id_tag1)
    gestor.agregar(id_documento, id_tag2)

    eliminado = gestor.eliminar(id_documento, id_tag1)
    assert eliminado
    resultado = gestor.buscar(id_documento, id_tag1)
    assert resultado is None

    lista = [rel for rel in gestor.listar() if rel.id_documento == id_documento]
    assert len(lista) >= 1
    for relacion in lista:
        assert relacion.id_documento == id_documento
        id_tag = relacion.id_tag
        gestor.agregar(id_documento=id_documento, id_tag=id_tag)
        eliminado = gestor.eliminar(id_documento, id_tag)
        assert eliminado, "No se pudo eliminar relación documento-tag"

        resultado = gestor.buscar(id_documento, id_tag)
        assert resultado is None, "Relación documento-tag no fue eliminada"


