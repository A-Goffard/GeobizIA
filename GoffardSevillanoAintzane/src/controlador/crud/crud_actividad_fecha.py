# from .base_crud import BaseCRUD
# from src.controlador.dominios.actividad_fecha import ActividadFecha
# from src.modelo.database.db_conexion import get_connection, close_connection

# class CrudActividadFecha(BaseCRUD):
#     def __init__(self):
#         super().__init__(
#             table_name="actividad_fecha",
#             fields=["id_actividad", "id_fecha"],
#             id_field=None  # clave compuesta
#         )

#     def crear(self, id_actividad, id_fecha):
#         values = {
#             "id_actividad": id_actividad,
#             "id_fecha": id_fecha
#         }
#         return self.insert(values, ActividadFecha)

#     def eliminar(self, id_actividad, id_fecha):
#         query = f"DELETE FROM {self.table_name} WHERE id_actividad = ? AND id_fecha = ?"
#         conn = get_connection()
#         cursor = conn.cursor()
#         try:
#             cursor.execute(query, (id_actividad, id_fecha))
#             conn.commit()
#             return cursor.rowcount > 0
#         except Exception as e:
#             print(f"Error al eliminar ActividadFecha: {e}")
#             return False
#         finally:
#             close_connection(conn, cursor)

#     def buscar(self, id_actividad, id_fecha):
#         query = f"SELECT id_actividad, id_fecha FROM {self.table_name} WHERE id_actividad = ? AND id_fecha = ?"
#         conn = get_connection()
#         cursor = conn.cursor()
#         try:
#             cursor.execute(query, (id_actividad, id_fecha))
#             row = cursor.fetchone()
#             if row:
#                 return ActividadFecha.crear(row[0], row[1])
#             return None
#         except Exception as e:
#             print(f"Error al buscar ActividadFecha: {e}")
#             return None
#         finally:
#             close_connection(conn, cursor)

#     def listar(self):
#         return self.select_all(ActividadFecha)
