import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.plantilla_tipo_publicaciones import PlantillaTipoPublicacionGestor
from src.controlador.gestores.plantillas import Plantillas
from src.controlador.gestores.tipos_publicacion import Tipos_Publicacion

@pytest.fixture
def gestor():
    # Limpieza previa para evitar conflictos de claves primarias y foráneas
    gestor_plantillas = Plantillas()
    gestor_relaciones = PlantillaTipoPublicacionGestor()
    gestor_tipo_publicaciones = Tipos_Publicacion()
    # Elimina relaciones si existen
    gestor_relaciones.eliminar(1, 2)
    gestor_relaciones.eliminar(3, 4)
    # Asegura que existan las plantillas necesarias para las pruebas
    if gestor_plantillas.buscar(1) is None:
        gestor_plantillas.agregar(
            id_plantilla=1,
            titulo="Plantilla Test 1",
            tipo="Tipo 1",
            contenido_base="Contenido base 1",
            fecha_creacion="2024-06-27",
            ultima_modificacion="2024-06-27"
        )
    if gestor_plantillas.buscar(3) is None:
        gestor_plantillas.agregar(
            id_plantilla=3,
            titulo="Plantilla Test 3",
            tipo="Tipo 3",
            contenido_base="Contenido base 3",
            fecha_creacion="2024-06-27",
            ultima_modificacion="2024-06-27"
        )
    # Asegura que existan los tipos de publicación necesarios para las pruebas
    if gestor_tipo_publicaciones.buscar(2) is None:
        gestor_tipo_publicaciones.agregar(
            id_tipo_publicacion=2,
            nombre="Tipo Publicación 2",
            descripcion="Descripción tipo publicación 2"
        )
    if gestor_tipo_publicaciones.buscar(4) is None:
        gestor_tipo_publicaciones.agregar(
            id_tipo_publicacion=4,
            nombre="Tipo Publicación 4",
            descripcion="Descripción tipo publicación 4"
        )
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
