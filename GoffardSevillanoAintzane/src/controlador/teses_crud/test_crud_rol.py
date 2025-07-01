import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.roles import Roles

@pytest.fixture
def gestor():
    return Roles()

def test_crud_rol(gestor):
    rol = gestor.agregar(id_rol=4, nombre="Admin", descripcion="Rol administrativo")
    assert rol is not None

    rol_leido = gestor.buscar(4)
    assert rol_leido.nombre == "Admin"

    actualizado = gestor.actualizar(4, nombre="SuperAdmin")
    assert actualizado
    assert gestor.buscar(4).nombre == "SuperAdmin"

    eliminado = gestor.eliminar(4)
    assert eliminado
    assert gestor.buscar(4) is None
