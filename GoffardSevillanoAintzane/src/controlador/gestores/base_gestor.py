from abc import ABC
from typing import List, Optional, TypeVar, Generic
from ..database.db_conexion import get_connection

T = TypeVar('T')

class BaseGestor(ABC, Generic[T]):
    def __init__(self, table_name=None, fields=None, id_field=None):
        self.table_name = table_name
        self.fields = fields
        self.id_field = id_field
        self.lista: List[T] = []

    def agregar(self, values) -> bool:
        placeholders = ', '.join(['?'] * len(self.fields))
        columns = ', '.join(self.fields)
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, values)
                conn.commit()
                cursor.close()
            return True
        except Exception as e:
            print(f"Error al agregar: {e}")
            return False

    def eliminar(self, id_value) -> bool:
        query = f"DELETE FROM {self.table_name} WHERE {self.id_field} = ?"
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_value,))
                conn.commit()
                result = cursor.rowcount > 0
                cursor.close()
            return result
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False

    def buscar(self, id_value):
        query = f"SELECT * FROM {self.table_name} WHERE {self.id_field} = ?"
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_value,))
                result = cursor.fetchone()
                cursor.close()
            return result
        except Exception as e:
            print(f"Error al buscar: {e}")
            return None

    def mostrar_todos_los_elem(self):
        query = f"SELECT * FROM {self.table_name}"
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
            return result
        except Exception as e:
            print(f"Error al mostrar todos los elementos: {e}")
            return []

    def actualizar(self, values):
        set_clause = ', '.join([f"{field}=?" for field in self.fields if field != self.id_field])
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {self.id_field} = ?"
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, values)
                conn.commit()
                result = cursor.rowcount > 0
                cursor.close()
            return result
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def existe(self, id_value) -> bool:
        query = f"SELECT 1 FROM {self.table_name} WHERE {self.id_field} = ?"
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_value,))
                result = cursor.fetchone()
                cursor.close()
            return result is not None
        except Exception as e:
            print(f"Error al comprobar existencia: {e}")
            return False

    def cantidad_elementos(self) -> int:
        query = f"SELECT COUNT(*) FROM {self.table_name}"
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                result = cursor.fetchone()
                cursor.close()
            return result[0] if result else 0
        except Exception as e:
            print(f"Error al contar elementos: {e}")
            return 0

    def mostrar_elemento(self, id_value) -> str:
        query = f"SELECT * FROM {self.table_name} WHERE {self.id_field} = ?"
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_value,))
                row = cursor.fetchone()
                cursor.close()
            if row:
                return str(row)
            else:
                return "Elemento no encontrado."
        except Exception as e:
            return f"Error al mostrar elemento: {e}"

