from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.usuario import Usuario
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Usuarios(BaseGestor[Usuario]):
    def __init__(self):
        super().__init__(table_name="usuario", id_field="id_usuario", domain_class=Usuario)

    def agregar(self, usuario: Usuario):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_persona, fecha_nacimiento, rol, preferencias, password)
                OUTPUT INSERTED.id_usuario
                VALUES (?, ?, ?, ?, ?)
            """
            if usuario.password and not usuario.password.startswith('$2b$'):
                 usuario.set_password(usuario.password)

            last_id = cursor.execute(query, (
                usuario.id_persona,
                usuario.fecha_nacimiento,
                usuario.rol,
                usuario.preferencias,
                usuario.password
            )).fetchval()

            conn.commit()

            if last_id is not None:
                usuario.id_usuario = last_id
                return usuario
            else:
                raise Exception("La consulta INSERT no devolvió un ID de usuario.")
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            conn.rollback()
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
                user = Usuario(id_persona=row[1], fecha_nacimiento=row[2], rol=row[3], preferencias=row[4], id_usuario=row[0])
                user.password = row[5]
                return user
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
            usuarios = []
            for row in rows:
                user = Usuario(id_persona=row[1], fecha_nacimiento=row[2], rol=row[3], preferencias=row[4], id_usuario=row[0])
                user.password = row[5]
                usuarios.append(user)
            return usuarios
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

    def buscar_por_email(self, email: str):
        """Busca un usuario por su email a través de la tabla persona."""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                SELECT u.id_usuario, u.id_persona, u.fecha_nacimiento, u.rol, u.preferencias, u.password
                FROM usuario u
                JOIN persona p ON u.id_persona = p.id_persona
                WHERE p.email = ?
            """
            cursor.execute(query, (email,))
            row = cursor.fetchone()
            if row:
                user = Usuario(id_usuario=row[0], id_persona=row[1], fecha_nacimiento=row[2], rol=row[3], preferencias=row[4])
                user.password = row[5]
                return user
            return None
        except Exception as e:
            print(f"Error al buscar usuario por email: {e}")
            return None
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