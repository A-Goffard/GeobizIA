from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.fecha_actividad import FechaActividad
from src.modelo.database.db_conexion import get_connection, close_connection

class FechasActividadGestor(BaseGestor[FechaActividad]):
    def __init__(self):
        super().__init__(table_name="fecha_actividad", id_field="id_fecha", domain_class=FechaActividad)

    def agregar(self, fecha_actividad: FechaActividad):
        if self.existe(fecha_actividad.id_fecha):
            print(f"Error: Ya existe una fecha con id_fecha={fecha_actividad.id_fecha}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"INSERT INTO {self.table_name} (id_fecha, fecha) VALUES (?, ?)"
            cursor.execute(query, (fecha_actividad.id_fecha, fecha_actividad.fecha))
            conn.commit()
            return fecha_actividad
        except Exception as e:
            print(f"Error al agregar fecha_actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_fecha):
        if not self.existe(id_fecha):
            print(f"Error: No existe una fecha con id_fecha={id_fecha}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_fecha = ?"
            cursor.execute(query, (id_fecha,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar fecha_actividad: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_fecha):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_fecha, fecha FROM {self.table_name} WHERE id_fecha = ?"
            cursor.execute(query, (id_fecha,))
            row = cursor.fetchone()
            if row:
                return FechaActividad(*row)
            return None
        except Exception as e:
            print(f"Error al buscar fecha_actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_fecha, fecha FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [FechaActividad(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar fechas_actividad: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, fecha_actividad: FechaActividad):
        if not self.existe(fecha_actividad.id_fecha):
            print(f"Error: No existe una fecha con id_fecha={fecha_actividad.id_fecha}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"UPDATE {self.table_name} SET fecha=? WHERE id_fecha=?"
            cursor.execute(query, (fecha_actividad.fecha, fecha_actividad.id_fecha))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar fecha_actividad: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_fecha):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_fecha = ?"
            cursor.execute(query, (id_fecha,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de fecha_actividad: {e}")
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
            print(f"Error al contar fechas_actividad: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, fecha_actividad: FechaActividad) -> str:
        return str(fecha_actividad)