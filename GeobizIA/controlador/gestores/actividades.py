from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.actividad import Actividad
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Actividades(BaseGestor[Actividad]):
    def __init__(self):
        super().__init__(table_name="actividad", id_field="id_actividad", domain_class=Actividad)

    def agregar(self, actividad: Actividad):
        if self.buscar_por_nombre(actividad.nombre):
            print(f"Error: Ya existe una actividad con nombre={actividad.nombre}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                actividad.tipo,
                actividad.nombre,
                actividad.descripcion,
                actividad.responsable,
                actividad.duracion,
                actividad.coste_economico,
                actividad.coste_horas,
                actividad.facturacion,
                actividad.resultados,
                actividad.valoracion,
                actividad.observaciones
            ))
            conn.commit()
            # Obtener el id generado automáticamente
            cursor.execute("SELECT @@IDENTITY")
            id_generado = int(cursor.fetchone()[0])
            return self.buscar(id_generado)
        except Exception as e:
            print(f"Error al agregar actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def buscar_por_nombre(self, nombre):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones FROM {self.table_name} WHERE nombre = ?"
            cursor.execute(query, (nombre,))
            row = cursor.fetchone()
            if row:
                return Actividad(
                    id_actividad=row[0],
                    tipo=row[1],
                    nombre=row[2],
                    descripcion=row[3],
                    responsable=row[4],
                    duracion=row[5],
                    coste_economico=row[6],
                    coste_horas=row[7],
                    facturacion=row[8],
                    resultados=row[9],
                    valoracion=row[10],
                    observaciones=row[11]
                )
            return None
        except Exception as e:
            print(f"Error al buscar actividad por nombre: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_actividad):
        if not self.existe(id_actividad):
            print(f"Error: No existe una actividad con id_actividad={id_actividad}.")
            return False
        
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # Iniciar transacción
            
            # 1. Eliminar registros dependientes en 'actividad_realizada'
            query_dependientes = "DELETE FROM actividad_realizada WHERE id_actividad = ?"
            cursor.execute(query_dependientes, (id_actividad,))
            
            # 2. Eliminar la actividad principal
            query_principal = f"DELETE FROM {self.table_name} WHERE id_actividad = ?"
            cursor.execute(query_principal, (id_actividad,))
            
            # Confirmar transacción
            conn.commit()
            
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar actividad y sus dependencias: {e}")
            conn.rollback() # Revertir cambios si algo falla
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_actividad):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones FROM {self.table_name} WHERE id_actividad = ?"
            cursor.execute(query, (id_actividad,))
            row = cursor.fetchone()
            if row:
                return Actividad(
                    id_actividad=row[0],
                    tipo=row[1],
                    nombre=row[2],
                    descripcion=row[3],
                    responsable=row[4],
                    duracion=row[5],
                    coste_economico=row[6],
                    coste_horas=row[7],
                    facturacion=row[8],
                    resultados=row[9],
                    valoracion=row[10],
                    observaciones=row[11]
                )
            return None
        except Exception as e:
            print(f"Error al buscar actividad: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_actividad, tipo, nombre, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, observaciones FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            actividades = []
            for row in rows:
                actividades.append(Actividad(
                    id_actividad=row[0],
                    tipo=row[1],
                    nombre=row[2],
                    descripcion=row[3],
                    responsable=row[4],
                    duracion=row[5],
                    coste_economico=row[6],
                    coste_horas=row[7],
                    facturacion=row[8],
                    resultados=row[9],
                    valoracion=row[10],
                    observaciones=row[11]
                ))
            return actividades
        except Exception as e:
            print(f"Error al listar actividades: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, actividad: Actividad):
        if not self.existe(actividad.id_actividad):
            print(f"Error: No existe una actividad con id_actividad={actividad.id_actividad}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET tipo=?, nombre=?, descripcion=?, responsable=?, duracion=?, coste_economico=?, coste_horas=?, facturacion=?, resultados=?, valoracion=?, observaciones=?
                WHERE id_actividad=?
            """
            cursor.execute(query, (
                actividad.tipo,
                actividad.nombre,
                actividad.descripcion,
                actividad.responsable,
                actividad.duracion,
                actividad.coste_economico,
                actividad.coste_horas,
                actividad.facturacion,
                actividad.resultados,
                actividad.valoracion,
                actividad.observaciones,
                actividad.id_actividad
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar actividad: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_actividad):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_actividad = ?"
            cursor.execute(query, (id_actividad,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de actividad: {e}")
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
            print(f"Error al contar actividades: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, actividad: Actividad) -> str:
        return str(actividad)