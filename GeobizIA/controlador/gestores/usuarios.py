from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.usuario import Usuario
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Usuarios(BaseGestor[Usuario]):
    def __init__(self):
        super().__init__(table_name="usuario", id_field="id_usuario", domain_class=Usuario)

    def agregar(self, usuario: Usuario):
        if self.existe(usuario.id_usuario):
            print(f"Error: Ya existe un usuario con id_usuario={usuario.id_usuario}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_usuario, id_persona, fecha_nacimiento, rol, preferencias, password)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                usuario.id_usuario,
                usuario.id_persona,
                usuario.fecha_nacimiento,
                usuario.rol,
                usuario.preferencias,
                usuario.password
            ))
            conn.commit()
            return usuario
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_usuario):
        if not self.existe(id_usuario):
            print(f"Error: No existe un usuario con id_usuario={id_usuario}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_usuario = ?"
            cursor.execute(query, (id_usuario,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_usuario):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_usuario, id_persona, fecha_nacimiento, rol, preferencias, password FROM {self.table_name} WHERE id_usuario = ?"
            cursor.execute(query, (id_usuario,))
            row = cursor.fetchone()
            if row:
                return Usuario(*row)
            return None
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_usuario, id_persona, fecha_nacimiento, rol, preferencias, password FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Usuario(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, usuario: Usuario):
        if not self.existe(usuario.id_usuario):
            print(f"Error: No existe un usuario con id_usuario={usuario.id_usuario}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET id_persona=?, fecha_nacimiento=?, rol=?, preferencias=?, password=?
                WHERE id_usuario=?
            """
            cursor.execute(query, (
                usuario.id_persona,
                usuario.fecha_nacimiento,
                usuario.rol,
                usuario.preferencias,
                usuario.password,
                usuario.id_usuario
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_usuario):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_usuario = ?"
            cursor.execute(query, (id_usuario,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de usuario: {e}")
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
            print(f"Error al contar usuarios: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, usuario: Usuario) -> str:
        return str(usuario)