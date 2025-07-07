from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.documento_tag import DocumentoTag
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class DocumentosTagGestor(BaseGestor[DocumentoTag]):
    def __init__(self):
        super().__init__(table_name="documento_tag", id_field=None, domain_class=DocumentoTag)

    def agregar(self, documento_tag: DocumentoTag):
        if self.existe((documento_tag.id_documento, documento_tag.id_tag)):
            print(f"Error: Ya existe la relación documento_tag ({documento_tag.id_documento}, {documento_tag.id_tag}).")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"INSERT INTO {self.table_name} (id_documento, id_tag) VALUES (?, ?)"
            cursor.execute(query, (documento_tag.id_documento, documento_tag.id_tag))
            conn.commit()
            return documento_tag
        except Exception as e:
            print(f"Error al agregar documento_tag: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tuple):
        id_documento, id_tag = id_tuple
        if not self.existe((id_documento, id_tag)):
            print(f"Error: No existe la relación documento_tag ({id_documento}, {id_tag}).")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_documento = ? AND id_tag = ?"
            cursor.execute(query, (id_documento, id_tag))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar documento_tag: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tuple):
        id_documento, id_tag = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_documento, id_tag FROM {self.table_name} WHERE id_documento = ? AND id_tag = ?"
            cursor.execute(query, (id_documento, id_tag))
            row = cursor.fetchone()
            if row:
                return DocumentoTag(*row)
            return None
        except Exception as e:
            print(f"Error al buscar documento_tag: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_documento, id_tag FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [DocumentoTag(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar documento_tag: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, obj):
        print("No se permite actualizar una relación documento_tag (clave compuesta).")
        return False

    def existe(self, id_tuple):
        id_documento, id_tag = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_documento = ? AND id_tag = ?"
            cursor.execute(query, (id_documento, id_tag))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de documento_tag: {e}")
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
            print(f"Error al contar documento_tag: {e}")
            return 0
        finally:
            close_connection(conn, cursor)
