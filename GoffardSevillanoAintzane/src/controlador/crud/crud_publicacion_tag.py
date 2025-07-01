from .base_crud import BaseCRUD
from src.controlador.dominios.publicacion_tag import PublicacionTag
from src.modelo.database.db_conexion import get_connection, close_connection

class CrudPublicacionTag(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="publicacion_tag",
            fields=["id_publicacion", "id_tag"],
            id_field=None  # clave compuesta
        )

    def crear(self, id_publicacion, id_tag):
        values = {
            "id_publicacion": id_publicacion,
            "id_tag": id_tag
        }
        return self.insert(values, PublicacionTag)

    def eliminar(self, id_publicacion, id_tag):
        query = f"DELETE FROM {self.table_name} WHERE id_publicacion = ? AND id_tag = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_publicacion, id_tag))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar PublicacionTag: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_publicacion, id_tag):
        query = f"SELECT id_publicacion, id_tag FROM {self.table_name} WHERE id_publicacion = ? AND id_tag = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_publicacion, id_tag))
            row = cursor.fetchone()
            if row:
                return PublicacionTag.crear(row[0], row[1])
            return None
        except Exception as e:
            print(f"Error al buscar PublicacionTag: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def listar(self):
        return self.select_all(PublicacionTag)
