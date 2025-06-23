import os
import pyodbc
import sys

# Opcional: cargar .env automáticamente si usas python-dotenv
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), "config", ".env"))
except ImportError:
    pass  # Si no tienes python-dotenv instalado, ignora

def get_connection():
    """
    Establece y retorna una conexión a SQL Server.
    """
    # Configuración de la conexión
    server = 'your_server_name'  # Ejemplo: 'localhost' o 'SERVIDOR\INSTANCIA'
    database = 'your_database_name'  # Nombre de la base de datos
    username = 'your_username'  # Nombre de usuario
    password = 'your_password'  # Contraseña
    driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el driver instalado

    # Cadena de conexión
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        # Establecer conexión
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        sys.exit(1)

def close_connection(conn, cursor=None):
    """
    Cierra el cursor y la conexión a la base de datos.
    """
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    except pyodbc.Error as e:
        print(f"Error al cerrar la conexión: {e}")