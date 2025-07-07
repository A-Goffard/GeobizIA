import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.recursos_multimedia import RecursosMultimedia

@pytest.fixture
def gestor():
    return RecursosMultimedia()

def test_crud_recurso_multimedia(gestor):
    # Crear
    recurso = gestor.agregar(
        id_recurso_multimedia=4,
        tipo="Imagen",
        titulo="Foto del proyecto",
        fecha_subida="2025-06-27",
        autor="Equipo A"
    )
    assert recurso is not None

    # Leer
    recurso_leido = gestor.buscar(4)
    assert recurso_leido.titulo == "Foto del proyecto"

    # Actualizar
    actualizado = gestor.actualizar(4, titulo="Foto oficial del proyecto")
    assert actualizado
    assert gestor.buscar(4).titulo == "Foto oficial del proyecto"

    # Eliminar
    eliminado = gestor.eliminar(4)
    assert eliminado
    assert gestor.buscar(4) is None
    eliminado = gestor.eliminar(recurso.id_recurso_multimedia)
    print(f"Recurso eliminado: {eliminado}")
    recurso_leido = gestor.buscar(recurso.id_recurso_multimedia)
    print(f"Recurso después de eliminar: {recurso_leido}")

if __name__ == "__main__":
    test_crud_recurso_multimedia()
