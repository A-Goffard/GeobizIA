import os
import pyodbc
from pathlib import Path

# Cargar .env automáticamente si python-dotenv está instalado
try:
    from dotenv import load_dotenv
    # Busca el .env en config relativo al proyecto raíz y también en otras ubicaciones posibles
    env_paths = [
        Path(__file__).parents[3] / "config" / ".env",
        Path(__file__).parent / "config" / ".env",
        Path(__file__).parents[2] / "config" / ".env",
        Path(__file__).parents[1] / "config" / ".env"
    ]
    env_found = False
    for env_path in env_paths:
        if env_path.exists():
            load_dotenv(env_path)
            print(f"Usando .env en: {env_path}")
            env_found = True
            break
    if not env_found:
        print("Advertencia: No se encontró el archivo .env en rutas conocidas.")
except ImportError:
    pass

print("Variables de entorno cargadas:")
for k, v in os.environ.items():
    if "DB_" in k:
        print(f"{k}={v}")

SERVER = os.getenv('DB_SERVER')
DATABASE = os.getenv('DB_NAME')
DRIVER = os.getenv('DB_DRIVER')
if not DRIVER:
    raise RuntimeError("La variable de entorno DB_DRIVER no está definida. Revisa tu archivo .env y asegúrate de que el script la está leyendo correctamente.")
if not DRIVER.startswith('{'):
    DRIVER = f'{{{DRIVER}}}'

USE_WINDOWS_AUTH = os.getenv('DB_USE_WINDOWS_AUTH', 'yes').lower() == 'yes'
USERNAME = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')

if USE_WINDOWS_AUTH:
    conn_str_server = f'DRIVER={DRIVER};SERVER={SERVER};Trusted_Connection=yes;'
    conn_str_db = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
else:
    conn_str_server = f'DRIVER={DRIVER};SERVER={SERVER};UID={USERNAME};PWD={PASSWORD};'
    conn_str_db = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};'

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