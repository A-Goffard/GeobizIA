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
    gestor = Publicaciones()
    # Elimina la publicación con id=18 si existe para evitar conflictos de clave primaria
    gestor.eliminar(18)
    return gestor

@pytest.fixture
def gestor_usuarios():
    gestor = Usuarios()
    # Elimina el usuario con id=18 si existe para evitar conflictos de clave primaria
    gestor.eliminar(18)
    return gestor

@pytest.fixture
def gestor_personas():
    gestor = Personas()
    # Elimina la persona con id=18 si existe para evitar conflictos de clave primaria
    gestor.eliminar(18)
    return gestor

@pytest.fixture
def gestor_generadores():
    gestor = GeneradoresIA()
    # Elimina el generador con id=18 si existe para evitar conflictos de clave primaria
    gestor.eliminar(18)
    return gestor

@pytest.fixture
def gestor_tipos():
    gestor = Tipos_Publicacion()
    # Elimina el tipo de publicación con id=18 si existe para evitar conflictos de clave primaria
    gestor.eliminar(18)
    return gestor

def test_crud_publicacion(gestor, gestor_usuarios, gestor_personas, gestor_generadores, gestor_tipos):
    # Limpieza previa en orden correcto
    gestor.eliminar(18)
    gestor_generadores.eliminar(18)
    gestor_tipos.eliminar(18)
    gestor_usuarios.eliminar(18)
    gestor_personas.eliminar(18)

    persona = gestor_personas.agregar(
        id_persona=18,
        nombre="Marta",
        apellido="Rodríguez",
        email="marta.rodriguez@example.com",
        telefono="181823185678",
        dni="1823185678E",
        direccion="Calle Sol 1856",
        cp="28005",
        poblacion="Madrid",
        pais="España"
    )
    assert persona is not None

    usuario = gestor_usuarios.agregar(
        id_usuario=18,
        id_persona=18,
        fecha_nacimiento="1818180-05-20",
        rol="Editor",
        preferencias="Notificaciones por email",
        password="password1856"
    )
    assert usuario is not None

    generador = gestor_generadores.agregar(
        id_generador_ia=18,
        nombre="Generador de texto para pruebas",
        descripcion="xxxxx",
        empresa_id=None,
        configuraciones=None,
        ejemplos_estilo=None,
        ultima_generacion=None
    )
    assert generador is not None

    tipo_publicacion = gestor_tipos.agregar(
        id_tipo_publicacion=18,
        nombre="Artículo"
    )
    assert tipo_publicacion is not None

    publicacion = gestor.agregar(
        id_publicacion=18,
        id_generador_ia=18,
        id_tipo_publicacion=18,
        titulo="Artículo de prueba",
        autor="Marta",
        estado="borrador",
        tags="",
        palabras_clave="",
        generada_por_ia=False,
        feedback_empresa="",
        id_plantilla=None,
        contenido="xxxxxxxxxxx",
        fecha_creacion="2025-06-27",
    )
    assert publicacion is not None

    publicacion_leida = gestor.buscar(18)
    assert publicacion_leida is not None

    actualizado = gestor.actualizar(18, contenido="Este es un artículo actualizado generado por IA")
    assert actualizado
    assert gestor.buscar(18).contenido == "Este es un artículo actualizado generado por IA"

    eliminado = gestor.eliminar(18)
    assert eliminado
    assert gestor.buscar(18) is None

    gestor_tipos.eliminar(18)
    gestor_generadores.eliminar(18)
    gestor_usuarios.eliminar(18)
    gestor_personas.eliminar(18)