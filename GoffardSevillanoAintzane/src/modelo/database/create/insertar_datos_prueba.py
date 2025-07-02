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

SERVER = os.getenv('DB_SERVER')
DATABASE = os.getenv('DB_NAME')
DRIVER = os.getenv('DB_DRIVER')
if not DRIVER:
    raise RuntimeError("La variable de entorno DB_DRIVER no está definida. Revisa tu archivo .env.")
if not DRIVER.startswith('{'):
    DRIVER = f'{{{DRIVER}}}'

USE_WINDOWS_AUTH = os.getenv('DB_USE_WINDOWS_AUTH', 'yes').lower() == 'yes'
USERNAME = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')

if USE_WINDOWS_AUTH:
    conn_str = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
else:
    conn_str = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};'

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

sql_path = r'c:\Aintzane\Data Analisis\GeobizIA\GoffardSevillanoAintzane\src\modelo\database\create\queries_ejemplo_pruebas.sql'
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
cursor.close()
conn.close()
print("Datos de prueba insertados correctamente.")

# Sí, puedes añadir más datos al archivo queries_ejemplo_pruebas.sql y volver a ejecutar este script.
# Si intentas insertar registros con claves primarias que ya existen, obtendrás un error de clave duplicada.
# Para evitar errores, usa sentencias como:
#   IF NOT EXISTS (SELECT 1 FROM tabla WHERE id=valor) INSERT INTO tabla (...) VALUES (...)
# o asegúrate de borrar los datos antes de insertar, o usa claves nuevas.
