from .base_crud import BaseCRUD
from src.controlador.dominios.documento_tag import DocumentoTag

class CrudDocumentoTag(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="documento_tag",
            fields=["id_documento", "id_tag"],
            id_field=None  # clave compuesta
        )

    def crear(self, id_documento, id_tag):
        values = {
            "id_documento": id_documento,
            "id_tag": id_tag
        }
        return self.insert(values, DocumentoTag)

    def eliminar(self, id_documento, id_tag):
        query = f"DELETE FROM {self.table_name} WHERE id_documento = ? AND id_tag = ?"
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_documento, id_tag))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar DocumentoTag: {e}")
            return False
        finally:
            self.close_connection(conn, cursor)

    def buscar(self, id_documento, id_tag):
        query = f"SELECT id_documento, id_tag FROM {self.table_name} WHERE id_documento = ? AND id_tag = ?"
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_documento, id_tag))
            row = cursor.fetchone()
            if row:
                return DocumentoTag.crear(row[0], row[1])
            return None
        except Exception as e:
            print(f"Error al buscar DocumentoTag: {e}")
            return None
        finally:
            self.close_connection(conn, cursor)

    def listar(self):
        return self.select_all(DocumentoTag)
