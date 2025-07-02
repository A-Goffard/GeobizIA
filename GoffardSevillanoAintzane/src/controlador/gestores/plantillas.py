from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.plantilla import Plantilla
from src.modelo.database.db_conexion import get_connection, close_connection

class Plantillas(BaseGestor[Plantilla]):
    def __init__(self):
        super().__init__(table_name="plantilla", id_field="id_plantilla", domain_class=Plantilla)

    def agregar(self, plantilla: Plantilla):
        if self.existe(plantilla.id_plantilla):
            print(f"Error: Ya existe una plantilla con id_plantilla={plantilla.id_plantilla}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_plantilla, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                plantilla.id_plantilla,
                plantilla.titulo,
                plantilla.tipo,
                plantilla.contenido_base,
                plantilla.fecha_creacion,
                plantilla.ultima_modificacion
            ))
            conn.commit()
            return plantilla
        except Exception as e:
            print(f"Error al agregar plantilla: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_plantilla):
        if not self.existe(id_plantilla):
            print(f"Error: No existe una plantilla con id_plantilla={id_plantilla}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_plantilla = ?"
            cursor.execute(query, (id_plantilla,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar plantilla: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_plantilla):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_plantilla, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion FROM {self.table_name} WHERE id_plantilla = ?"
            cursor.execute(query, (id_plantilla,))
            row = cursor.fetchone()
            if row:
                return Plantilla(*row)
            return None
        except Exception as e:
            print(f"Error al buscar plantilla: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_plantilla, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Plantilla(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar plantillas: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, plantilla: Plantilla):
        if not self.existe(plantilla.id_plantilla):
            print(f"Error: No existe una plantilla con id_plantilla={plantilla.id_plantilla}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET titulo=?, tipo=?, contenido_base=?, fecha_creacion=?, ultima_modificacion=?
                WHERE id_plantilla=?
            """
            cursor.execute(query, (
                plantilla.titulo,
                plantilla.tipo,
                plantilla.contenido_base,
                plantilla.fecha_creacion,
                plantilla.ultima_modificacion,
                plantilla.id_plantilla
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar plantilla: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_plantilla):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_plantilla = ?"
            cursor.execute(query, (id_plantilla,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de plantilla: {e}")
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
            print(f"Error al contar plantillas: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, plantilla: Plantilla) -> str:
        return str(plantilla)