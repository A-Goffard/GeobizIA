from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.actividad import Actividad
from src.modelo.database.db_conexion import get_connection, close_connection

class Actividades(BaseGestor[Actividad]):
    def __init__(self):
        super().__init__(table_name="actividad", id_field="id_actividad", domain_class=Actividad)

    def agregar(self, actividad: Actividad):
        if self.existe(actividad.id_actividad):
            print(f"Error: Ya existe una actividad con id_actividad={actividad.id_actividad}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                actividad.id_actividad,
                actividad.tipo,
                actividad.nombre,
                actividad.descripcion,
                actividad.responsable,
                actividad.duracion,
                actividad.coste_economico,
                actividad.coste_horas,
                actividad.facturacion,
                actividad.resultados,
                actividad.valoracion,
                actividad.observaciones
            ))
            conn.commit()
            return actividad
        except Exception as e:
            print(f"Error al agregar actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_actividad):
        if not self.existe(id_actividad):
            print(f"Error: No existe una actividad con id_actividad={id_actividad}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_actividad = ?"
            cursor.execute(query, (id_actividad,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar actividad: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_actividad):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones FROM {self.table_name} WHERE id_actividad = ?"
            cursor.execute(query, (id_actividad,))
            row = cursor.fetchone()
            if row:
                return Actividad(*row)
            return None
        except Exception as e:
            print(f"Error al buscar actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Actividad(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar actividades: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, actividad: Actividad):
        if not self.existe(actividad.id_actividad):
            print(f"Error: No existe una actividad con id_actividad={actividad.id_actividad}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET tipo=?, nombre=?, descripcion=?, responsable=?, duracion=?, coste_economico=?, coste_horas=?, facturacion=?, resultados=?, valoracion=?, observaciones=?
                WHERE id_actividad=?
            """
            cursor.execute(query, (
                actividad.tipo,
                actividad.nombre,
                actividad.descripcion,
                actividad.responsable,
                actividad.duracion,
                actividad.coste_economico,
                actividad.coste_horas,
                actividad.facturacion,
                actividad.resultados,
                actividad.valoracion,
                actividad.observaciones,
                actividad.id_actividad
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar actividad: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_actividad):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_actividad = ?"
            cursor.execute(query, (id_actividad,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de actividad: {e}")
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
            print(f"Error al contar actividades: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, actividad: Actividad) -> str:
        return str(actividad)