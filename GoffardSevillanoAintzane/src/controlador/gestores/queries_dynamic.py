def get_insert_query(table, fields):
    placeholders = ', '.join(['?'] * len(fields))
    columns = ', '.join(fields)
    return f"INSERT INTO {table} ({columns}) VALUES ({placeholders});"

def get_select_query(table, id_field):
    return f"SELECT * FROM {table} WHERE {id_field} = ?;"

def get_update_query(table, fields, id_field):
    set_clause = ', '.join([f"{field}=?" for field in fields if field != id_field])
    return f"UPDATE {table} SET {set_clause} WHERE {id_field} = ?;"

def get_delete_query(table, id_field):
    return f"DELETE FROM {table} WHERE {id_field} = ?;"

# Ejemplo de uso:
if __name__ == "__main__":
    # Para la tabla 'usuarios'
    table = "usuarios"
    fields = [
        "id_usuario", "nombre", "apellido", "email", "telefono", "dni", "direccion",
        "cp", "poblacion", "pais", "fecha_nacimiento", "preferencias", "rol", "password"
    ]
    id_field = "id_usuario"

    print(get_insert_query(table, fields))
    print(get_select_query(table, id_field))
    print(get_update_query(table, fields, id_field))
    print(get_delete_query(table, id_field))
