import os
import pyodbc
import sys
from pathlib import Path

# Cargar .env automáticamente
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent / "config" / ".env"
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
    server = os.getenv('DB_SERVER', 'localhost')
    database = os.getenv('DB_NAME')
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

def test_connection():
    """
    Prueba la conexión a la base de datos ejecutando varias consultas.
    """
    conn = None
    cursor = None
    try:
        # Establecer conexión
        conn = get_connection()
        cursor = conn.cursor()

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
