import pytest
from src.controlador.gestores.usuarios import Usuarios
from src.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    return Usuarios()

@pytest.fixture
def gestor_personas():
    return Personas()

def test_crud_usuario(gestor, gestor_personas):
    persona = gestor_personas.agregar(
        id_persona=1,
        nombre="Juan",
        apellido="Pérez",
        email="juan.perez@example.com",
        telefono="123456789",
        dni="12345678A",
        direccion="Calle Falsa 123",
        cp="28001",
        poblacion="Madrid",
        pais="España"
    )
    assert persona is not None

    usuario = gestor.agregar(
        id_usuario=1,
        id_persona=1,
        fecha_nacimiento="1990-01-01",
        rol="Usuario",
        preferencias="Notificaciones por email",
        password="contraseña123"
    )
    assert usuario is not None

    usuario_leido = gestor.buscar(1)
    assert usuario_leido is not None

    actualizado = gestor.actualizar(
        1,
        fecha_nacimiento="1990-02-02",
        rol="Administrador",
        preferencias="Notificaciones por SMS",
        password="nueva_contraseña456"
    )
    assert actualizado
    usuario_leido = gestor.buscar(1)
    assert usuario_leido.rol == "Administrador"
    assert usuario_leido.preferencias == "Notificaciones por SMS"

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

    gestor_personas.eliminar(1)