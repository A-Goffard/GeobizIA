import os
import pyodbc
import sys
from pathlib import Path

# Cargar .env automáticamente si python-dotenv está instalado
try:
    from dotenv import load_dotenv
    # Busca el .env en config relativo al proyecto raíz y también en otras ubicaciones posibles
    env_paths = [
        Path(__file__).parents[2] / "config" / ".env",
        Path(__file__).parent / "config" / ".env",
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

def get_connection():
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    driver = os.getenv('DB_DRIVER')
    if not driver:
        raise RuntimeError("La variable de entorno DB_DRIVER no está definida. Revisa tu archivo .env.")
    if not driver.startswith('{'):
        driver = f'{{{driver}}}'
    use_windows_auth = os.getenv('DB_USE_WINDOWS_AUTH', 'yes').lower() == 'yes'

    if not database:
        raise ValueError("La variable de entorno DB_NAME es requerida.")

    if use_windows_auth:
        connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes'
    else:
        username = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        if not username or not password:
            raise ValueError("Las variables DB_USER y DB_PASSWORD son requeridas para autenticación de SQL Server.")
        connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        conn = pyodbc.connect(connection_string)
        print(f"Conexión exitosa a la base de datos '{database}' en el servidor '{server}'")
        return conn
    except pyodbc.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        sys.exit(1)

def close_connection(conn, cursor=None):
    try:
        if cursor:
            cursor.close()
            print("Cursor cerrado exitosamente.")
        if conn:
            conn.close()
            print("Conexión cerrada exitosamente.")
    except pyodbc.Error as e:
        print(f"Error al cerrar la conexión o cursor: {e}")