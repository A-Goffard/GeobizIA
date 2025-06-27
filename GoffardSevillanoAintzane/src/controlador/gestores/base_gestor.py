from abc import ABC
from typing import List, Optional, TypeVar, Generic
import pyodbc
from src.modelo.database.db_conexion import get_connection, close_connection

T = TypeVar('T')

class BaseGestor(ABC, Generic[T]):
    def __init__(self, table_name: str, fields: List[str], id_field: str, domain_class: type):
        """
        Inicializa el gestor base para operaciones CRUD.

        Args:
            table_name (str): Nombre de la tabla en la base de datos.
            fields (List[str]): Lista de nombres de los campos de la tabla.
            id_field (str): Nombre del campo de clave primaria.
            domain_class (type): Clase del dominio para crear instancias (por ejemplo, Rol, Persona).
        """
        self.table_name = table_name
        self.fields = fields
        self.id_field = id_field
        self.domain_class = domain_class

    def agregar(self, **kwargs) -> Optional[T]:
        """
        Agrega un nuevo registro a la base de datos, manejando columnas IDENTITY.

        Args:
            **kwargs: Diccionario con los valores de los campos (clave: nombre del campo).

        Returns:
            Optional[T]: Objeto del dominio creado, o None si falla.
        """
        fields = [f for f in self.fields if f != self.id_field or not self.is_identity_field()]
        if not all(field in kwargs for field in fields):
            print(f"Error: Faltan campos requeridos: {fields}")
            return None

        values = [kwargs[field] for field in fields]
        placeholders = ', '.join(['?'] * len(fields))
        columns = ', '.join(fields)
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, values)
            if self.is_identity_field():
                cursor.execute("SELECT @@IDENTITY")
                kwargs[self.id_field] = int(cursor.fetchone()[0])
            conn.commit()
            return self.domain_class.crear(**kwargs)
        except pyodbc.Error as e:
            print(f"Error al agregar registro: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_value) -> bool:
        """
        Elimina un registro de la base de datos por su ID.

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

    def buscar(self, id_value) -> Optional[T]:
        """
        Busca un registro por su ID y lo devuelve como objeto del dominio.

        Args:
            id_value: Valor del campo ID.

        Returns:
            Optional[T]: Objeto del dominio si se encuentra, o None si no.
        """
        query = f"SELECT {', '.join(self.fields)} FROM {self.table_name} WHERE {self.id_field} = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_value,))
            row = cursor.fetchone()
            if row:
                kwargs = {field: getattr(row, field) for field in self.fields}
                return self.domain_class.crear(**kwargs)
            return None
        except pyodbc.Error as e:
            print(f"Error al buscar registro: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self) -> List[T]:
        """
        Devuelve todos los registros de la tabla como lista de objetos del dominio.

        Returns:
            List[T]: Lista de objetos del dominio.
        """
        query = f"SELECT {', '.join(self.fields)} FROM {self.table_name}"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return [self.domain_class.crear(**{field: getattr(row, field) for field in self.fields}) for row in rows]
        except pyodbc.Error as e:
            print(f"Error al mostrar todos los registros: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, id_value, **kwargs) -> bool:
        """
        Actualiza un registro existente en la base de datos.

        Args:
            id_value: Valor del campo ID.
            **kwargs: Diccionario con los campos a actualizar (clave: nombre del campo).

        Returns:
            bool: True si se actualizó, False si no.
        """
        updates = []
        params = []
        for field in self.fields:
            if field in kwargs and field != self.id_field and kwargs[field] is not None:
                updates.append(f"{field} = ?")
                params.append(kwargs[field])
        
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

    def existe(self, id_value) -> bool:
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

    def cantidad_elementos(self) -> int:
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

    def validar_clave_foranea(self, fk_field: str, fk_value, fk_table: str, fk_id_field: str) -> bool:
        """
        Valida si un valor de clave foránea existe en la tabla referenciada.

        Args:
            fk_field (str): Nombre del campo de clave foránea.
            fk_value: Valor de la clave foránea.
            fk_table (str): Nombre de la tabla referenciada.
            fk_id_field (str): Nombre del campo ID en la tabla referenciada.

        Returns:
            bool: True si el valor existe, False si no.
        """
        query = f"SELECT 1 FROM {fk_table} WHERE {fk_id_field} = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (fk_value,))
            return cursor.fetchone() is not None
        except pyodbc.Error as e:
            print(f"Error al validar clave foránea {fk_field}: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def is_identity_field(self) -> bool:
        """
        Verifica si id_field es una columna IDENTITY en la base de datos.

        Returns:
            bool: True si el campo es IDENTITY, False si no.
        """
        query = """
            SELECT COLUMNPROPERTY(OBJECT_ID(?), ?, 'IsIdentity') AS is_identity
        """
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (self.table_name, self.id_field))
            result = cursor.fetchone()
            return bool(result.is_identity) if result else False
        except pyodbc.Error as e:
            print(f"Error al verificar si {self.id_field} es IDENTITY: {e}")
            return False
        finally:
            close_connection(conn, cursor)