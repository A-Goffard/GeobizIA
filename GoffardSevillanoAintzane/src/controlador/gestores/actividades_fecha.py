from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.actividad_fecha import ActividadFecha
from src.modelo.database.db_conexion import get_connection, close_connection

class ActividadesFechaGestor(BaseGestor[ActividadFecha]):
    def __init__(self):
        super().__init__(table_name="actividad_fecha", id_field=None, domain_class=ActividadFecha)

    def agregar(self, actividad_fecha: ActividadFecha):
        if self.existe((actividad_fecha.id_actividad, actividad_fecha.id_fecha)):
            print(f"Error: Ya existe la relación actividad_fecha ({actividad_fecha.id_actividad}, {actividad_fecha.id_fecha}).")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"INSERT INTO {self.table_name} (id_actividad, id_fecha) VALUES (?, ?)"
            cursor.execute(query, (actividad_fecha.id_actividad, actividad_fecha.id_fecha))
            conn.commit()
            return actividad_fecha
        except Exception as e:
            print(f"Error al agregar actividad_fecha: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tuple):
        id_actividad, id_fecha = id_tuple
        if not self.existe((id_actividad, id_fecha)):
            print(f"Error: No existe la relación actividad_fecha ({id_actividad}, {id_fecha}).")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_actividad = ? AND id_fecha = ?"
            cursor.execute(query, (id_actividad, id_fecha))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar actividad_fecha: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tuple):
        id_actividad, id_fecha = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad, id_fecha FROM {self.table_name} WHERE id_actividad = ? AND id_fecha = ?"
            cursor.execute(query, (id_actividad, id_fecha))
            row = cursor.fetchone()
            if row:
                return ActividadFecha(*row)
            return None
        except Exception as e:
            print(f"Error al buscar actividad_fecha: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad, id_fecha FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [ActividadFecha(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar actividad_fecha: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, obj):
        print("No se permite actualizar una relación actividad_fecha (clave compuesta).")
        return False

    def existe(self, id_tuple):
        id_actividad, id_fecha = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_actividad = ? AND id_fecha = ?"
            cursor.execute(query, (id_actividad, id_fecha))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de actividad_fecha: {e}")
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
            print(f"Error al contar actividad_fecha: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, actividad_fecha: ActividadFecha) -> str:
        return str(actividad_fecha)
