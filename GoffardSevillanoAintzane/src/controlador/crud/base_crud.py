from typing import List, Optional, TypeVar
import pyodbc
from src.modelo.database.db_conexion import get_connection, close_connection

T = TypeVar('T')

class BaseCRUD:
    def __init__(self, table_name: str, fields: List[str], id_field: str):
        """
        Inicializa la clase base para operaciones CRUD con SQL.

        Args:
            table_name (str): Nombre de la tabla en la base de datos.
            fields (List[str]): Lista de nombres de los campos de la tabla.
            id_field (str): Nombre del campo de clave primaria.
        """
        self.table_name = table_name
        self.fields = fields
        self.id_field = id_field

    def insert(self, values: dict, domain_class, is_identity: bool = False) -> Optional[object]:
        """
        Inserta un nuevo registro en la tabla.

        Args:
            values (dict): Diccionario con los valores de los campos.
            domain_class: Clase del dominio para crear instancias.
            is_identity (bool): True si el campo ID es IDENTITY.

        Returns:
            Optional[object]: Objeto del dominio creado, o None si falla.
        """
        # Excluye id_field si no está en values (para autoincrementales)
        fields = [f for f in self.fields if f in values]
        if not all(field in values for field in fields):
            print(f"Error: Faltan campos requeridos: {fields}")
            return None

        params = [values[field] for field in fields]
        placeholders = ', '.join(['?'] * len(fields))
        columns = ', '.join(fields)
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            # Si el campo id es autoincremental y no está en values, obtén el id generado
            if self.id_field and self.id_field not in values:
                cursor.execute("SELECT @@IDENTITY")
                values[self.id_field] = int(cursor.fetchone()[0])
            elif is_identity:
                cursor.execute("SELECT @@IDENTITY")
                values[self.id_field] = int(cursor.fetchone()[0])
            conn.commit()
            # Usa el método 'crear' si existe, si no, usa el constructor
            if domain_class:
                if hasattr(domain_class, "crear"):
                    try:
                        return domain_class.crear(**values)
                    except TypeError:
                        return domain_class(**values)
                elif callable(domain_class):
                    return domain_class(**values)
            return True
        except pyodbc.Error as e:
            print(f"Error al insertar registro: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def delete(self, id_value) -> bool:
        """
        Elimina un registro por su ID.

        Args:
            id_value: Valor del campo ID.

        Returns:
            bool: True si se eliminó, False si no.
        """
        query = f"DELETE FROM {self.table_name} WHERE {self.id_field} = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_value,))
            conn.commit()
            return cursor.rowcount > 0
        except pyodbc.Error as e:
            print(f"Error al eliminar registro: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def select_by_id(self, id_value, domain_class) -> Optional[object]:
        """
        Busca un registro por su ID.

        Args:
            id_value: Valor del campo ID.
            domain_class: Clase del dominio para crear instancias.

        Returns:
            Optional[object]: Objeto del dominio si se encuentra, o None si no.
        """
        query = f"SELECT {', '.join(self.fields)} FROM {self.table_name} WHERE {self.id_field} = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_value,))
            row = cursor.fetchone()
            if row:
                values = {field: getattr(row, field) for field in self.fields}
                return domain_class.crear(**values)
            return None
        except pyodbc.Error as e:
            print(f"Error al buscar registro: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def select_all(self, domain_class) -> List[object]:
        """
        Devuelve todos los registros de la tabla.

        Args:
            domain_class: Clase del dominio para crear instancias.

        Returns:
            List[object]: Lista de objetos del dominio.
        """
        query = f"SELECT {', '.join(self.fields)} FROM {self.table_name}"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return [domain_class.crear(**{field: getattr(row, field) for field in self.fields}) for row in rows]
        except pyodbc.Error as e:
            print(f"Error al mostrar todos los registros: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def update(self, id_value, values: dict) -> bool:
        """
        Actualiza un registro existente.

        Args:
            id_value: Valor del campo ID.
            values (dict): Diccionario con los campos a actualizar.

        Returns:
            bool: True si se actualizó, False si no.
        """
        updates = []
        params = []
        for field in self.fields:
            if field in values and field != self.id_field and values[field] is not None:
                updates.append(f"{field} = ?")
                params.append(values[field])
        
        if not updates:
            print("No se proporcionaron campos para actualizar.")
            return False

        params.append(id_value)
        query = f"UPDATE {self.table_name} SET {', '.join(updates)} WHERE {self.id_field} = ?"
        
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount > 0
        except pyodbc.Error as e:
            print(f"Error al actualizar registro: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def exists(self, id_value) -> bool:
        """
        Verifica si un registro existe por su ID.

        Args:
            id_value: Valor del campo ID.

        Returns:
            bool: True si el registro existe, False si no.
        """
        query = f"SELECT 1 FROM {self.table_name} WHERE {self.id_field} = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_value,))
            return cursor.fetchone() is not None
        except pyodbc.Error as e:
            print(f"Error al comprobar existencia: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def count(self) -> int:
        """
        Devuelve el número total de registros en la tabla.

        Returns:
            int: Cantidad de registros.
        """
        query = f"SELECT COUNT(*) FROM {self.table_name}"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchone()[0]
        except pyodbc.Error as e:
            print(f"Error al contar elementos: {e}")
            return 0
        finally:
            close_connection(conn, cursor)