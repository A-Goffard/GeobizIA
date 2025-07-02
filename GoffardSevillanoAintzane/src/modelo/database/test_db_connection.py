import sys
import os

# Añade la raíz del proyecto al sys.path para que los imports absolutos funcionen
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pyodbc
from src.modelo.database.db_conexion import get_connection, close_connection

def test_connection():
    """
    Prueba la conexión a la base de datos ejecutando varias consultas.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Prueba 1: Obtener la versión de SQL Server
        print("\nPrueba 1: Obteniendo la versión de SQL Server...")
        cursor.execute("SELECT @@VERSION")
        version = cursor.fetchone()[0]
        print(f"Versión de SQL Server: {version}")

        # Prueba 2: Listar las tablas de la base de datos
        print("\nPrueba 2: Listando las tablas de la base de datos...")
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        tables = cursor.fetchall()
        print("Tablas en la base de datos:")
        for table in tables:
            print(f"- {table[0]}")

        # Prueba 3: Consultar datos de la tabla 'rol'
        print("\nPrueba 3: Consultando datos de la tabla 'rol'...")
        cursor.execute("SELECT * FROM rol")
        rows = cursor.fetchall()
        if rows:
            print("Registros en la tabla 'rol':")
            for row in rows:
                print(f"ID: {row.id_rol}, Nombre: {row.nombre}, Descripción: {row.descripcion}")
        else:
            print("No hay registros en la tabla 'rol'.")

        # Prueba 4: Insertar un registro de prueba en 'rol' (si no existe)
        print("\nPrueba 4: Insertando un registro de prueba en 'rol'...")
        cursor.execute("""
            IF NOT EXISTS (SELECT 1 FROM rol WHERE id_rol = 999)
            INSERT INTO rol (id_rol, nombre, descripcion) VALUES (999, 'TestRol', 'Rol de prueba')
        """)
        conn.commit()
        print("Registro de prueba insertado (o ya existía).")

        # Prueba 5: Verificar el registro insertado
        print("\nPrueba 5: Verificando el registro insertado en 'rol'...")
        cursor.execute("SELECT * FROM rol WHERE id_rol = 999")
        row = cursor.fetchone()
        if row:
            print(f"Registro encontrado: ID: {row.id_rol}, Nombre: {row.nombre}, Descripción: {row.descripcion}")
        else:
            print("No se encontró el registro de prueba.")

    except pyodbc.Error as e:
        print(f"Error al ejecutar las pruebas: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        close_connection(conn, cursor)

if __name__ == "__main__":
    test_connection()
