from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.evento import Evento
from src.modelo.database.db_conexion import get_connection, close_connection

class Eventos(BaseGestor[Evento]):
    def __init__(self):
        super().__init__(table_name="evento", id_field="id_evento", domain_class=Evento)

    def agregar(self, evento: Evento):
        if self.existe(evento.id_evento):
            print(f"Error: Ya existe un evento con id_evento={evento.id_evento}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                evento.id_evento,
                evento.nombre,
                evento.tipo,
                evento.lugar,
                evento.fecha_comienzo,
                evento.fecha_final,
                evento.poblacion,
                evento.tematica
            ))
            conn.commit()
            return evento
        except Exception as e:
            print(f"Error al agregar evento: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_evento):
        if not self.existe(id_evento):
            print(f"Error: No existe un evento con id_evento={id_evento}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_evento = ?"
            cursor.execute(query, (id_evento,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar evento: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_evento):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica FROM {self.table_name} WHERE id_evento = ?"
            cursor.execute(query, (id_evento,))
            row = cursor.fetchone()
            if row:
                return Evento(*row)
            return None
        except Exception as e:
            print(f"Error al buscar evento: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Evento(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar eventos: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, evento: Evento):
        if not self.existe(evento.id_evento):
            print(f"Error: No existe un evento con id_evento={evento.id_evento}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET nombre=?, tipo=?, lugar=?, fecha_comienzo=?, fecha_final=?, poblacion=?, tematica=?
                WHERE id_evento=?
            """
            cursor.execute(query, (
                evento.nombre,
                evento.tipo,
                evento.lugar,
                evento.fecha_comienzo,
                evento.fecha_final,
                evento.poblacion,
                evento.tematica,
                evento.id_evento
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar evento: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_evento):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_evento = ?"
            cursor.execute(query, (id_evento,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de evento: {e}")
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
            print(f"Error al contar eventos: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, evento: Evento) -> str:
        return str(evento)