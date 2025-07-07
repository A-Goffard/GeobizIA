import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.tipo_publicacion_redsocial import TipoPublicacionRedSocialGestor

@pytest.fixture
def gestor():
    return TipoPublicacionRedSocialGestor()

def test_crud_tipo_publicacion_redsocial(gestor):
    # Asegúrate de que existen los registros referenciados antes de insertar la relación
    from GeobizIA.controlador.crud.crud_tipo_publicacion import CrudTipoPublicacion
    from GeobizIA.controlador.crud.crud_redsocial import CrudRedSocial
    from GeobizIA.controlador.dominios.tipo_publicacion import Tipo_Publicacion
    from GeobizIA.controlador.dominios.redsocial import RedSocial

    crud_tipo = CrudTipoPublicacion()
    crud_red = CrudRedSocial()

    id_tipo_publicacion = 6
    id_red_social = 7

    # Crear tipo_publicacion si no existe
    if not crud_tipo.select_by_id(id_tipo_publicacion, Tipo_Publicacion):
        crud_tipo.insert({'id_tipo_publicacion': id_tipo_publicacion, 'nombre': 'Prueba'}, Tipo_Publicacion)
    # Crear red_social si no existe
    if not crud_red.select_by_id(id_red_social, RedSocial):
        crud_red.insert({
            'id_red_social': id_red_social,
            'plataforma': 'Prueba',
            'nombre_cuenta': 'prueba',
            'credenciales': '',
            'preferencias_publicacion': '',
            'estado_conexion': '',
            'ultima_publicacion': ''
        }, RedSocial)

    agregado = gestor.agregar(id_tipo_publicacion, id_red_social)
    assert agregado is not None

    encontrado = gestor.buscar(id_tipo_publicacion, id_red_social)
    assert encontrado is not None
    assert encontrado.id_tipo_publicacion == id_tipo_publicacion
    assert encontrado.id_red_social == id_red_social

    eliminado = gestor.eliminar(id_tipo_publicacion, id_red_social)
    assert eliminado
    assert gestor.buscar(id_tipo_publicacion, id_red_social) is None