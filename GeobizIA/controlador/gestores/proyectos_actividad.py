from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.proyecto_actividad import ProyectoActividad
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class ProyectosActividadGestor(BaseGestor[ProyectoActividad]):
    def __init__(self):
        super().__init__(table_name="proyecto_actividad", id_field=None, domain_class=ProyectoActividad)

    def agregar(self, proyecto_actividad: ProyectoActividad):
        if self.existe((proyecto_actividad.id_proyecto, proyecto_actividad.id_actividad)):
            print(f"Error: Ya existe la relación proyecto_actividad ({proyecto_actividad.id_proyecto}, {proyecto_actividad.id_actividad}).")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"INSERT INTO {self.table_name} (id_proyecto, id_actividad) VALUES (?, ?)"
            cursor.execute(query, (proyecto_actividad.id_proyecto, proyecto_actividad.id_actividad))
            conn.commit()
            return proyecto_actividad
        except Exception as e:
            print(f"Error al agregar proyecto_actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tuple):
        id_proyecto, id_actividad = id_tuple
        if not self.existe((id_proyecto, id_actividad)):
            print(f"Error: No existe la relación proyecto_actividad ({id_proyecto}, {id_actividad}).")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_proyecto = ? AND id_actividad = ?"
            cursor.execute(query, (id_proyecto, id_actividad))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar proyecto_actividad: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tuple):
        id_proyecto, id_actividad = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_proyecto, id_actividad FROM {self.table_name} WHERE id_proyecto = ? AND id_actividad = ?"
            cursor.execute(query, (id_proyecto, id_actividad))
            row = cursor.fetchone()
            if row:
                return ProyectoActividad(*row)
            return None
        except Exception as e:
            print(f"Error al buscar proyecto_actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_proyecto, id_actividad FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [ProyectoActividad(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar proyecto_actividad: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, obj):
        print("No se permite actualizar una relación proyecto_actividad (clave compuesta).")
        return False

    def existe(self, id_tuple):
        id_proyecto, id_actividad = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_proyecto = ? AND id_actividad = ?"
            cursor.execute(query, (id_proyecto, id_actividad))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de proyecto_actividad: {e}")
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
            print(f"Error al contar proyecto_actividad: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, proyecto_actividad: ProyectoActividad) -> str:
        return str(proyecto_actividad)
