import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.auditorias_publicacion import Auditorias_Publicacion
from src.controlador.gestores.publicaciones import Publicaciones
from src.controlador.gestores.generadoresia import GeneradoresIA
from src.controlador.gestores.usuarios import Usuarios
from src.controlador.gestores.personas import Personas
from src.controlador.gestores.tipos_publicacion import Tipos_Publicacion
from src.controlador.gestores.plantillas import Plantillas

@pytest.fixture
def gestor():
    gestor = Auditorias_Publicacion()
    # Elimina la auditoría con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

@pytest.fixture
def gestor_publicaciones():
    gestor = Publicaciones()
    # Elimina la publicación con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

@pytest.fixture
def gestor_generadores():
    gestor = GeneradoresIA()
    # Elimina el generador con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

@pytest.fixture
def gestor_usuarios():
    gestor = Usuarios()
    # Elimina el usuario con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

@pytest.fixture
def gestor_personas():
    gestor = Personas()
    # Elimina la persona con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

@pytest.fixture
def gestor_tipos():
    gestor = Tipos_Publicacion()
    # Elimina el tipo de publicación con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

@pytest.fixture
def gestor_plantillas():
    gestor = Plantillas()
    # Elimina la plantilla con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

def test_crud_auditoria_publicacion(
    gestor, gestor_publicaciones, gestor_generadores, gestor_usuarios, gestor_personas, gestor_tipos, gestor_plantillas
):
    persona = gestor_personas.buscar(1)
    if persona is None:
        persona = gestor_personas.agregar(
            id_persona=1,
            nombre="Laura",
            apellido="Martínez",
            email="laura.martinez@example.com",
            telefono="912345678",
            dni="12345678G",
            direccion="Calle Estrella 123",
            cp="28004",
            poblacion="Madrid",
            pais="España"
        )
    assert persona is not None

    usuario = gestor_usuarios.buscar(1)
    if usuario is None:
        usuario = gestor_usuarios.agregar(
            id_usuario=1,
            id_persona=1,
            fecha_nacimiento="1985-03-15",
            rol="Administrador",
            preferencias="Notificaciones por email",
            password="password789"
        )
    assert usuario is not None

    generador = gestor_generadores.agregar(
        id_generador_ia=1,
        nombre="Grok",
        descripcion="Generador de texto avanzado",
        empresa_id=None,
        configuraciones=None,
        ejemplos_estilo=None,
        ultima_generacion=None
    )
    assert generador is not None

    tipo_publicacion = gestor_tipos.buscar(1)
    if tipo_publicacion is None:
        tipo_publicacion = gestor_tipos.agregar(
            id_tipo_publicacion=1,
            nombre="Artículo",
            descripcion="Publicación de tipo artículo"
        )
    assert tipo_publicacion is not None

    plantilla = gestor_plantillas.buscar(1)
    if plantilla is None:
        plantilla = gestor_plantillas.agregar(
            id_plantilla=1,
            titulo="Plantilla Artículo",
            tipo="Artículo",
            contenido_base="Contenido de ejemplo para artículos",
            fecha_creacion="2025-06-27",
            ultima_modificacion="2025-06-27"
        )
    assert plantilla is not None

    publicacion = gestor_publicaciones.agregar(
        id_publicacion=1,
        titulo="Publicación de prueba",
        contenido="Contenido de la publicación de prueba",
        autor="Laura",
        fecha_creacion="2025-06-27",
        estado="Publicado",
        tags="",
        palabras_clave="",
        generada_por_ia=True,
        id_generador_ia=1,
        feedback_empresa="",
        id_tipo_publicacion=1,
        id_plantilla=1
    )
    assert publicacion is not None

    auditoria = gestor.agregar(
        id_auditoria_publicacion=1,
        publicacion_id=1,
        generador_ia_id=1,
        fecha_generacion="2025-06-27 15:30:00",
        usuario_id=1,
        parametros_entrada="{}",
        resultado="OK",
        observaciones="Creación de publicación"
    )
    assert auditoria is not None

    auditoria_leida = gestor.buscar(1)
    assert auditoria_leida is not None

    actualizado = gestor.actualizar(1, resultado="EDITADO", observaciones="Edición de publicación")
    assert actualizado
    assert gestor.buscar(1).resultado == "EDITADO"

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

    gestor_publicaciones.eliminar(1)
    gestor_plantillas.eliminar(1)
    gestor_tipos.eliminar(1)
    gestor_generadores.eliminar(1)
    gestor_usuarios.eliminar(1)
    gestor_personas.eliminar(1)