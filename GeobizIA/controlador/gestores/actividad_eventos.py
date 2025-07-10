from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.actividad_evento import ActividadEvento
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class ActividadEventosGestor(BaseGestor[ActividadEvento]):
    def __init__(self):
        super().__init__(table_name="actividad_evento", id_field=None, domain_class=ActividadEvento)

    def agregar(self, actividad_evento: ActividadEvento):
        if self.existe((actividad_evento.id_actividad, actividad_evento.id_evento)):
            print(f"Error: Ya existe la relación actividad_evento ({actividad_evento.id_actividad}, {actividad_evento.id_evento}).")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"INSERT INTO {self.table_name} (id_actividad, id_evento) VALUES (?, ?)"
            cursor.execute(query, (actividad_evento.id_actividad, actividad_evento.id_evento))
            conn.commit()
            return actividad_evento
        except Exception as e:
            print(f"Error al agregar actividad_evento: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tuple):
        id_actividad, id_evento = id_tuple
        if not self.existe((id_actividad, id_evento)):
            print(f"Error: No existe la relación actividad_evento ({id_actividad}, {id_evento}).")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_actividad = ? AND id_evento = ?"
            cursor.execute(query, (id_actividad, id_evento))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar actividad_evento: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tuple):
        id_actividad, id_evento = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad, id_evento FROM {self.table_name} WHERE id_actividad = ? AND id_evento = ?"
            cursor.execute(query, (id_actividad, id_evento))
            row = cursor.fetchone()
            if row:
                return ActividadEvento(
                    id_actividad=row[0],
                    id_evento=row[1]
                )
            return None
        except Exception as e:
            print(f"Error al buscar actividad_evento: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad, id_evento FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            actividades_eventos = []
            for row in rows:
                actividades_eventos.append(ActividadEvento(
                    id_actividad=row[0],
                    id_evento=row[1]
                ))
            return actividades_eventos
        except Exception as e:
            print(f"Error al listar actividad_evento: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, actividad_evento: ActividadEvento):
        print("No se permite actualizar una relación actividad_evento (clave compuesta).")
        return False

    def existe(self, id_tuple):
        id_actividad, id_evento = id_tuple
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_actividad = ? AND id_evento = ?"
            cursor.execute(query, (id_actividad, id_evento))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de actividad_evento: {e}")
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
            print(f"Error al contar actividad_evento: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, actividad_evento: ActividadEvento) -> str:
        return str(actividad_evento)
