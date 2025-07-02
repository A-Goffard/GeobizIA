from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.participante import Participante
from src.modelo.database.db_conexion import get_connection, close_connection

class Participantes(BaseGestor[Participante]):
    def __init__(self):
        super().__init__(table_name="participante", id_field="id_participante", domain_class=Participante)

    def agregar(self, participante: Participante):
        if self.existe(participante.id_participante):
            print(f"Error: Ya existe un participante con id_participante={participante.id_participante}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_participante, id_persona, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                participante.id_participante,
                participante.id_persona,
                participante.numero_personas_juntas,
                participante.rol,
                participante.como_conocer,
                participante.actividad_id,
                participante.fecha_registro
            ))
            conn.commit()
            return participante
        except Exception as e:
            print(f"Error al agregar participante: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_participante):
        if not self.existe(id_participante):
            print(f"Error: No existe un participante con id_participante={id_participante}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_participante = ?"
            cursor.execute(query, (id_participante,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar participante: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_participante):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_participante, id_persona, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro FROM {self.table_name} WHERE id_participante = ?"
            cursor.execute(query, (id_participante,))
            row = cursor.fetchone()
            if row:
                return Participante(*row)
            return None
        except Exception as e:
            print(f"Error al buscar participante: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_participante, id_persona, numero_personas_juntas, rol, como_conocer, actividad_id, fecha_registro FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Participante(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar participantes: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, participante: Participante):
        if not self.existe(participante.id_participante):
            print(f"Error: No existe un participante con id_participante={participante.id_participante}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET id_persona=?, numero_personas_juntas=?, rol=?, como_conocer=?, actividad_id=?, fecha_registro=?
                WHERE id_participante=?
            """
            cursor.execute(query, (
                participante.id_persona,
                participante.numero_personas_juntas,
                participante.rol,
                participante.como_conocer,
                participante.actividad_id,
                participante.fecha_registro,
                participante.id_participante
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar participante: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_participante):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_participante = ?"
            cursor.execute(query, (id_participante,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de participante: {e}")
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
            print(f"Error al contar participantes: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, participante: Participante) -> str:
        return str(participante)