import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.documentos import Documentos

@pytest.fixture
def gestor():
    gestor = Documentos()
    # Elimina primero los tags relacionados antes de eliminar el documento
    import pyodbc
    from src.modelo.database.db_conexion import get_connection, close_connection
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM documento_tag WHERE id_documento = ?", (1,))
        conn.commit()
    finally:
        close_connection(conn, cursor)
    gestor.eliminar(1)
    return gestor

def test_crud_documento(gestor):
    # Crear un documento solo si no existe
    documento = gestor.buscar(1)
    if documento is None:
        documento = gestor.agregar(
            id_documento=1,
            titulo="Informe Anual",
            descripcion="Informe anual de actividades 2025",
            fecha_subida="2025-06-27",
            tipo="Informe",
            tematica="Gestión Empresarial"
        )
    assert documento is not None

    # Leer el documento
    documento_leido = gestor.buscar(1)
    assert documento_leido.titulo == "Informe Anual"

    # Actualizar el documento
    actualizado = gestor.actualizar(1, titulo="Informe Anual Actualizado", tipo="Informe Técnico")
    assert actualizado
    assert gestor.buscar(1).titulo == "Informe Anual Actualizado"

    # Eliminar el documento
    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None