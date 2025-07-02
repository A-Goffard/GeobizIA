from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.documento import Documento
from src.modelo.database.db_conexion import get_connection, close_connection

class Documentos(BaseGestor[Documento]):
    def __init__(self):
        super().__init__(table_name="documento", id_field="id_documento", domain_class=Documento)

    def agregar(self, documento: Documento):
        if self.existe(documento.id_documento):
            print(f"Error: Ya existe un documento con id_documento={documento.id_documento}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_documento, titulo, descripcion, fecha_subida, tipo, tematica)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                documento.id_documento,
                documento.titulo,
                documento.descripcion,
                documento.fecha_subida,
                documento.tipo,
                documento.tematica
            ))
            conn.commit()
            return documento
        except Exception as e:
            print(f"Error al agregar documento: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_documento):
        if not self.existe(id_documento):
            print(f"Error: No existe un documento con id_documento={id_documento}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_documento = ?"
            cursor.execute(query, (id_documento,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar documento: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_documento):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_documento, titulo, descripcion, fecha_subida, tipo, tematica FROM {self.table_name} WHERE id_documento = ?"
            cursor.execute(query, (id_documento,))
            row = cursor.fetchone()
            if row:
                return Documento(*row)
            return None
        except Exception as e:
            print(f"Error al buscar documento: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_documento, titulo, descripcion, fecha_subida, tipo, tematica FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Documento(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar documentos: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, documento: Documento):
        if not self.existe(documento.id_documento):
            print(f"Error: No existe un documento con id_documento={documento.id_documento}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET titulo=?, descripcion=?, fecha_subida=?, tipo=?, tematica=?
                WHERE id_documento=?
            """
            cursor.execute(query, (
                documento.titulo,
                documento.descripcion,
                documento.fecha_subida,
                documento.tipo,
                documento.tematica,
                documento.id_documento
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar documento: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_documento):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_documento = ?"
            cursor.execute(query, (id_documento,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de documento: {e}")
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
            print(f"Error al contar documentos: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, documento: Documento) -> str:
        return str(documento)