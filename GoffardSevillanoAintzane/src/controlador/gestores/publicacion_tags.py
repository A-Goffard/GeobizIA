from src.modelo.database.db_conexion import close_connection, get_connection
from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.publicacion_tag import PublicacionTag

class PublicacionTags(BaseGestor[PublicacionTag]):
    def __init__(self):
        # id_field no existe (clave compuesta), pasamos "" para evitar conflictos
        super().__init__(
            table_name="publicacion_tag",
            fields=["id_publicacion", "id_tag"],
            id_field="",  
            domain_class=PublicacionTag
        )

    def agregar(self, **kwargs):
        if "id_publicacion" in kwargs and not self.validar_clave_foranea("id_publicacion", kwargs["id_publicacion"], "publicacion", "id_publicacion"):
            print(f"Error: El id_publicacion {kwargs['id_publicacion']} no existe en la tabla publicacion.")
            return None
        if "id_tag" in kwargs and not self.validar_clave_foranea("id_tag", kwargs["id_tag"], "tag", "id_tag"):
            print(f"Error: El id_tag {kwargs['id_tag']} no existe en la tabla tag.")
            return None
        
        # Construimos el insert manualmente porque no hay id_field ni identidad
        query = f"INSERT INTO {self.table_name} (id_publicacion, id_tag) VALUES (?, ?)"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (kwargs["id_publicacion"], kwargs["id_tag"]))
            conn.commit()
            return PublicacionTag.crear(kwargs["id_publicacion"], kwargs["id_tag"])
        except Exception as e:
            print(f"Error al agregar PublicacionTag: {e}")
            return None
        finally:
            close_connection(conn, cursor)

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
