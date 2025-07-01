import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

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
        id_persona=9,
        nombre="Marta",
        apellido="Rodríguez",
        email="marta.rodriguez@example.com",
        telefono="992395678",
        dni="92395678E",
        direccion="Calle Sol 956",
        cp="28005",
        poblacion="Madrid",
        pais="España"
    )
    assert persona is not None

    usuario = gestor_usuarios.agregar(
        id_usuario=9,
        id_persona=9,
        fecha_nacimiento="9990-05-20",
        rol="Editor",
        preferencias="Notificaciones por email",
        password="password956"
    )
    assert usuario is not None

    generador = gestor_generadores.agregar(
        id_generador_IA=9,
        id_usuario=None,
        nombre="Generador de Texto",
        descripcion="Generador de texto basado en IA",
        tipo=None
    )
    assert generador is not None

    tipo_publicacion = gestor_tipos.agregar(
        id_tipo_publicacion=9,
        nombre="Artículo",
        descripcion="Publicación de tipo artículo"
    )
    assert tipo_publicacion is not None

    publicacion = gestor.agregar(
        id_publicacion=9,
        titulo="Título de prueba",
        contenido="Este es un artículo generado por IA",
        autor="Marta",
        fecha_creacion="2025-06-27",
        estado="borrador",
        tags="",
        palabras_clave="",
        generada_por_ia=True,
        id_generador_ia=9,
        feedback_empresa="",
        id_tipo_publicacion=9,
        id_plantilla=None
    )
    assert publicacion is not None

    publicacion_leida = gestor.buscar(9)
    assert publicacion_leida is not None

    actualizado = gestor.actualizar(9, contenido="Este es un artículo actualizado generado por IA")
    assert actualizado
    assert gestor.buscar(9).contenido == "Este es un artículo actualizado generado por IA"

    eliminado = gestor.eliminar(9)
    assert eliminado
    assert gestor.buscar(9) is None

    gestor_tipos.eliminar(9)
    gestor_generadores.eliminar(9)
    gestor_usuarios.eliminar(9)
    gestor_personas.eliminar(9)