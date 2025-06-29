import pytest
from src.controlador.gestores.generadoresia import GeneradoresIA
from src.controlador.gestores.usuarios import Usuarios
from src.controlador.gestores.personas import Personas

@pytest.fixture
def gestor():
    return GeneradoresIA()

@pytest.fixture
def gestor_usuarios():
    return Usuarios()

@pytest.fixture
def gestor_personas():
    return Personas()

def test_crud_generador_ia(gestor, gestor_usuarios, gestor_personas):
    persona = gestor_personas.agregar(
        id_persona=1,
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
        id_usuario=1,
        id_persona=1,
        fecha_nacimiento="1995-03-15",
        rol="Analista",
        preferencias="Notificaciones por email",
        password="password123"
    )
    assert usuario is not None

    generador = gestor.agregar(
        id_generador_ia=1,
        nombre="Generador de Texto",
        descripcion="Generador de texto basado en IA",
        empresa_id=None,
        configuraciones=None,
        ejemplos_estilo=None,
        ultima_generacion=None
    )
    assert generador is not None

    generador_leido = gestor.buscar(1)
    assert generador_leido.nombre == "Generador de Texto"

    actualizado = gestor.actualizar(1, nombre="Generador de Imágenes", descripcion="Generador de imágenes basado en IA")
    assert actualizado
    assert gestor.buscar(1).nombre == "Generador de Imágenes"

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

    gestor_usuarios.eliminar(1)
    gestor_personas.eliminar(1)