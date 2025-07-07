import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.temas_ambientales_tag import TemaAmbientalTagGestor


@pytest.fixture
def gestor():
    return TemaAmbientalTagGestor()


def test_crud_tema_ambiental_tag(gestor):
    # Crear dependencias si no existen
    from GeobizIA.controlador.crud.crud_tema_ambiental import CrudTemaAmbiental
    from GeobizIA.controlador.crud.crud_tag import CrudTag
    from GeobizIA.controlador.crud.crud_tema_ambiental_tag import CrudTemaAmbientalTag
    from GeobizIA.controlador.dominios.tema_ambiental import Tema_Ambiental
    from GeobizIA.controlador.dominios.tag import Tag

    crud_tema = CrudTemaAmbiental()
    crud_tag = CrudTag()
    crud_rel = CrudTemaAmbientalTag()

    id_tema_ambiental = 1
    id_tag = 10

    # Crear tema_ambiental si no existe
    if not crud_tema.select_by_id(id_tema_ambiental, Tema_Ambiental):
        crud_tema.insert({
            "id_tema_ambiental": id_tema_ambiental,
            "nombre": "Prueba",
            "descripcion": "desc",
            "relevancia": "Alta"
        }, Tema_Ambiental)
    # Crear tag si no existe
    if not crud_tag.select_by_id(id_tag, Tag):
        crud_tag.insert({
            "id_tag": id_tag,
            "palabra_clave": "clave",
            "categoria": "cat",
            "frecuencia_uso": 1
        }, Tag)
    # Eliminar relación si ya existe (para que el test sea idempotente)
    if crud_rel.buscar(id_tema_ambiental, id_tag):
        crud_rel.eliminar(id_tema_ambiental, id_tag)

    # Crear relación
    relacion = gestor.agregar(id_tema_ambiental, id_tag)
    assert relacion is not None

    # Buscar relación
    encontrada = gestor.buscar(id_tema_ambiental, id_tag)
    assert encontrada is not None

    # Eliminar relación
    eliminado = gestor.eliminar(id_tema_ambiental, id_tag)
    assert eliminado
    assert gestor.buscar(id_tema_ambiental, id_tag) is None
    print(f"Eliminada relación: {eliminado}")

if __name__ == "__main__":
    test_crud_tema_ambiental_tag()
