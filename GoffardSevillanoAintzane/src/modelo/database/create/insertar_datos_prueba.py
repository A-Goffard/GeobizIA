import pyodbc

# Configura estos valores según tu entorno
SERVER = r'DESKTOP-G9GRQKM\SQLEXPRESS'
DATABASE = 'GeobizIAPruebas2'
DRIVER = 'ODBC Driver 17 for SQL Server'

conn_str = f'DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Ruta absoluta al archivo con los inserts de prueba
sql_path = r'c:\Aintzane\Data Analisis\GeobizIA\GoffardSevillanoAintzane\src\modelo\database\create\queries_ejemplo_pruebas.sql'
with open(sql_path, encoding='utf-8') as f:
    sql_script = f.read()

# Ejecutar cada sentencia INSERT
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
