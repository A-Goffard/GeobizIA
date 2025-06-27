import os
import pyodbc
import sys
from pathlib import Path

# Cargar .env automáticamente si python-dotenv está instalado
try:
    from dotenv import load_dotenv
    # Ajusta según la ubicación real del .env
    env_path = Path(__file__).parent / "config" / ".env"
    # Si .env está en C:/Aintzane/Data Analisis/GeobizIA/config/.env, usa:
    # env_path = Path(__file__).parents[3] / "config" / ".env"
    if not load_dotenv(env_path):
        print(f"Advertencia: No se pudo cargar el archivo .env en {env_path}")
except ImportError:
    print("Advertencia: python-dotenv no está instalado. Usa variables de entorno del sistema.")
    pass

def get_connection():
    """
    Establece una conexión a SQL Server usando autenticación de Windows o SQL Server.

    Returns:
        pyodbc.Connection: Objeto de conexión a la base de datos.

    Raises:
        ValueError: Si faltan variables de entorno requeridas.
        pyodbc.Error: Si falla la conexión a la base de datos.
    """
    server = os.getenv('DB_SERVER', 'DESKTOP-G9GRQKM\SQLEXPRESS')
    database = os.getenv('DB_NAME', 'GeobizIAPruebas')
    driver = os.getenv('DB_DRIVER', '{ODBC Driver 17 for SQL Server}')
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
    """
    Cierra el cursor y la conexión a la base de datos de forma segura.

    Args:
        conn (pyodbc.Connection): Conexión a la base de datos.
        cursor (pyodbc.Cursor, optional): Cursor a cerrar.
    """
    try:
        if cursor:
            cursor.close()
            print("Cursor cerrado exitosamente.")
        if conn:
            conn.close()
            print("Conexión cerrada exitosamente.")
    except pyodbc.Error as e:
        print(f"Error al cerrar la conexión o cursor: {e}")