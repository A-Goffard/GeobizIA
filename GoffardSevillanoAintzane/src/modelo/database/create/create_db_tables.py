import pyodbc

# Configura estos valores según tu entorno
SERVER = r'DESKTOP-G9GRQKM\SQLEXPRESS'
DATABASE = 'GeobizIAPruebas2'
USERNAME = ''
PASSWORD = ''
DRIVER = 'ODBC Driver 17 for SQL Server'

# 1. Conexión al servidor (sin base de datos)
conn_str_server = f'DRIVER={{{DRIVER}}};SERVER={SERVER};Trusted_Connection=yes;'
conn_server = pyodbc.connect(conn_str_server, autocommit=True)
cursor_server = conn_server.cursor()

# 2. Crear la base de datos si no existe
try:
    cursor_server.execute(f"IF DB_ID('{DATABASE}') IS NULL CREATE DATABASE [{DATABASE}]")
    print(f"Base de datos '{DATABASE}' verificada/creada.")
finally:
    cursor_server.close()
    conn_server.close()

# 3. Conexión a la base de datos
conn_str_db = f'DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
conn_db = pyodbc.connect(conn_str_db)
cursor_db = conn_db.cursor()

# 4. Leer el SQL de creación de tablas
# Usa la ruta absoluta correcta al archivo SQL
sql_path = r'c:\Aintzane\Data Analisis\GeobizIA\GoffardSevillanoAintzane\src\modelo\database\create\queries_creacion_tablas.sql'
with open(sql_path, encoding='utf-8') as f:
    sql_script = f.read()

# 5. Ejecutar cada sentencia CREATE TABLE
for statement in sql_script.split(';'):
    stmt = statement.strip()
    if stmt:
        try:
            cursor_db.execute(stmt)
        except Exception as e:
            print(f"Error ejecutando: {stmt[:60]}... -> {e}")

conn_db.commit()
cursor_db.close()
conn_db.close()
print("Tablas creadas/verificadas.")

# Sí, al ejecutar este archivo se crea la base de datos (si no existe) y luego se crean todas las tablas
# definidas en el archivo queries_creacion_tablas.sql. Si las tablas ya existen, simplemente ignora el error.