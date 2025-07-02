from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.generadoria import GeneradorIA
from src.modelo.database.db_conexion import get_connection, close_connection

class GeneradoresIA(BaseGestor[GeneradorIA]):
    def __init__(self):
        super().__init__(table_name="generadoria", id_field="id_generador_ia", domain_class=GeneradorIA)

    def agregar(self, generador: GeneradorIA):
        if self.existe(generador.id_generador_ia):
            print(f"Error: Ya existe un generador con id_generador_ia={generador.id_generador_ia}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                generador.id_generador_ia,
                generador.nombre,
                generador.descripcion,
                generador.empresa_id,
                generador.configuraciones,
                generador.ejemplos_estilo,
                generador.ultima_generacion
            ))
            conn.commit()
            return generador
        except Exception as e:
            print(f"Error al agregar generador: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_generador_ia):
        if not self.existe(id_generador_ia):
            print(f"Error: No existe un generador con id_generador_ia={id_generador_ia}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_generador_ia = ?"
            cursor.execute(query, (id_generador_ia,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar generador: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_generador_ia):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion FROM {self.table_name} WHERE id_generador_ia = ?"
            cursor.execute(query, (id_generador_ia,))
            row = cursor.fetchone()
            if row:
                return GeneradorIA(*row)
            return None
        except Exception as e:
            print(f"Error al buscar generador: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [GeneradorIA(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar generadores: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, generador: GeneradorIA):
        if not self.existe(generador.id_generador_ia):
            print(f"Error: No existe un generador con id_generador_ia={generador.id_generador_ia}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET nombre=?, descripcion=?, empresa_id=?, configuraciones=?, ejemplos_estilo=?, ultima_generacion=?
                WHERE id_generador_ia=?
            """
            cursor.execute(query, (
                generador.nombre,
                generador.descripcion,
                generador.empresa_id,
                generador.configuraciones,
                generador.ejemplos_estilo,
                generador.ultima_generacion,
                generador.id_generador_ia
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar generador: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_generador_ia):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_generador_ia = ?"
            cursor.execute(query, (id_generador_ia,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de generador: {e}")
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
            print(f"Error al contar generadores: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, generador: GeneradorIA) -> str:
        return str(generador)