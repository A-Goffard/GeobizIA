import pyodbc
import os

# Opcional: cargar .env automáticamente si usas python-dotenv
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), "config", ".env"))
except ImportError:
    pass  # Si no tienes python-dotenv instalado, ignora

class ConexionBD:
    def __init__(self):
        self.server = os.getenv('SQLSERVER_SERVER')
        self.database = os.getenv('SQLSERVER_DATABASE')
        self.username = os.getenv('SQLSERVER_USER')
        self.password = os.getenv('SQLSERVER_PASSWORD')
        self.driver = '{ODBC Driver 17 for SQL Server}'  # Cambia si usas otro driver

        self.connection_string = (
            f'DRIVER={self.driver};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'UID={self.username};'
            f'PWD={self.password}'
        )
        self.conn = None

    def conectar(self):
        if self.conn is None:
            self.conn = pyodbc.connect(self.connection_string)
        return self.conn

    def cerrar(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def get_cursor(self):
        conn = self.conectar()
        return conn.cursor()
