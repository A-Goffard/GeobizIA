from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.redsocial import RedSocial
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class RedesSociales(BaseGestor[RedSocial]):
    def __init__(self):
        super().__init__(table_name="redsocial", id_field="id_red_social", domain_class=RedSocial)

    def agregar(self, red: RedSocial):
        if self.existe(red.id_red_social):
            print(f"Error: Ya existe una red social con id_red_social={red.id_red_social}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                red.id_red_social,
                red.plataforma,
                red.nombre_cuenta,
                red.credenciales,
                red.preferencias_publicacion,
                red.estado_conexion,
                red.ultima_publicacion
            ))
            conn.commit()
            return red
        except Exception as e:
            print(f"Error al agregar red social: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_red_social):
        if not self.existe(id_red_social):
            print(f"Error: No existe una red social con id_red_social={id_red_social}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_red_social = ?"
            cursor.execute(query, (id_red_social,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar red social: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_red_social):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion FROM {self.table_name} WHERE id_red_social = ?"
            cursor.execute(query, (id_red_social,))
            row = cursor.fetchone()
            if row:
                return RedSocial(*row)
            return None
        except Exception as e:
            print(f"Error al buscar red social: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_red_social, plataforma, nombre_cuenta, credenciales, preferencias_publicacion, estado_conexion, ultima_publicacion FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [RedSocial(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar redes sociales: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, red: RedSocial):
        if not self.existe(red.id_red_social):
            print(f"Error: No existe una red social con id_red_social={red.id_red_social}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET plataforma=?, nombre_cuenta=?, credenciales=?, preferencias_publicacion=?, estado_conexion=?, ultima_publicacion=?
                WHERE id_red_social=?
            """
            cursor.execute(query, (
                red.plataforma,
                red.nombre_cuenta,
                red.credenciales,
                red.preferencias_publicacion,
                red.estado_conexion,
                red.ultima_publicacion,
                red.id_red_social
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar red social: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_red_social):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_red_social = ?"
            cursor.execute(query, (id_red_social,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de red social: {e}")
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
            print(f"Error al contar redes sociales: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, red: RedSocial) -> str:
        return str(red)
