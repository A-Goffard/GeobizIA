from .base_crud import BaseCRUD
from src.controlador.dominios.tipo_publicacion_redsocial import TipoPublicacionRedSocial
from src.modelo.database.db_conexion import get_connection, close_connection
class CrudTipoPublicacionRedSocial(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="tipo_publicacion_redsocial",
            fields=["id_tipo_publicacion", "id_red_social"],
            id_field=None  # clave compuesta
        )

    def crear(self, id_tipo_publicacion, id_red_social):
        values = {
            "id_tipo_publicacion": id_tipo_publicacion,
            "id_red_social": id_red_social
        }
        return self.insert(values, TipoPublicacionRedSocial)

    def eliminar(self, id_tipo_publicacion, id_red_social):
        query = f"DELETE FROM {self.table_name} WHERE id_tipo_publicacion = ? AND id_red_social = ?"
        
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_tipo_publicacion, id_red_social))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar TipoPublicacionRedSocial: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tipo_publicacion, id_red_social):
        query = f"SELECT id_tipo_publicacion, id_red_social FROM {self.table_name} WHERE id_tipo_publicacion = ? AND id_red_social = ?"
        from src.modelo.database.db_conexion import get_connection, close_connection
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_tipo_publicacion, id_red_social))
            row = cursor.fetchone()
            if row:
                return TipoPublicacionRedSocial(id_tipo_publicacion=row[0], id_red_social=row[1])
            return None
        except Exception as e:
            print(f"Error al buscar TipoPublicacionRedSocial: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def listar(self):
        return self.select_all(TipoPublicacionRedSocial)
