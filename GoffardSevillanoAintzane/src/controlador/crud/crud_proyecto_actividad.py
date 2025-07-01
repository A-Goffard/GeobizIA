from .base_crud import BaseCRUD
from src.controlador.dominios.proyecto_actividad import ProyectoActividad
from src.modelo.database.db_conexion import get_connection, close_connection

class CrudProyectoActividad(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="proyecto_actividad",
            fields=["id_proyecto", "id_actividad"],
            id_field=None  # clave compuesta
        )

    def crear(self, id_proyecto, id_actividad):
        values = {
            "id_proyecto": id_proyecto,
            "id_actividad": id_actividad
        }
        return self.insert(values, ProyectoActividad)

    def eliminar(self, id_proyecto, id_actividad):
        query = f"DELETE FROM {self.table_name} WHERE id_proyecto = ? AND id_actividad = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_proyecto, id_actividad))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar ProyectoActividad: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_proyecto, id_actividad):
        query = f"SELECT id_proyecto, id_actividad FROM {self.table_name} WHERE id_proyecto = ? AND id_actividad = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_proyecto, id_actividad))
            row = cursor.fetchone()
            if row:
                return ProyectoActividad.crear(row[0], row[1])
            return None
        except Exception as e:
            print(f"Error al buscar ProyectoActividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def listar(self):
        return self.select_all(ProyectoActividad)
