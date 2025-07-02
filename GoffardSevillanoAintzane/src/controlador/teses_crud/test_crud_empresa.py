import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.controlador.gestores.empresas import Empresas

@pytest.fixture
def gestor():
    gestor = Empresas()
    # Elimina la empresa con id=1 si existe para evitar conflictos de clave primaria
    gestor.eliminar(1)
    return gestor

def test_crud_empresa(gestor):
    empresa = gestor.buscar(1)
    if empresa is None:
        empresa = gestor.agregar(
            id_empresa=1,
            nombre="Innovatech S.A.",
            sector="Tecnología",
            logo="logo.png",
            ubicacion="Valencia"
        )
        assert empresa is not None
        assert empresa.nombre == "Innovatech S.A."
    else:
        # Si ya existe, solo continúa el test con la empresa existente
        empresa = gestor.buscar(1)

    empresa_leida = gestor.buscar(1)
    assert empresa_leida is not None

    actualizado = gestor.actualizar(1, nombre="Innovatech Solutions S.A.", sector="Innovación")
    assert actualizado
    assert gestor.buscar(1).nombre == "Innovatech Solutions S.A."
    assert gestor.buscar(1).sector == "Innovación"

    # Eliminar relaciones dependientes antes de eliminar la empresa
    import pyodbc
    from src.modelo.database.db_conexion import get_connection, close_connection
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Elimina primero las programaciones de publicaciones asociadas a la empresa
        cursor.execute("""
            DELETE FROM programacion
            WHERE publicacion_id IN (
                SELECT id_publicacion FROM publicacion
                WHERE id_generador_ia IN (
                    SELECT id_generador_ia FROM generadoria WHERE empresa_id = ?
                )
            )
        """, (1,))
        # Luego elimina las auditorías de publicaciones asociadas a la empresa
        cursor.execute("""
            DELETE FROM auditoria_publicacion
            WHERE publicacion_id IN (
                SELECT id_publicacion FROM publicacion
                WHERE id_generador_ia IN (
                    SELECT id_generador_ia FROM generadoria WHERE empresa_id = ?
                )
            )
        """, (1,))
        # Luego elimina los tags de publicaciones asociadas a la empresa
        cursor.execute("""
            DELETE FROM publicacion_tag
            WHERE id_publicacion IN (
                SELECT id_publicacion FROM publicacion
                WHERE id_generador_ia IN (
                    SELECT id_generador_ia FROM generadoria WHERE empresa_id = ?
                )
            )
        """, (1,))
        # Luego elimina las publicaciones
        cursor.execute("""
            DELETE FROM publicacion
            WHERE id_generador_ia IN (
                SELECT id_generador_ia FROM generadoria WHERE empresa_id = ?
            )
        """, (1,))
        # Luego elimina los generadores
        cursor.execute("DELETE FROM generadoria WHERE empresa_id = ?", (1,))
        conn.commit()
    finally:
        close_connection(conn, cursor)

    eliminado = gestor.eliminar(1)
    assert eliminado
    assert gestor.buscar(1) is None