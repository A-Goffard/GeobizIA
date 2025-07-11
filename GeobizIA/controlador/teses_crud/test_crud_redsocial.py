import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.redes_sociales import RedesSociales

@pytest.fixture
def gestor():
    return RedesSociales()

def test_crud_redsocial(gestor):
    # Crear red social
    red = gestor.agregar(
        id_red_social=4,
        plataforma="Instagram",
        nombre_cuenta="@eco_ambiental",
        preferencias_publicacion="",
        estado_conexion="Activa",
        ultima_publicacion="2025-06-04",
        credenciales=""
    )
    assert red is not None
    print(f"Red social creada: {red}")

    red_leida = gestor.buscar(4)
    assert red_leida.nombre_cuenta == "@eco_ambiental"
    print(f"Red social leída: {red_leida}")

    # Actualizar red social
    actualizado = gestor.actualizar(4, nombre_cuenta="@eco_actualizada", estado_conexion="En revisión")
    assert actualizado
    assert gestor.buscar(4).nombre_cuenta == "@eco_actualizada"
    assert gestor.buscar(4).estado_conexion == "En revisión"
    print(f"Red social actualizada: {actualizado}")
    red_leida = gestor.buscar(4)
    print(f"Red social después de actualizar: {red_leida}")

    # Eliminar red social
    eliminado = gestor.eliminar(4)
    assert eliminado
    assert gestor.buscar(4) is None
    print(f"Red social eliminada: {eliminado}")
    red_leida = gestor.buscar(4)
    print(f"Red social después de eliminar: {red_leida}")
