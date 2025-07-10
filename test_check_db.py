from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

try:
    conn = get_connection()
    cursor = conn.cursor()
    
    # Verificar estructura de la tabla cliente
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'cliente'")
    columns = cursor.fetchall()
    print('Columnas de la tabla cliente:')
    for column in columns:
        print(f"- {column[3]} ({column[7]})")
    
    # Verificar qué clientes existen
    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    print(f'\nTotal de clientes: {len(clientes)}')
    if clientes:
        print('Primeros 5 clientes:')
        for i, cliente in enumerate(clientes[:5]):
            print(f"- Cliente {i+1}: {cliente}")
    
    close_connection(conn, cursor)
except Exception as e:
    print(f'Error: {e}')
