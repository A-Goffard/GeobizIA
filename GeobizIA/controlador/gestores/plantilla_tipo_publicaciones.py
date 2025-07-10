from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.plantilla_tipo_publicacion import PlantillaTipoPublicacion
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class PlantillaTipoPublicacionesGestor(BaseGestor[PlantillaTipoPublicacion]):
    def __init__(self):
        super().__init__(table_name="plantilla_tipo_publicacion", id_field=None, domain_class=PlantillaTipoPublicacion)

    def agregar(self, obj: PlantillaTipoPublicacion):
        if self.existe((obj.id_plantilla, obj.id_tipo_publicacion)):
            print(f"Error: Ya existe la relación plantilla_tipo_publicacion ({obj.id_plantilla}, {obj.id_tipo_publicacion}).")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"INSERT INTO {self.table_name} (id_plantilla, id_tipo_publicacion) VALUES (?, ?)"
            cursor.execute(query, (obj.id_plantilla, obj.id_tipo_publicacion))
            conn.commit()
            return obj
        except Exception as e:
            print(f"Error al agregar plantilla_tipo_publicacion: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tuple):
        id_plantilla, id_tipo_publicacion = id_tuple
        if not self.existe((id_plantilla, id_tipo_publicacion)):
            print(f"Error: No existe la relación plantilla_tipo_publicacion ({id_plantilla}, {id_tipo_publicacion}).")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_plantilla = ? AND id_tipo_publicacion = ?"
            cursor.execute(query, (id_plantilla, id_tipo_publicacion))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar plantilla_tipo_publicacion: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tuple):
        id_plantilla, id_tipo_publicacion = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_plantilla, id_tipo_publicacion FROM {self.table_name} WHERE id_plantilla = ? AND id_tipo_publicacion = ?"
            cursor.execute(query, (id_plantilla, id_tipo_publicacion))
            row = cursor.fetchone()
            if row:
                return PlantillaTipoPublicacion(
                    id_plantilla=row[0],
                    id_tipo_publicacion=row[1]
                )
            return None
        except Exception as e:
            print(f"Error al buscar plantilla_tipo_publicacion: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_plantilla, id_tipo_publicacion FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [PlantillaTipoPublicacion(
                id_plantilla=row[0],
                id_tipo_publicacion=row[1]
            ) for row in rows]
        except Exception as e:
            print(f"Error al listar plantilla_tipo_publicacion: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, obj):
        print("No se permite actualizar una relación plantilla_tipo_publicacion (clave compuesta).")
        return False

    def existe(self, id_tuple):
        id_plantilla, id_tipo_publicacion = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_plantilla = ? AND id_tipo_publicacion = ?"
            cursor.execute(query, (id_plantilla, id_tipo_publicacion))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de plantilla_tipo_publicacion: {e}")
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
            print(f"Error al contar plantilla_tipo_publicacion: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, obj: PlantillaTipoPublicacion) -> str:
        return str(obj)
