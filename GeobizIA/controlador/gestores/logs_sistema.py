from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.log_sistema import Log_Sistema
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class LogsSistema(BaseGestor[Log_Sistema]):
    def __init__(self):
        super().__init__(table_name="log_sistema", id_field="id_log_sistema", domain_class=Log_Sistema)

    def agregar(self, log: Log_Sistema):
        if self.existe(log.id_log_sistema):
            print(f"Error: Ya existe un log_sistema con id_log_sistema={log.id_log_sistema}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_log_sistema, usuario_id, fecha, accion, descripcion, nivel)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                log.id_log_sistema,
                log.usuario_id,
                log.fecha,
                log.accion,
                log.descripcion,
                log.nivel
            ))
            conn.commit()
            return log
        except Exception as e:
            print(f"Error al agregar log_sistema: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_log_sistema):
        if not self.existe(id_log_sistema):
            print(f"Error: No existe un log_sistema con id_log_sistema={id_log_sistema}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_log_sistema = ?"
            cursor.execute(query, (id_log_sistema,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar log_sistema: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_log_sistema):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_log_sistema, usuario_id, fecha, accion, descripcion, nivel FROM {self.table_name} WHERE id_log_sistema = ?"
            cursor.execute(query, (id_log_sistema,))
            row = cursor.fetchone()
            if row:
                return Log_Sistema(*row)
            return None
        except Exception as e:
            print(f"Error al buscar log_sistema: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_log_sistema, usuario_id, fecha, accion, descripcion, nivel FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Log_Sistema(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar logs_sistema: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, log: Log_Sistema):
        if not self.existe(log.id_log_sistema):
            print(f"Error: No existe un log_sistema con id_log_sistema={log.id_log_sistema}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET usuario_id=?, fecha=?, accion=?, descripcion=?, nivel=?
                WHERE id_log_sistema=?
            """
            cursor.execute(query, (
                log.usuario_id,
                log.fecha,
                log.accion,
                log.descripcion,
                log.nivel,
                log.id_log_sistema
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar log_sistema: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_log_sistema):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_log_sistema = ?"
            cursor.execute(query, (id_log_sistema,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de log_sistema: {e}")
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
            print(f"Error al contar logs_sistema: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, log: Log_Sistema) -> str:
        return str(log)