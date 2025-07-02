from .base_crud import BaseCRUD
from src.controlador.dominios.plantilla_tipo_publicacion import PlantillaTipoPublicacion
from src.modelo.database.db_conexion import get_connection, close_connection

class CrudPlantillaTipoPublicacion(BaseCRUD):
    def __init__(self):
        table_name = "plantilla_tipo_publicacion"
        fields = ["id_plantilla", "id_tipo_publicacion"]
        id_field = None  # No hay clave primaria simple, es compuesta
        super().__init__(table_name, fields, id_field)

    def crear(self, id_plantilla, id_tipo_publicacion):
        values = {
            "id_plantilla": id_plantilla,
            "id_tipo_publicacion": id_tipo_publicacion
        }
        # Pasa la clase de dominio correctamente
        res = self.insert(values, PlantillaTipoPublicacion)
        return res

    def eliminar(self, id_plantilla, id_tipo_publicacion):
        query = f"DELETE FROM {self.table_name} WHERE id_plantilla = ? AND id_tipo_publicacion = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_plantilla, id_tipo_publicacion))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar PlantillaTipoPublicacion: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_plantilla, id_tipo_publicacion):
        query = f"SELECT id_plantilla, id_tipo_publicacion FROM {self.table_name} WHERE id_plantilla = ? AND id_tipo_publicacion = ?"
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, (id_plantilla, id_tipo_publicacion))
            row = cursor.fetchone()
            if row:
                return PlantillaTipoPublicacion(row[0], row[1])
            return None
        except Exception as e:
            print(f"Error al buscar PlantillaTipoPublicacion: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def listar(self, filtro: dict = None) -> list[PlantillaTipoPublicacion]:
        sql = "SELECT id_plantilla, id_tipo_publicacion FROM plantilla_tipo_publicacion"
        params = []
        if filtro:
            condiciones = []
            if "id_plantilla" in filtro:
                condiciones.append("id_plantilla = ?")
                params.append(filtro["id_plantilla"])
            if "id_tipo_publicacion" in filtro:
                condiciones.append("id_tipo_publicacion = ?")
                params.append(filtro["id_tipo_publicacion"])
            if condiciones:
                sql += " WHERE " + " AND ".join(condiciones)

        filas = self.leer_varios(sql, tuple(params))
        return [PlantillaTipoPublicacion(f[0], f[1]) for f in filas]
        filas = self.leer_varios(sql, tuple(params))
        return [PlantillaTipoPublicacion(f[0], f[1]) for f in filas]
