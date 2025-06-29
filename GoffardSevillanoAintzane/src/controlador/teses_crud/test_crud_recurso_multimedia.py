import pytest
from src.controlador.gestores.recursos_multimedia import RecursosMultimedia

@pytest.fixture
def gestor():
    return RecursosMultimedia()

def test_crud_recurso_multimedia(gestor):
    # Crear
    recurso = gestor.agregar(
        id_recurso_multimedia=1,
        tipo="Imagen",
        titulo="Foto del proyecto",
        fecha_subida="2025-06-27",
        autor="Equipo A"
    )
    assert recurso is not None

    # Leer
    recurso_leido = gestor.buscar(1)
    assert recurso_leido.titulo == "Foto del proyecto"

    # Actualizar
    actualizado = gestor.actualizar(1, titulo="Foto oficial del proyecto")
    assert actualizado
    assert gestor.buscar(1).titulo == "Foto oficial del proyecto"

    # Eliminar
    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None
    eliminado = eliminar_recurso_multimedia(recurso.id_recurso_multimedia)
    print(f"Recurso eliminado: {eliminado}")
    recurso_leido = leer_recurso_multimedia(recurso.id_recurso_multimedia)
    print(f"Recurso después de eliminar: {recurso_leido}")

if __name__ == "__main__":
    test_crud_recurso_multimedia()
