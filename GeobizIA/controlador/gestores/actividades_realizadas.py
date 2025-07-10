from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.actividad_realizada import ActividadRealizada
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

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
                return ActividadRealizada(
                    id_actividad_realizada=row[0],
                    id_actividad=row[1],
                    fecha=row[2],
                    asistentes=row[3],
                    coste_economico=row[4],
                    facturacion=row[5],
                    observaciones=row[6],
                    id_evento=row[7],
                    id_proyecto=row[8]
                )
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
            actividades = []
            for row in rows:
                actividades.append(ActividadRealizada(
                    id_actividad_realizada=row[0],
                    id_actividad=row[1],
                    fecha=row[2],
                    asistentes=row[3],
                    coste_economico=row[4],
                    facturacion=row[5],
                    observaciones=row[6],
                    id_evento=row[7],
                    id_proyecto=row[8]
                ))
            return actividades
        except Exception as e:
            print(f"Error al listar actividades_realizadas: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def buscar_por_id_actividad(self, id_actividad: int):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT * FROM {self.table_name} WHERE id_actividad = ? ORDER BY fecha DESC"
            cursor.execute(query, (id_actividad,))
            rows = cursor.fetchall()
            actividades = []
            for row in rows:
                actividades.append(ActividadRealizada(
                    id_actividad_realizada=row[0],
                    id_actividad=row[1],
                    fecha=row[2],
                    asistentes=row[3],
                    coste_economico=row[4],
                    facturacion=row[5],
                    observaciones=row[6],
                    id_evento=row[7],
                    id_proyecto=row[8]
                ))
            return actividades
        except Exception as e:
            print(f"Error al buscar actividades realizadas por id_actividad: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, actividad_realizada: ActividadRealizada):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
                UPDATE actividad_realizada
                SET fecha=?, asistentes=?, coste_economico=?, facturacion=?, observaciones=?, id_evento=?, id_proyecto=?
                WHERE id_actividad_realizada=?
            """
            cursor.execute(query, (
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
            print(f"Error al actualizar actividad realizada: {e}")
            conn.rollback()
            return False
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
