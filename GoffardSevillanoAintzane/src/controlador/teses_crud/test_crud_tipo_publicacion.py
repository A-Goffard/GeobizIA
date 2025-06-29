import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.tipos_publicacion import Tipos_Publicacion

@pytest.fixture
def gestor():
    return Tipos_Publicacion()

def test_crud_tipo_publicacion(gestor):
    # Crear un tipo_publicacion
    tipo = gestor.agregar(
        id_tipo_publicacion=1,
        nombre="Artículo",
        descripcion="Publicación de tipo artículo"
    )
    assert tipo is not None

    # Leer el tipo_publicacion
    tipo_leido = gestor.buscar(1)
    assert tipo_leido.nombre == "Artículo"

    # Actualizar el tipo_publicacion
    actualizado = gestor.actualizar(1, nombre="Informe", descripcion="Publicación de tipo informe técnico")
    assert actualizado
    assert gestor.buscar(1).nombre == "Informe"

    # Eliminar el tipo_publicacion
    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

if __name__ == "__main__":
    test_crud_tipo_publicacion()