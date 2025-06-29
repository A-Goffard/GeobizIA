import pytest
from src.controlador.gestores.auditorias_publicacion import Auditorias_Publicacion
from src.controlador.gestores.publicaciones import Publicaciones
from src.controlador.gestores.generadoresia import GeneradoresIA
from src.controlador.gestores.usuarios import Usuarios
from src.controlador.gestores.personas import Personas
from src.controlador.gestores.tipos_publicacion import Tipos_Publicacion
from src.controlador.gestores.plantillas import Plantillas

@pytest.fixture
def gestor():
    return Auditorias_Publicacion()

@pytest.fixture
def gestor_publicaciones():
    return Publicaciones()

@pytest.fixture
def gestor_generadores():
    return GeneradoresIA()

@pytest.fixture
def gestor_usuarios():
    return Usuarios()

@pytest.fixture
def gestor_personas():
    return Personas()

@pytest.fixture
def gestor_tipos():
    return Tipos_Publicacion()

@pytest.fixture
def gestor_plantillas():
    return Plantillas()

def test_crud_auditoria_publicacion(
    gestor, gestor_publicaciones, gestor_generadores, gestor_usuarios, gestor_personas, gestor_tipos, gestor_plantillas
):
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

    tipo_publicacion = gestor_tipos.agregar(
        id_tipo_publicacion=1,
        nombre="Artículo",
        descripcion="Publicación de tipo artículo"
    )
    assert tipo_publicacion is not None

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