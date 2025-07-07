import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.tipos_publicacion import Tipos_Publicacion

@pytest.fixture
def gestor():
    return Tipos_Publicacion()

def test_crud_tipo_publicacion(gestor):
    # Crear un tipo_publicacion
    tipo = gestor.agregar(
        id_tipo_publicacion=3,
        nombre="Artículo"
        # No incluyas 'descripcion' porque la columna no existe en la tabla
    )
    assert tipo is not None

    # Leer el tipo_publicacion
    tipo_leido = gestor.buscar(3)
    assert tipo_leido.nombre == "Artículo"

    # Actualizar el tipo_publicacion
    actualizado = gestor.actualizar(3, nombre="Informe")
    assert actualizado
    assert gestor.buscar(3).nombre == "Informe"

    # Eliminar el tipo_publicacion
    eliminado = gestor.eliminar(3)
    assert eliminado
    assert gestor.buscar(3) is None

if __name__ == "__main__":
    # No llames directamente a la función de test con argumentos de pytest.
    # Usa pytest desde la terminal para ejecutar los tests.
    # Elimina este bloque para evitar el error.
    pass