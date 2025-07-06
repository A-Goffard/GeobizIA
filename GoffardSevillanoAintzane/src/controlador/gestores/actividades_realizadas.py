from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.actividad_realizada import ActividadRealizada
from src.modelo.database.db_conexion import get_connection, close_connection

class ActividadesRealizadas(BaseGestor[ActividadRealizada]):
    def __init__(self):
        super().__init__(table_name="actividad_realizada", id_field="id_actividad_realizada", domain_class=ActividadRealizada)

    def agregar(self, actividad_realizada: ActividadRealizada):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_actividad, fecha, asistentes, coste_economico, facturacion, observaciones, id_evento, id_proyecto)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                actividad_realizada.id_actividad,
                actividad_realizada.fecha,
                actividad_realizada.asistentes,
                actividad_realizada.coste_economico,
                actividad_realizada.facturacion,
                actividad_realizada.observaciones,
                actividad_realizada.id_evento,
                actividad_realizada.id_proyecto
            ))
            conn.commit()
            cursor.execute("SELECT @@IDENTITY")
            id_generado = int(cursor.fetchone()[0])
            return self.buscar(id_generado)
        except Exception as e:
            print(f"Error al agregar actividad_realizada: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_actividad_realizada):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad_realizada, id_actividad, fecha, asistentes, coste_economico, facturacion, observaciones, id_evento, id_proyecto FROM {self.table_name} WHERE id_actividad_realizada = ?"
            cursor.execute(query, (id_actividad_realizada,))
            row = cursor.fetchone()
            if row:
                return ActividadRealizada(*row)
            return None
        except Exception as e:
            print(f"Error al buscar actividad_realizada: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad_realizada, id_actividad, fecha, asistentes, coste_economico, facturacion, observaciones, id_evento, id_proyecto FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [ActividadRealizada(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar actividades_realizadas: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_actividad_realizada):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_actividad_realizada = ?"
            cursor.execute(query, (id_actividad_realizada,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar actividad_realizada: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def actualizar(self, actividad_realizada: ActividadRealizada):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET id_actividad=?, fecha=?, asistentes=?, coste_economico=?, facturacion=?, observaciones=?, id_evento=?, id_proyecto=?
                WHERE id_actividad_realizada=?
            """
            cursor.execute(query, (
                actividad_realizada.id_actividad,
                actividad_realizada.fecha,
                actividad_realizada.asistentes,
                actividad_realizada.coste_economico,
                actividad_realizada.facturacion,
                actividad_realizada.observaciones,
                actividad_realizada.id_evento,
                actividad_realizada.id_proyecto,
                actividad_realizada.id_actividad_realizada
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar actividad_realizada: {e}")
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
            print(f"Error al contar actividades_realizadas: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def existe(self, id_actividad_realizada):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE {self.id_field} = ?"
            cursor.execute(query, (id_actividad_realizada,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de actividad_realizada: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, actividad_realizada):
        return str(actividad_realizada)
