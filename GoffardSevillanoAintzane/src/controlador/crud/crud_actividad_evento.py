from .base_crud import BaseCRUD
from src.controlador.dominios.actividad_evento import ActividadEvento
from src.modelo.database.db_conexion import get_connection, close_connection

class CrudActividadEvento(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="actividad_evento",
            fields=["id_actividad", "id_evento"],
            id_field=None  # clave compuesta
        )

    def crear(self, id_actividad, id_evento):
        values = {
            "id_actividad": id_actividad,
            "id_evento": id_evento
        }
        return self.insert(values, ActividadEvento)

    def eliminar(self, id_actividad, id_evento):
        query = f"DELETE FROM {self.table_name} WHERE id_actividad = ? AND id_evento = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_actividad, id_evento))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar ActividadEvento: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_actividad, id_evento):
        query = f"SELECT id_actividad, id_evento FROM {self.table_name} WHERE id_actividad = ? AND id_evento = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_actividad, id_evento))
            row = cursor.fetchone()
            if row:
                return ActividadEvento.crear(row[0], row[1])
            return None
        except Exception as e:
            print(f"Error al buscar ActividadEvento: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def listar(self):
        return self.select_all(ActividadEvento)
