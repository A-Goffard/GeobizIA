import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.proyectos import Proyectos

@pytest.fixture
def gestor():
    gestor = Proyectos()
    # Elimina el proyecto con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

def test_crud_proyecto(gestor):
    # Crear un proyecto
    proyecto = gestor.agregar(
        id_proyecto=1,
        nombre="Proyecto de Consultoría",
        descripcion="Consultoría para optimización de procesos",
        fecha_inicio="2025-07-01",
        fecha_fin="2025-12-31",
        poblacion="Madrid",
        responsable="Juan Pérez",
        estado="Activo",
        objetivos="Mejorar eficiencia operativa",
        presupuesto=50000.0
    )
    assert proyecto is not None

    # Leer el proyecto
    proyecto_leido = gestor.buscar(1)
    assert proyecto_leido.nombre == "Proyecto de Consultoría"

    # Actualizar el proyecto
    actualizado = gestor.actualizar(1, nombre="Proyecto de Consultoría Actualizado", presupuesto=60000.0)
    assert actualizado
    assert gestor.buscar(1).nombre == "Proyecto de Consultoría Actualizado"
    assert gestor.buscar(1).presupuesto == 60000.0

    # Eliminar el proyecto
    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None