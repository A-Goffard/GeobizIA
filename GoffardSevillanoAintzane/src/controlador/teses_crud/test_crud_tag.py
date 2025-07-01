import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.tags import Tags

@pytest.fixture
def gestor():
    return Tags()

def test_crud_tag(gestor):
    # Crear un tag
    tag = gestor.agregar(id_tag=3, palabra_clave="sostenibilidad", categoria="ambiental", frecuencia_uso=5)
    print(f"Tag creado: {tag}")

    assert tag is not None, "Error: No se pudo crear el tag. Finalizando la prueba."

    # Leer el tag
    tag_leido = gestor.buscar(3)
    assert tag_leido.palabra_clave == "sostenibilidad", "La palabra clave no coincide."

    # Actualizar el tag
    actualizado = gestor.actualizar(3, palabra_clave="eco", frecuencia_uso=30)
    assert actualizado, "Error al actualizar el tag."
    assert gestor.buscar(3).palabra_clave == "eco", "La palabra clave no se actualizó correctamente."
    assert gestor.buscar(3).frecuencia_uso == 30, "La frecuencia de uso no se actualizó correctamente."

    # Eliminar el tag
    eliminado = gestor.eliminar(3)
    assert eliminado, "Error al eliminar el tag."
    assert gestor.buscar(3) is None, "El tag no se eliminó correctamente."

if __name__ == "__main__":
    pytest.main()
