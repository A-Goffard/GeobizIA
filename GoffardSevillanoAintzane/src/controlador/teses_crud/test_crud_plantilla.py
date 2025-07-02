import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.plantillas import Plantillas

@pytest.fixture
def gestor():
    return Plantillas()

def test_crud_plantilla(gestor):

    # Crear una plantilla
    plantilla = gestor.agregar(
        id_plantilla=8,
        titulo="Plantilla Informe",
        tipo="Informe",
        contenido_base="Este es el contenido base del informe",
        fecha_creacion="2025-06-27",
        ultima_modificacion="2025-06-27"
    )
    assert plantilla is not None

    # Leer la plantilla
    plantilla_leida = gestor.buscar(8)
    assert plantilla_leida.titulo == "Plantilla Informe"

    # Actualizar la plantilla
    actualizado = gestor.actualizar(8, titulo="Plantilla Informe Actualizado", tipo="Informe Técnico")
    assert actualizado
    assert gestor.buscar(8).titulo == "Plantilla Informe Actualizado"

    # Eliminar la plantilla
    eliminado = gestor.eliminar(8)
    assert eliminado
    assert gestor.buscar(8) is None