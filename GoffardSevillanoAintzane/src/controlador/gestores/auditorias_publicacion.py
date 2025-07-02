from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.auditoria_publicacion import AuditoriaPublicacion
from src.modelo.database.db_conexion import get_connection, close_connection

class AuditoriasPublicacion(BaseGestor[AuditoriaPublicacion]):
    def __init__(self):
        super().__init__(table_name="auditoria_publicacion", id_field="id_auditoria_publicacion", domain_class=AuditoriaPublicacion)

    def agregar(self, auditoria: AuditoriaPublicacion):
        if self.existe(auditoria.id_auditoria_publicacion):
            print(f"Error: Ya existe una auditoría con id={auditoria.id_auditoria_publicacion}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_auditoria_publicacion, publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                auditoria.id_auditoria_publicacion,
                auditoria.publicacion_id,
                auditoria.generador_ia_id,
                auditoria.fecha_generacion,
                auditoria.usuario_id,
                auditoria.parametros_entrada,
                auditoria.resultado,
                auditoria.observaciones
            ))
            conn.commit()
            return auditoria
        except Exception as e:
            print(f"Error al agregar auditoría: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_auditoria):
        if not self.existe(id_auditoria):
            print(f"Error: No existe una auditoría con id={id_auditoria}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_auditoria_publicacion = ?"
            cursor.execute(query, (id_auditoria,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar auditoría: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_auditoria):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_auditoria_publicacion, publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones FROM {self.table_name} WHERE id_auditoria_publicacion = ?"
            cursor.execute(query, (id_auditoria,))
            row = cursor.fetchone()
            if row:
                return AuditoriaPublicacion(*row)
            return None
        except Exception as e:
            print(f"Error al buscar auditoría: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_auditoria_publicacion, publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [AuditoriaPublicacion(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar auditorías: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, auditoria: AuditoriaPublicacion):
        if not self.existe(auditoria.id_auditoria_publicacion):
            print(f"Error: No existe una auditoría con id={auditoria.id_auditoria_publicacion}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET publicacion_id=?, generador_ia_id=?, fecha_generacion=?, usuario_id=?, parametros_entrada=?, resultado=?, observaciones=?
                WHERE id_auditoria_publicacion=?
            """
            cursor.execute(query, (
                auditoria.publicacion_id,
                auditoria.generador_ia_id,
                auditoria.fecha_generacion,
                auditoria.usuario_id,
                auditoria.parametros_entrada,
                auditoria.resultado,
                auditoria.observaciones,
                auditoria.id_auditoria_publicacion
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar auditoría: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_auditoria):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_auditoria_publicacion = ?"
            cursor.execute(query, (id_auditoria,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de auditoría: {e}")
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
            print(f"Error al contar auditorías: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, auditoria: AuditoriaPublicacion) -> str:
        return str(auditoria)