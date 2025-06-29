import pytest
from src.controlador.gestores.redes_sociales import RedesSociales

@pytest.fixture
def gestor():
    return RedesSociales()

def test_crud_redsocial(gestor):
    # Crear red social
    red = gestor.agregar(
        id_red_social=1,
        plataforma="Instagram",
        nombre_cuenta="@eco_ambiental",
        preferencias_publicacion="",
        estado_conexion="Activa",
        ultima_publicacion="2025-06-01",
        credenciales=""
    )
    assert red is not None
    print(f"Red social creada: {red}")

    red_leida = gestor.buscar(1)
    assert red_leida.nombre_cuenta == "@eco_ambiental"
    print(f"Red social leída: {red_leida}")

    # Actualizar red social
    actualizado = gestor.actualizar(1, nombre_cuenta="@eco_actualizada", estado_conexion="En revisión")
    assert actualizado
    assert gestor.buscar(1).nombre_cuenta == "@eco_actualizada"
    assert gestor.buscar(1).estado_conexion == "En revisión"
    print(f"Red social actualizada: {actualizado}")
    red_leida = gestor.buscar(1)
    print(f"Red social después de actualizar: {red_leida}")

    # Eliminar red social
    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None
    print(f"Red social eliminada: {eliminado}")
    red_leida = gestor.buscar(1)
    print(f"Red social después de eliminar: {red_leida}")
