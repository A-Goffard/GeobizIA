from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.tipo_publicacion_redsocial import TipoPublicacionRedsocial
from src.modelo.database.db_conexion import get_connection, close_connection

class TipoPublicacionRedsocialGestor(BaseGestor[TipoPublicacionRedsocial]):
    def __init__(self):
        super().__init__(table_name="tipo_publicacion_redsocial", id_field=None, domain_class=TipoPublicacionRedsocial)

    def agregar(self, obj: TipoPublicacionRedsocial):
        if self.existe((obj.id_tipo_publicacion, obj.id_red_social)):
            print(f"Error: Ya existe la relación tipo_publicacion_redsocial ({obj.id_tipo_publicacion}, {obj.id_red_social}).")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"INSERT INTO {self.table_name} (id_tipo_publicacion, id_red_social) VALUES (?, ?)"
            cursor.execute(query, (obj.id_tipo_publicacion, obj.id_red_social))
            conn.commit()
            return obj
        except Exception as e:
            print(f"Error al agregar tipo_publicacion_redsocial: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tuple):
        id_tipo_publicacion, id_red_social = id_tuple
        if not self.existe((id_tipo_publicacion, id_red_social)):
            print(f"Error: No existe la relación tipo_publicacion_redsocial ({id_tipo_publicacion}, {id_red_social}).")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_tipo_publicacion = ? AND id_red_social = ?"
            cursor.execute(query, (id_tipo_publicacion, id_red_social))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar tipo_publicacion_redsocial: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tuple):
        id_tipo_publicacion, id_red_social = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_tipo_publicacion, id_red_social FROM {self.table_name} WHERE id_tipo_publicacion = ? AND id_red_social = ?"
            cursor.execute(query, (id_tipo_publicacion, id_red_social))
            row = cursor.fetchone()
            if row:
                return TipoPublicacionRedsocial(*row)
            return None
        except Exception as e:
            print(f"Error al buscar tipo_publicacion_redsocial: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_tipo_publicacion, id_red_social FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [TipoPublicacionRedsocial(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar tipo_publicacion_redsocial: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, obj):
        print("No se permite actualizar una relación tipo_publicacion_redsocial (clave compuesta).")
        return False

    def existe(self, id_tuple):
        id_tipo_publicacion, id_red_social = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_tipo_publicacion = ? AND id_red_social = ?"
            cursor.execute(query, (id_tipo_publicacion, id_red_social))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de tipo_publicacion_redsocial: {e}")
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
            print(f"Error al contar tipo_publicacion_redsocial: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, obj: TipoPublicacionRedsocial) -> str:
        return str(obj)
