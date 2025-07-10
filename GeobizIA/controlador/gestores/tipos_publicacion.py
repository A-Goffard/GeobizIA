from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.tipo_publicacion import TipoPublicacion
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class TiposPublicacion(BaseGestor[TipoPublicacion]):
    def __init__(self):
        super().__init__(table_name="tipo_publicacion", id_field="id_tipo_publicacion", domain_class=TipoPublicacion)

    def agregar(self, tipo: TipoPublicacion):
        if self.existe(tipo.id_tipo_publicacion):
            print(f"Error: Ya existe un tipo_publicacion con id_tipo_publicacion={tipo.id_tipo_publicacion}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_tipo_publicacion, nombre)
                VALUES (?, ?)
            """
            cursor.execute(query, (
                tipo.id_tipo_publicacion,
                tipo.nombre
            ))
            conn.commit()
            return tipo
        except Exception as e:
            print(f"Error al agregar tipo_publicacion: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tipo_publicacion):
        if not self.existe(id_tipo_publicacion):
            print(f"Error: No existe un tipo_publicacion con id_tipo_publicacion={id_tipo_publicacion}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_tipo_publicacion = ?"
            cursor.execute(query, (id_tipo_publicacion,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar tipo_publicacion: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tipo_publicacion):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_tipo_publicacion, nombre FROM {self.table_name} WHERE id_tipo_publicacion = ?"
            cursor.execute(query, (id_tipo_publicacion,))
            row = cursor.fetchone()
            if row:
                return TipoPublicacion(
                    id_tipo_publicacion=row[0],
                    nombre=row[1]
                )
            return None
        except Exception as e:
            print(f"Error al buscar tipo_publicacion: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_tipo_publicacion, nombre FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [TipoPublicacion(
                id_tipo_publicacion=row[0],
                nombre=row[1]
            ) for row in rows]
        except Exception as e:
            print(f"Error al listar tipos_publicacion: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, tipo: TipoPublicacion):
        if not self.existe(tipo.id_tipo_publicacion):
            print(f"Error: No existe un tipo_publicacion con id_tipo_publicacion={tipo.id_tipo_publicacion}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET nombre=?
                WHERE id_tipo_publicacion=?
            """
            cursor.execute(query, (
                tipo.nombre,
                tipo.id_tipo_publicacion
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar tipo_publicacion: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_tipo_publicacion):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_tipo_publicacion = ?"
            cursor.execute(query, (id_tipo_publicacion,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de tipo_publicacion: {e}")
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
            print(f"Error al contar tipos_publicacion: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, tipo: TipoPublicacion) -> str:
        return str(tipo)