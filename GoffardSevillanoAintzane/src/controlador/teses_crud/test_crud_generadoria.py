import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.generadoresia import GeneradoresIA
from src.controlador.gestores.usuarios import Usuarios
from src.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    gestor = GeneradoresIA()
    # Elimina el generador con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

@pytest.fixture
def gestor_usuarios():
    gestor = Usuarios()
    # Elimina el usuario con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

@pytest.fixture
def gestor_personas():
    gestor = Personas()
    # Elimina la persona con id=17 si existe para evitar conflictos de clave primaria
    gestor.eliminar(17)
    return gestor

def test_crud_generador_ia(gestor, gestor_usuarios, gestor_personas):
    persona = gestor_personas.agregar(
        id_persona=17,
        nombre="Laura",
        apellido="Sánchez",
        email="laura.sanchez@example.com",
        telefono="987654321",
        dni="87654321D",
        direccion="Calle Luna 123",
        cp="28004",
        poblacion="Sevilla",
        pais="España"
    )
    assert persona is not None

    usuario = gestor_usuarios.agregar(
        id_usuario=17,
        id_persona=17,
        fecha_nacimiento="1995-03-15",
        rol="Analista",
        preferencias="Notificaciones por email",
        password="password123"
    )
    assert usuario is not None

    generador = gestor.agregar(
        id_generador_ia=17,
        nombre="Generador de Texto",
        descripcion="Generador de texto basado en IA",
        empresa_id=None,
        configuraciones=None,
        ejemplos_estilo=None,
        ultima_generacion=None
    )
    assert generador is not None

    generador_leido = gestor.buscar(17)
    assert generador_leido.nombre == "Generador de Texto"

    actualizado = gestor.actualizar(17, nombre="Generador de Imágenes", descripcion="Generador de imágenes basado en IA")
    assert actualizado
    assert gestor.buscar(17).nombre == "Generador de Imágenes"

    eliminado = gestor.eliminar(17)
    assert eliminado
    assert gestor.buscar(17) is None

    gestor_usuarios.eliminar(17)
    gestor_personas.eliminar(17)