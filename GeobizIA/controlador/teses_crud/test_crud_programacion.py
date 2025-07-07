import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.programaciones import Programaciones
from GeobizIA.controlador.gestores.publicaciones import Publicaciones
from GeobizIA.controlador.gestores.redes_sociales import RedesSociales

@pytest.fixture
def gestor():
    return Programaciones()

def test_crud_programacion(gestor):
    # Reset de datos previos para evitar conflictos de claves foráneas y duplicados
    gestor_programaciones = Programaciones()
    gestor_publicaciones = Publicaciones()
    gestor_redes = RedesSociales()

    # Eliminar programación, publicación y red social con id=3 si existen (en orden inverso de dependencias)
    gestor_programaciones.eliminar(3)
    gestor_publicaciones.eliminar(3)
    gestor_redes.eliminar(3)

    # Crear publicación si no existe
    if gestor_publicaciones.buscar(3) is None:
        gestor_publicaciones.agregar(
            id_publicacion=3,
            titulo="Prueba",
            contenido="Contenido de prueba",
            autor="María López",
            fecha_creacion="2025-07-01",
            estado="Borrador",
            tags="",
            palabras_clave="",
            generada_por_ia=0,
            id_generador_ia=None,
            feedback_empresa="",
            id_tipo_publicacion=1,
            id_plantilla=None
        )

    # Crear red social si no existe
    if gestor_redes.buscar(3) is None:
        gestor_redes.agregar(
            id_red_social=3,
            plataforma="Instagram",
            nombre_cuenta="@prueba",
            preferencias_publicacion="",
            estado_conexion="Activa",
            ultima_publicacion="2025-07-01",
            credenciales=""
        )

    # Crear programación
    programacion = gestor.agregar(
        id_programacion=3,
        publicacion_id=3,
        red_social_id=3,
        fecha_programada="2025-07-10",
        estado="Programado",
        notificaciones="",
        responsable="María López"
    )
    assert programacion is not None

    # Leer programación
    programacion_leida = gestor.buscar(3)
    assert programacion_leida is not None

    # Actualizar programación
    actualizado = gestor.actualizar(3, estado="Reprogramado")
    assert actualizado
    assert gestor.buscar(3).estado == "Reprogramado"

    # Eliminar programación
    eliminado = gestor.eliminar(3)
    assert eliminado
    assert gestor.buscar(3) is None
    programacion_eliminada = gestor.buscar(programacion.id_programacion)
    print(f"Programación después de eliminar: {programacion_eliminada}")

if __name__ == "__main__":
    test_crud_programacion()