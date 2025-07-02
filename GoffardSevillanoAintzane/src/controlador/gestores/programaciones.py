from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.programacion import Programacion
from src.modelo.database.db_conexion import get_connection, close_connection

class Programaciones(BaseGestor[Programacion]):
    def __init__(self):
        super().__init__(table_name="programacion", id_field="id_programacion", domain_class=Programacion)

    def agregar(self, programacion: Programacion):
        if self.existe(programacion.id_programacion):
            print(f"Error: Ya existe una programación con id_programacion={programacion.id_programacion}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                programacion.id_programacion,
                programacion.publicacion_id,
                programacion.red_social_id,
                programacion.fecha_programada,
                programacion.estado,
                programacion.notificaciones,
                programacion.responsable
            ))
            conn.commit()
            return programacion
        except Exception as e:
            print(f"Error al agregar programación: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_programacion):
        if not self.existe(id_programacion):
            print(f"Error: No existe una programación con id_programacion={id_programacion}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_programacion = ?"
            cursor.execute(query, (id_programacion,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar programación: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_programacion):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable FROM {self.table_name} WHERE id_programacion = ?"
            cursor.execute(query, (id_programacion,))
            row = cursor.fetchone()
            if row:
                return Programacion(*row)
            return None
        except Exception as e:
            print(f"Error al buscar programación: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_programacion, publicacion_id, red_social_id, fecha_programada, estado, notificaciones, responsable FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Programacion(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar programaciones: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, programacion: Programacion):
        if not self.existe(programacion.id_programacion):
            print(f"Error: No existe una programación con id_programacion={programacion.id_programacion}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET publicacion_id=?, red_social_id=?, fecha_programada=?, estado=?, notificaciones=?, responsable=?
                WHERE id_programacion=?
            """
            cursor.execute(query, (
                programacion.publicacion_id,
                programacion.red_social_id,
                programacion.fecha_programada,
                programacion.estado,
                programacion.notificaciones,
                programacion.responsable,
                programacion.id_programacion
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar programación: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_programacion):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_programacion = ?"
            cursor.execute(query, (id_programacion,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de programación: {e}")
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
            print(f"Error al contar programaciones: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, programacion: Programacion) -> str:
        return str(programacion)