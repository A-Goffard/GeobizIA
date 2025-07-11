import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.actividades import Actividades
from GeobizIA.controlador.dominios.actividad import Actividad

@pytest.fixture
def gestor():
    gestor = Actividades()
    # Elimina la actividad con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

def test_crud_actividad(gestor):
    # Crear una actividad solo si no existe
    actividad = gestor.buscar(1)
    if actividad is None:
        actividad = Actividad(
            id_actividad=1,
            tipo="Conferencia",
            nombre="Evento Anual",
            descripcion="Evento de tecnología",
            responsable="Juan Pérez",
            duracion="2 horas",
            coste_economico=1000.0,
            coste_horas=20.0,
            facturacion=1500.0,
            resultados="Éxito",
            valoracion="Positiva",
            observaciones="Ninguna"
        )
        actividad = gestor.agregar(actividad)
    assert actividad is not None

    # Leer la actividad
    actividad_leida = gestor.buscar(1)
    assert actividad_leida is not None

    # Actualizar la actividad
    actividad_leida.nombre = "Taller de Innovación"
    actividad_leida.tipo = "Taller"
    actividad_leida.descripcion = "Taller práctico"
    actividad_leida.responsable = "María López"
    actividad_leida.duracion = "3 horas"
    actividad_leida.coste_economico = 1200.0
    actividad_leida.coste_horas = 25.0
    actividad_leida.facturacion = 1800.0
    actividad_leida.resultados = "Muy exitoso"
    actividad_leida.valoracion = "Excelente"
    actividad_leida.observaciones = "Buena participación"
    actualizado = gestor.actualizar(actividad_leida)
    assert actualizado
    assert gestor.buscar(1).nombre == "Taller de Innovación"

    # Eliminar la actividad
    import pyodbc
    from GeobizIA.modelo.database.db_conexion import get_connection, close_connection
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Elimina primero todas las relaciones hijas
        cursor.execute("DELETE FROM participante WHERE actividad_id = ?", (1,))
        cursor.execute("DELETE FROM actividad_fecha WHERE id_actividad = ?", (1,))
        cursor.execute("DELETE FROM proyecto_actividad WHERE id_actividad = ?", (1,))
        cursor.execute("DELETE FROM actividad_evento WHERE id_actividad = ?", (1,))
        conn.commit()
    finally:
        close_connection(conn, cursor)

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

if __name__ == "__main__":
    # Ejecuta el test con pytest, no lo llames directamente
    import pytest
    pytest.main([__file__])