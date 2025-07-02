from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.empresa import Empresa
from src.modelo.database.db_conexion import get_connection, close_connection

class Empresas(BaseGestor[Empresa]):
    def __init__(self):
        super().__init__(table_name="empresa", id_field="id_empresa", domain_class=Empresa)

    def agregar(self, empresa: Empresa):
        if self.existe(empresa.id_empresa):
            print(f"Error: Ya existe una empresa con id_empresa={empresa.id_empresa}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_empresa, nombre, sector, logo, ubicacion)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                empresa.id_empresa,
                empresa.nombre,
                empresa.sector,
                empresa.logo,
                empresa.ubicacion
            ))
            conn.commit()
            return empresa
        except Exception as e:
            print(f"Error al agregar empresa: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_empresa):
        if not self.existe(id_empresa):
            print(f"Error: No existe una empresa con id_empresa={id_empresa}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_empresa = ?"
            cursor.execute(query, (id_empresa,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar empresa: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_empresa):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_empresa, nombre, sector, logo, ubicacion FROM {self.table_name} WHERE id_empresa = ?"
            cursor.execute(query, (id_empresa,))
            row = cursor.fetchone()
            if row:
                return Empresa(*row)
            return None
        except Exception as e:
            print(f"Error al buscar empresa: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_empresa, nombre, sector, logo, ubicacion FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Empresa(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar empresas: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, empresa: Empresa):
        if not self.existe(empresa.id_empresa):
            print(f"Error: No existe una empresa con id_empresa={empresa.id_empresa}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET nombre=?, sector=?, logo=?, ubicacion=?
                WHERE id_empresa=?
            """
            cursor.execute(query, (
                empresa.nombre,
                empresa.sector,
                empresa.logo,
                empresa.ubicacion,
                empresa.id_empresa
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar empresa: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_empresa):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_empresa = ?"
            cursor.execute(query, (id_empresa,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de empresa: {e}")
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
            print(f"Error al contar empresas: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, empresa: Empresa) -> str:
        return str(empresa)