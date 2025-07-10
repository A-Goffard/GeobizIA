from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.rol import Rol
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Roles(BaseGestor[Rol]):
    def __init__(self):
        super().__init__(table_name="rol", id_field="id_rol", domain_class=Rol)

    def agregar(self, rol: Rol):
        if self.existe(rol.id_rol):
            print(f"Error: Ya existe un rol con id_rol={rol.id_rol}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_rol, nombre, descripcion)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (
                rol.id_rol,
                rol.nombre,
                rol.descripcion
            ))
            conn.commit()
            return rol
        except Exception as e:
            print(f"Error al agregar rol: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_rol):
        if not self.existe(id_rol):
            print(f"Error: No existe un rol con id_rol={id_rol}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_rol = ?"
            cursor.execute(query, (id_rol,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar rol: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_rol):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_rol, nombre, descripcion FROM {self.table_name} WHERE id_rol = ?"
            cursor.execute(query, (id_rol,))
            row = cursor.fetchone()
            if row:
                return Rol(
                    id_rol=row[0],
                    nombre=row[1],
                    descripcion=row[2]
                )
            return None
        except Exception as e:
            print(f"Error al buscar rol: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_rol, nombre, descripcion FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Rol(
                id_rol=row[0],
                nombre=row[1],
                descripcion=row[2]
            ) for row in rows]
        except Exception as e:
            print(f"Error al listar roles: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, rol: Rol):
        if not self.existe(rol.id_rol):
            print(f"Error: No existe un rol con id_rol={rol.id_rol}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET nombre=?, descripcion=?
                WHERE id_rol=?
            """
            cursor.execute(query, (
                rol.nombre,
                rol.descripcion,
                rol.id_rol
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar rol: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_rol):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_rol = ?"
            cursor.execute(query, (id_rol,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de rol: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def cantidad_elementos(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT COUNT(*) FROM {self.table_name}"
            cursor.execute(query)
            return cursor.fetchone()[0]
        except Exception as e:
            print(f"Error al contar roles: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, rol: Rol) -> str:
        return str(rol)