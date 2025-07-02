from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.publicacion_tag import PublicacionTag
from src.modelo.database.db_conexion import get_connection, close_connection

class PublicacionTagsGestor(BaseGestor[PublicacionTag]):
    def __init__(self):
        super().__init__(table_name="publicacion_tag", id_field=None, domain_class=PublicacionTag)

    def agregar(self, obj: PublicacionTag):
        if self.existe((obj.id_publicacion, obj.id_tag)):
            print(f"Error: Ya existe la relación publicacion_tag ({obj.id_publicacion}, {obj.id_tag}).")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"INSERT INTO {self.table_name} (id_publicacion, id_tag) VALUES (?, ?)"
            cursor.execute(query, (obj.id_publicacion, obj.id_tag))
            conn.commit()
            return obj
        except Exception as e:
            print(f"Error al agregar publicacion_tag: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tuple):
        id_publicacion, id_tag = id_tuple
        if not self.existe((id_publicacion, id_tag)):
            print(f"Error: No existe la relación publicacion_tag ({id_publicacion}, {id_tag}).")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_publicacion = ? AND id_tag = ?"
            cursor.execute(query, (id_publicacion, id_tag))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar publicacion_tag: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tuple):
        id_publicacion, id_tag = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_publicacion, id_tag FROM {self.table_name} WHERE id_publicacion = ? AND id_tag = ?"
            cursor.execute(query, (id_publicacion, id_tag))
            row = cursor.fetchone()
            if row:
                return PublicacionTag(*row)
            return None
        except Exception as e:
            print(f"Error al buscar publicacion_tag: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_publicacion, id_tag FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [PublicacionTag(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar publicacion_tag: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, obj):
        print("No se permite actualizar una relación publicacion_tag (clave compuesta).")
        return False

    def existe(self, id_tuple):
        id_publicacion, id_tag = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_publicacion = ? AND id_tag = ?"
            cursor.execute(query, (id_publicacion, id_tag))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de publicacion_tag: {e}")
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
            print(f"Error al contar publicacion_tag: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, publicacion_tag: PublicacionTag) -> str:
        return str(publicacion_tag)