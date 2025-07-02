from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.recurso_multimedia import RecursoMultimedia
from src.modelo.database.db_conexion import get_connection, close_connection

class RecursosMultimedia(BaseGestor[RecursoMultimedia]):
    def __init__(self):
        super().__init__(table_name="recurso_multimedia", id_field="id_recurso_multimedia", domain_class=RecursoMultimedia)

    def agregar(self, recurso: RecursoMultimedia):
        if self.existe(recurso.id_recurso_multimedia):
            print(f"Error: Ya existe un recurso con id_recurso_multimedia={recurso.id_recurso_multimedia}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_recurso_multimedia, tipo, titulo, fecha_subida, autor)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                recurso.id_recurso_multimedia,
                recurso.tipo,
                recurso.titulo,
                recurso.fecha_subida,
                recurso.autor
            ))
            conn.commit()
            return recurso
        except Exception as e:
            print(f"Error al agregar recurso_multimedia: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_recurso_multimedia):
        if not self.existe(id_recurso_multimedia):
            print(f"Error: No existe un recurso con id_recurso_multimedia={id_recurso_multimedia}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_recurso_multimedia = ?"
            cursor.execute(query, (id_recurso_multimedia,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar recurso_multimedia: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_recurso_multimedia):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_recurso_multimedia, tipo, titulo, fecha_subida, autor FROM {self.table_name} WHERE id_recurso_multimedia = ?"
            cursor.execute(query, (id_recurso_multimedia,))
            row = cursor.fetchone()
            if row:
                return RecursoMultimedia(*row)
            return None
        except Exception as e:
            print(f"Error al buscar recurso_multimedia: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_recurso_multimedia, tipo, titulo, fecha_subida, autor FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [RecursoMultimedia(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar recursos_multimedia: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, recurso: RecursoMultimedia):
        if not self.existe(recurso.id_recurso_multimedia):
            print(f"Error: No existe un recurso con id_recurso_multimedia={recurso.id_recurso_multimedia}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET tipo=?, titulo=?, fecha_subida=?, autor=?
                WHERE id_recurso_multimedia=?
            """
            cursor.execute(query, (
                recurso.tipo,
                recurso.titulo,
                recurso.fecha_subida,
                recurso.autor,
                recurso.id_recurso_multimedia
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar recurso_multimedia: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_recurso_multimedia):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_recurso_multimedia = ?"
            cursor.execute(query, (id_recurso_multimedia,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de recurso_multimedia: {e}")
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
            print(f"Error al contar recursos_multimedia: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, recurso: RecursoMultimedia) -> str:
        return str(recurso)
