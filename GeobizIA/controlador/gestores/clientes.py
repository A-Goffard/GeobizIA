from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.cliente import Cliente
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Clientes(BaseGestor[Cliente]):
    def __init__(self):
        super().__init__(table_name="cliente", id_field="id_cliente", domain_class=Cliente)

    def agregar(self, cliente: Cliente):
        if self.existe(cliente.id_cliente):
            print(f"Error: Ya existe un cliente con id_cliente={cliente.id_cliente}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_cliente, id_persona, tipo, razon_social, nif, fecha_registro)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                cliente.id_cliente,
                cliente.id_persona,
                cliente.tipo,
                cliente.razon_social,
                cliente.nif,
                cliente.fecha_registro
            ))
            conn.commit()
            return cliente
        except Exception as e:
            print(f"Error al agregar cliente: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_cliente):
        if not self.existe(id_cliente):
            print(f"Error: No existe un cliente con id_cliente={id_cliente}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_cliente = ?"
            cursor.execute(query, (id_cliente,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_cliente):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_cliente, id_persona, tipo, razon_social, nif, fecha_registro FROM {self.table_name} WHERE id_cliente = ?"
            cursor.execute(query, (id_cliente,))
            row = cursor.fetchone()
            if row:
                return Cliente(*row)
            return None
        except Exception as e:
            print(f"Error al buscar cliente: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_cliente, id_persona, tipo, razon_social, nif, fecha_registro FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Cliente(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar clientes: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, cliente: Cliente):
        if not self.existe(cliente.id_cliente):
            print(f"Error: No existe un cliente con id_cliente={cliente.id_cliente}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET id_persona=?, tipo=?, razon_social=?, nif=?, fecha_registro=?
                WHERE id_cliente=?
            """
            cursor.execute(query, (
                cliente.id_persona,
                cliente.tipo,
                cliente.razon_social,
                cliente.nif,
                cliente.fecha_registro,
                cliente.id_cliente
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_cliente):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_cliente = ?"
            cursor.execute(query, (id_cliente,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de cliente: {e}")
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
            print(f"Error al contar clientes: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, cliente: Cliente) -> str:
        return str(cliente)