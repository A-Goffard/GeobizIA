from .base_crud import BaseCRUD
from src.controlador.dominios.tema_ambiental_tag import TemaAmbientalTag

class CrudTemaAmbientalTag(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="tema_ambiental_tag",
            fields=["id_tema_ambiental", "id_tag"],
            id_field=None  # clave compuesta
        )

    def crear(self, id_tema_ambiental, id_tag):
        values = {
            "id_tema_ambiental": id_tema_ambiental,
            "id_tag": id_tag
        }
        return self.insert(values, TemaAmbientalTag)

    def eliminar(self, id_tema_ambiental, id_tag):
        query = f"DELETE FROM {self.table_name} WHERE id_tema_ambiental = ? AND id_tag = ?"
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_tema_ambiental, id_tag))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar TemaAmbientalTag: {e}")
            return False
        finally:
            self.close_connection(conn, cursor)

    def buscar(self, id_tema_ambiental, id_tag):
        query = f"SELECT id_tema_ambiental, id_tag FROM {self.table_name} WHERE id_tema_ambiental = ? AND id_tag = ?"
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_tema_ambiental, id_tag))
            row = cursor.fetchone()
            if row:
                return TemaAmbientalTag.crear(row[0], row[1])
            return None
        except Exception as e:
            print(f"Error al buscar TemaAmbientalTag: {e}")
            return None
        finally:
            self.close_connection(conn, cursor)

    def listar(self):
        return self.select_all(TemaAmbientalTag)
