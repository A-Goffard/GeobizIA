import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.usuarios import Usuarios
from GeobizIA.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    return Usuarios()

@pytest.fixture
def gestor_personas():
    return Personas()

def test_crud_usuario(gestor, gestor_personas):
    persona = gestor_personas.agregar(
        id_persona=8,
        nombre="Juan",
        apellido="Pérez",
        email="juan.perez@example.com",
        telefono="823456789",
        dni="82345678A",
        direccion="Calle Falsa 823",
        cp="28008",
        poblacion="Madrid",
        pais="España"
    )
    assert persona is not None

    usuario = gestor.agregar(
        id_usuario=8,
        id_persona=8,
        fecha_nacimiento="8990-08-08",
        rol="Usuario",
        preferencias="Notificaciones por email",
        password="contraseña823"
    )
    assert usuario is not None

    usuario_leido = gestor.buscar(8)
    assert usuario_leido is not None

    actualizado = gestor.actualizar(
        8,
        fecha_nacimiento="8990-02-02",
        rol="Administrador",
        preferencias="Notificaciones por SMS",
        password="nueva_contraseña456"
    )
    assert actualizado
    usuario_leido = gestor.buscar(8)
    assert usuario_leido.rol == "Administrador"
    assert usuario_leido.preferencias == "Notificaciones por SMS"

    eliminado = gestor.eliminar(8)
    assert eliminado
    assert gestor.buscar(8) is None

    gestor_personas.eliminar(8)