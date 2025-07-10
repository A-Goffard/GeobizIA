from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.tema_ambiental import TemaAmbiental
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class TemasAmbientales(BaseGestor[TemaAmbiental]):
    def __init__(self):
        super().__init__(table_name="tema_ambiental", id_field="id_tema_ambiental", domain_class=TemaAmbiental)

    def agregar(self, tema: TemaAmbiental):
        if self.existe(tema.id_tema_ambiental):
            print(f"Error: Ya existe un tema ambiental con id_tema_ambiental={tema.id_tema_ambiental}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_tema_ambiental, nombre, descripcion, relevancia)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (
                tema.id_tema_ambiental,
                tema.nombre,
                tema.descripcion,
                tema.relevancia
            ))
            conn.commit()
            return tema
        except Exception as e:
            print(f"Error al agregar tema_ambiental: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_tema_ambiental):
        if not self.existe(id_tema_ambiental):
            print(f"Error: No existe un tema ambiental con id_tema_ambiental={id_tema_ambiental}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_tema_ambiental = ?"
            cursor.execute(query, (id_tema_ambiental,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar tema_ambiental: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_tema_ambiental):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_tema_ambiental, nombre, descripcion, relevancia FROM {self.table_name} WHERE id_tema_ambiental = ?"
            cursor.execute(query, (id_tema_ambiental,))
            row = cursor.fetchone()
            if row:
                return TemaAmbiental(
                    id_tema_ambiental=row[0],
                    nombre=row[1],
                    descripcion=row[2],
                    relevancia=row[3]
                )
            return None
        except Exception as e:
            print(f"Error al buscar tema_ambiental: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_tema_ambiental, nombre, descripcion, relevancia FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [TemaAmbiental(
                id_tema_ambiental=row[0],
                nombre=row[1],
                descripcion=row[2],
                relevancia=row[3]
            ) for row in rows]
        except Exception as e:
            print(f"Error al listar temas_ambientales: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, tema: TemaAmbiental):
        if not self.existe(tema.id_tema_ambiental):
            print(f"Error: No existe un tema ambiental con id_tema_ambiental={tema.id_tema_ambiental}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET nombre=?, descripcion=?, relevancia=?
                WHERE id_tema_ambiental=?
            """
            cursor.execute(query, (
                tema.nombre,
                tema.descripcion,
                tema.relevancia,
                tema.id_tema_ambiental
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar tema_ambiental: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_tema_ambiental):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_tema_ambiental = ?"
            cursor.execute(query, (id_tema_ambiental,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de tema_ambiental: {e}")
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
            print(f"Error al contar temas_ambientales: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, tema: TemaAmbiental) -> str:
        return str(tema)