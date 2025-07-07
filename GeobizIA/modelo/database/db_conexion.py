import pyodbc
from GeobizIA.modelo.database.config.constantes_conexion import get_connection_string

def get_connection():
    """
    Devuelve una conexión pyodbc usando la configuración centralizada.
    """
    conn_str = get_connection_string()
    return pyodbc.connect(conn_str)

def close_connection(conn, cursor=None):
    """
    Cierra el cursor y la conexión a la base de datos de forma segura.
    """
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    except Exception as e:
        print(f"Error al cerrar la conexión o cursor: {e}")