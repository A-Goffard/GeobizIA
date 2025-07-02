import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.logs_sistema import LogsSistema
from src.controlador.gestores.usuarios import Usuarios
from src.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    return LogsSistema()

@pytest.fixture
def gestor_usuarios():
    return Usuarios()

@pytest.fixture
def gestor_personas():
    gestor = Personas()
    # Elimina la persona con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor


def test_crud_log_sistema(gestor, gestor_usuarios, gestor_personas):
    persona = gestor_personas.agregar(
        id_persona=17,
        nombre="Marta",
        apellido="Rodríguez",
        email="marta.rodriguez@example.com",
        telefono="912345678",
        dni="12345678E",
        direccion="Calle Sol 456",
        cp="28005",
        poblacion="Madrid",
        pais="España"
    )
    assert persona is not None

    usuario = gestor_usuarios.agregar(
        id_usuario=17,
        id_persona=17,
        fecha_nacimiento="1990-05-20",
        rol="Editor",
        preferencias="Notificaciones por email",
        password="password456"
    )
    assert usuario is not None

    log_sistema = gestor.agregar(
        id_log_sistema=17,
        usuario_id=17,
        fecha="2025-06-27 13:22:00",
        accion="Inicio de sesión",
        descripcion="El usuario inició sesión en el sistema",
        nivel="INFO"
    )
    assert log_sistema is not None

    log_sistema_leido = gestor.buscar(17)
    assert log_sistema_leido.accion == "Inicio de sesión"

    actualizado = gestor.actualizar(17, accion="Actualización de perfil")
    assert actualizado
    assert gestor.buscar(17).accion == "Actualización de perfil"

    eliminado = gestor.eliminar(17)
    assert eliminado
    assert gestor.buscar(17) is None

    gestor_usuarios.eliminar(17)
    gestor_personas.eliminar(17)