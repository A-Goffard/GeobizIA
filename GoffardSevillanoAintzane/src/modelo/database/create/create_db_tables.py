import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.modelo.database.db_conexion import get_connection, close_connection
from src.modelo.database.config.constantes_conexion import get_connection_string
import pyodbc

# Conexión a master para crear la base de datos si no existe
master_conn = pyodbc.connect(get_connection_string(database="master"))
master_cursor = master_conn.cursor()
try:
    # Deshabilita la autocommit para ejecutar CREATE DATABASE fuera de una transacción
    master_conn.autocommit = True
    master_cursor.execute("IF DB_ID('GeobizIAPruebas') IS NULL CREATE DATABASE GeobizIAPruebas;")
finally:
    master_cursor.close()
    master_conn.close()

# Ahora conecta a la base de datos y sigue con el resto del código
conn = get_connection()
cursor = conn.cursor()

# Leer el SQL de creación de tablas
# Usa la ruta relativa al archivo actual
sql_path = os.path.join(os.path.dirname(__file__), "queries_creacion_tablas.sql")
with open(sql_path, encoding='utf-8') as f:
    sql_script = f.read()

# Ejecutar cada sentencia CREATE TABLE
for statement in sql_script.split(';'):
    stmt = statement.strip()
    if stmt:
        try:
            cursor.execute(stmt)
        except Exception as e:
            print(f"Error ejecutando: {stmt[:60]}... -> {e}")

conn.commit()
close_connection(conn, cursor)
print("Tablas creadas/verificadas.")

# Al ejecutar este archivo se crea la base de datos (si no existe) y luego se crean todas las tablas
# definidas en el archivo queries_creacion_tablas.sql. Si las tablas ya existen, simplemente ignora el error.