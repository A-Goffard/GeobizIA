from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.proyecto import Proyecto
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Proyectos(BaseGestor[Proyecto]):
    def __init__(self):
        super().__init__(table_name="proyecto", id_field="id_proyecto", domain_class=Proyecto)

    def agregar(self, proyecto: Proyecto):
        if self.existe(proyecto.id_proyecto):
            print(f"Error: Ya existe un proyecto con id_proyecto={proyecto.id_proyecto}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                proyecto.id_proyecto,
                proyecto.nombre,
                proyecto.descripcion,
                proyecto.fecha_inicio,
                proyecto.fecha_fin,
                proyecto.poblacion,
                proyecto.responsable,
                proyecto.estado,
                proyecto.objetivos,
                proyecto.presupuesto
            ))
            conn.commit()
            return proyecto
        except Exception as e:
            print(f"Error al agregar proyecto: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_proyecto):
        if not self.existe(id_proyecto):
            print(f"Error: No existe un proyecto con id_proyecto={id_proyecto}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_proyecto = ?"
            cursor.execute(query, (id_proyecto,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar proyecto: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_proyecto):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto FROM {self.table_name} WHERE id_proyecto = ?"
            cursor.execute(query, (id_proyecto,))
            row = cursor.fetchone()
            if row:
                return Proyecto(*row)
            return None
        except Exception as e:
            print(f"Error al buscar proyecto: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, poblacion, responsable, estado, objetivos, presupuesto FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Proyecto(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar proyectos: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, proyecto: Proyecto):
        if not self.existe(proyecto.id_proyecto):
            print(f"Error: No existe un proyecto con id_proyecto={proyecto.id_proyecto}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET nombre=?, descripcion=?, fecha_inicio=?, fecha_fin=?, poblacion=?, responsable=?, estado=?, objetivos=?, presupuesto=?
                WHERE id_proyecto=?
            """
            cursor.execute(query, (
                proyecto.nombre,
                proyecto.descripcion,
                proyecto.fecha_inicio,
                proyecto.fecha_fin,
                proyecto.poblacion,
                proyecto.responsable,
                proyecto.estado,
                proyecto.objetivos,
                proyecto.presupuesto,
                proyecto.id_proyecto
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar proyecto: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_proyecto):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_proyecto = ?"
            cursor.execute(query, (id_proyecto,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de proyecto: {e}")
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
            print(f"Error al contar proyectos: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, proyecto: Proyecto) -> str:
        return str(proyecto)