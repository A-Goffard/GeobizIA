from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.cliente import Cliente
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Clientes(BaseGestor[Cliente]):
    def __init__(self):
        super().__init__(table_name="cliente", id_field="id_cliente", domain_class=Cliente)

    def agregar(self, cliente: Cliente):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # Insertar y obtener el ID generado automáticamente en una sola consulta
            query = f"""
                INSERT INTO {self.table_name} (id_persona, tipo, razon_social, nif, fecha_registro)
                OUTPUT INSERTED.id_cliente
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                cliente.id_persona,
                cliente.tipo,
                cliente.razon_social,
                cliente.nif,
                cliente.fecha_registro
            ))
            
            # Obtener el ID generado automáticamente
            result = cursor.fetchone()
            if result and result[0]:
                nuevo_id = int(result[0])
                cliente.id_cliente = nuevo_id
                conn.commit()
                return cliente
            else:
                raise Exception("No se pudo obtener el ID generado automáticamente")
        except Exception as e:
            print(f"Error al agregar cliente: {e}")
            conn.rollback()
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
                return Cliente(
                    id_cliente=row[0],
                    id_persona=row[1],
                    tipo=row[2],
                    razon_social=row[3],
                    nif=row[4],
                    fecha_registro=row[5]
                )
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
            clientes = []
            for row in rows:
                clientes.append(Cliente(
                    id_cliente=row[0],
                    id_persona=row[1],
                    tipo=row[2],
                    razon_social=row[3],
                    nif=row[4],
                    fecha_registro=row[5]
                ))
            return clientes
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