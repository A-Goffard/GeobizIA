import sys
import os

# Añade la raíz del proyecto al sys.path para que los imports absolutos funcionen
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pyodbc
from src.modelo.database.db_conexion import get_connection, close_connection


conn = get_connection()
cursor = conn.cursor()

sql_path = os.path.join(os.path.dirname(__file__), "queries_ejemplo_pruebas.sql")
with open(sql_path, encoding='utf-8') as f:
    sql_script = f.read()

for statement in sql_script.split(';'):
    stmt = statement.strip()
    if stmt:
        try:
            cursor.execute(stmt)
        except Exception as e:
            print(f"Error ejecutando: {stmt[:60]}... -> {e}")

conn.commit()
close_connection(conn, cursor)
print("Datos de prueba insertados correctamente.")
