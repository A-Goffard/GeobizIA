from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.tag import Tag
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Tags(BaseGestor[Tag]):
    def __init__(self):
        super().__init__(table_name="tag", id_field="id_tag", domain_class=Tag)

    def agregar(self, tag: Tag):
        if self.existe(tag.id_tag):
            print(f"Error: Ya existe un tag con id_tag={tag.id_tag}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_tag, palabra_clave, categoria, frecuencia_uso)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (
                tag.id_tag,
                tag.palabra_clave,
                tag.categoria,
                tag.frecuencia_uso
            ))
            conn.commit()
            return tag
        except Exception as e:
            print(f"Error al agregar tag: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tag):
        if not self.existe(id_tag):
            print(f"Error: No existe un tag con id_tag={id_tag}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_tag = ?"
            cursor.execute(query, (id_tag,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar tag: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tag):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_tag, palabra_clave, categoria, frecuencia_uso FROM {self.table_name} WHERE id_tag = ?"
            cursor.execute(query, (id_tag,))
            row = cursor.fetchone()
            if row:
                return Tag(*row)
            return None
        except Exception as e:
            print(f"Error al buscar tag: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_tag, palabra_clave, categoria, frecuencia_uso FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Tag(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar tags: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, tag: Tag):
        if not self.existe(tag.id_tag):
            print(f"Error: No existe un tag con id_tag={tag.id_tag}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET palabra_clave=?, categoria=?, frecuencia_uso=?
                WHERE id_tag=?
            """
            cursor.execute(query, (
                tag.palabra_clave,
                tag.categoria,
                tag.frecuencia_uso,
                tag.id_tag
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar tag: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_tag):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_tag = ?"
            cursor.execute(query, (id_tag,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de tag: {e}")
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
            print(f"Error al contar tags: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, tag: Tag) -> str:
        return str(tag)
