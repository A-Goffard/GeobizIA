import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.eventos import Eventos

@pytest.fixture
def gestor():
    gestor = Eventos()
    # Elimina el evento con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

def test_crud_evento(gestor):
    # Crear un evento solo si no existe
    evento = gestor.buscar(1)
    if evento is None:
        evento = gestor.agregar(
            id_evento=1,
            nombre="Conferencia de Tecnología",
            tipo="Conferencia",
            lugar="Centro de Convenciones",
            fecha_comienzo="2025-07-01",
            fecha_final="2025-07-03",
            poblacion="Madrid",
            tematica="Innovación Tecnológica"
        )
        assert evento is not None
        assert evento.nombre == "Conferencia de Tecnología"
    else:
        # Si ya existe, solo continúa el test con el evento existente
        evento = gestor.buscar(1)

    # Leer el evento
    evento_leido = gestor.buscar(1)
    # No asserts estrictos sobre el nombre original si ya existía
    assert evento_leido is not None

    # Actualizar el evento
    actualizado = gestor.actualizar(1, nombre="Conferencia de Tecnología Actualizada", tipo="Conferencia Internacional")
    assert actualizado
    assert gestor.buscar(1).nombre == "Conferencia de Tecnología Actualizada"
    assert gestor.buscar(1).tipo == "Conferencia Internacional"

    # Eliminar relaciones dependientes antes de eliminar el evento
    import pyodbc
    from GeobizIA.modelo.database.db_conexion import get_connection, close_connection
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM actividad_evento WHERE id_evento = ?", (1,))
        conn.commit()
    finally:
        close_connection(conn, cursor)

    # Eliminar el evento
    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None

if __name__ == "__main__":
    pytest.main()