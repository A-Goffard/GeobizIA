from .base_crud import BaseCRUD
from src.controlador.dominios.factura_actividad import FacturaActividad

class CrudFacturaActividad(BaseCRUD):
    def __init__(self):
        super().__init__(
            table_name="factura_actividad",
            fields=["id_factura", "id_actividad"],
            id_field=None  # clave compuesta
        )

    def crear(self, id_factura, id_actividad):
        values = {
            "id_factura": id_factura,
            "id_actividad": id_actividad
        }
        return self.insert(values, FacturaActividad)

    def eliminar(self, id_factura, id_actividad):
        query = f"DELETE FROM {self.table_name} WHERE id_factura = ? AND id_actividad = ?"
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_factura, id_actividad))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar FacturaActividad: {e}")
            return False
        finally:
            self.close_connection(conn, cursor)

    def buscar(self, id_factura, id_actividad):
        query = f"SELECT id_factura, id_actividad FROM {self.table_name} WHERE id_factura = ? AND id_actividad = ?"
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_factura, id_actividad))
            row = cursor.fetchone()
            if row:
                return FacturaActividad.crear(row[0], row[1])
            return None
        except Exception as e:
            print(f"Error al buscar FacturaActividad: {e}")
            return None
        finally:
            self.close_connection(conn, cursor)

    def listar(self):
        return self.select_all(FacturaActividad)
