import pytest
from src.controlador.gestores.publicaciones import Publicaciones
from src.controlador.gestores.usuarios import Usuarios
from src.controlador.gestores.personas import Personas
from src.controlador.gestores.generadoresia import GeneradoresIA
from src.controlador.gestores.tipos_publicacion import Tipos_Publicacion

@pytest.fixture
def gestor():
    return Publicaciones()

@pytest.fixture
def gestor_usuarios():
    return Usuarios()

@pytest.fixture
def gestor_personas():
    return Personas()

@pytest.fixture
def gestor_generadores():
    return GeneradoresIA()

@pytest.fixture
def gestor_tipos():
    return Tipos_Publicacion()

def test_crud_publicacion(gestor, gestor_usuarios, gestor_personas, gestor_generadores, gestor_tipos):
    persona = gestor_personas.agregar(
        id_persona=1,
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
        id_usuario=1,
        id_persona=1,
        fecha_nacimiento="1990-05-20",
        rol="Editor",
        preferencias="Notificaciones por email",
        password="password456"
    )
    assert usuario is not None

    generador = gestor_generadores.agregar(
        id_generador_ia=1,
        nombre="Generador de Texto",
        descripcion="Generador de texto basado en IA",
        empresa_id=None,
        configuraciones=None,
        ejemplos_estilo=None,
        ultima_generacion=None
    )
    assert generador is not None

    tipo_publicacion = gestor_tipos.agregar(
        id_tipo_publicacion=1,
        nombre="Artículo",
        descripcion="Publicación de tipo artículo"
    )
    assert tipo_publicacion is not None

    publicacion = gestor.agregar(
        id_publicacion=1,
        titulo="Título de prueba",
        contenido="Este es un artículo generado por IA",
        autor="Marta",
        fecha_creacion="2025-06-27",
        estado="borrador",
        tags="",
        palabras_clave="",
        generada_por_ia=True,
        id_generador_ia=1,
        feedback_empresa="",
        id_tipo_publicacion=1,
        id_plantilla=None
    )
    assert publicacion is not None

    publicacion_leida = gestor.buscar(1)
    assert publicacion_leida is not None

    actualizado = gestor.actualizar(1, contenido="Este es un artículo actualizado generado por IA")
    assert actualizado
    assert gestor.buscar(1).contenido == "Este es un artículo actualizado generado por IA"

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

    gestor_tipos.eliminar(1)
    gestor_generadores.eliminar(1)
    gestor_usuarios.eliminar(1)
    gestor_personas.eliminar(1)