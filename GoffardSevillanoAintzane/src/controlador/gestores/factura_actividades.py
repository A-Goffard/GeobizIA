from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.factura_actividad import FacturaActividad
from src.modelo.database.db_conexion import get_connection, close_connection

class FacturaActividadGestor(BaseGestor[FacturaActividad]):
    def __init__(self):
        super().__init__(table_name="factura_actividad", id_field=None, domain_class=FacturaActividad)

    def agregar(self, factura_actividad: FacturaActividad):
        if self.existe((factura_actividad.id_factura, factura_actividad.id_actividad)):
            print(f"Error: Ya existe la relación factura_actividad ({factura_actividad.id_factura}, {factura_actividad.id_actividad}).")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"INSERT INTO {self.table_name} (id_factura, id_actividad) VALUES (?, ?)"
            cursor.execute(query, (factura_actividad.id_factura, factura_actividad.id_actividad))
            conn.commit()
            return factura_actividad
        except Exception as e:
            print(f"Error al agregar factura_actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tuple):
        id_factura, id_actividad = id_tuple
        if not self.existe((id_factura, id_actividad)):
            print(f"Error: No existe la relación factura_actividad ({id_factura}, {id_actividad}).")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_factura = ? AND id_actividad = ?"
            cursor.execute(query, (id_factura, id_actividad))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar factura_actividad: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tuple):
        id_factura, id_actividad = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_factura, id_actividad FROM {self.table_name} WHERE id_factura = ? AND id_actividad = ?"
            cursor.execute(query, (id_factura, id_actividad))
            row = cursor.fetchone()
            if row:
                return FacturaActividad(*row)
            return None
        except Exception as e:
            print(f"Error al buscar factura_actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_factura, id_actividad FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [FacturaActividad(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar factura_actividad: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, obj):
        print("No se permite actualizar una relación factura_actividad (clave compuesta).")
        return False

    def existe(self, id_tuple):
        id_factura, id_actividad = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_factura = ? AND id_actividad = ?"
            cursor.execute(query, (id_factura, id_actividad))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de factura_actividad: {e}")
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
            print(f"Error al contar factura_actividad: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, factura_actividad: FacturaActividad) -> str:
        return str(factura_actividad)
