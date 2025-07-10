from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.factura import Factura
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Facturas(BaseGestor[Factura]):
    def __init__(self):
        super().__init__(table_name="factura", id_field="id_factura", domain_class=Factura)

    def agregar(self, factura: Factura):
        # Para SQL Server con columna IDENTITY, no incluir id_factura en el INSERT
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_cliente, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            cursor.execute(query, (
                factura.id_cliente,
                factura.tipo,
                factura.nombre,
                factura.direccion,
                factura.nif,
                factura.fecha_facturacion,
                factura.fecha_vencimiento,
                factura.concepto,
                factura.responsable,
                factura.iva,
                factura.coste_total,
                factura.base_imponible,
                factura.numero_factura,
                factura.tipo_pago,
                factura.irpf
            ))
            
            # Obtener el ID generado por IDENTITY
            cursor.execute("SELECT @@IDENTITY")
            nuevo_id = cursor.fetchone()[0]
            factura.id_factura = int(nuevo_id)
            
            conn.commit()
            return factura
        except Exception as e:
            print(f"Error al agregar factura: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_factura):
        if not self.existe(id_factura):
            print(f"Error: No existe una factura con id_factura={id_factura}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_factura = ?"
            cursor.execute(query, (id_factura,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar factura: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_factura):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_factura, id_cliente, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf FROM {self.table_name} WHERE id_factura = ?"
            cursor.execute(query, (id_factura,))
            row = cursor.fetchone()
            if row:
                return Factura(
                    id_factura=row[0],
                    id_cliente=row[1],
                    tipo=row[2],
                    nombre=row[3],
                    direccion=row[4],
                    nif=row[5],
                    fecha_facturacion=row[6],
                    fecha_vencimiento=row[7],
                    concepto=row[8],
                    responsable=row[9],
                    iva=row[10],
                    coste_total=row[11],
                    base_imponible=row[12],
                    numero_factura=row[13],
                    tipo_pago=row[14],
                    irpf=row[15]
                )
            return None
        except Exception as e:
            print(f"Error al buscar factura: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_factura, id_cliente, tipo, nombre, direccion, nif, fecha_facturacion, fecha_vencimiento, concepto, responsable, iva, coste_total, base_imponible, numero_factura, tipo_pago, irpf FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Factura(
                id_factura=row[0],
                id_cliente=row[1],
                tipo=row[2],
                nombre=row[3],
                direccion=row[4],
                nif=row[5],
                fecha_facturacion=row[6],
                fecha_vencimiento=row[7],
                concepto=row[8],
                responsable=row[9],
                iva=row[10],
                coste_total=row[11],
                base_imponible=row[12],
                numero_factura=row[13],
                tipo_pago=row[14],
                irpf=row[15]
            ) for row in rows]
        except Exception as e:
            print(f"Error al listar facturas: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, factura: Factura):
        if not self.existe(factura.id_factura):
            print(f"Error: No existe una factura con id_factura={factura.id_factura}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET id_cliente=?, tipo=?, nombre=?, direccion=?, nif=?, fecha_facturacion=?, fecha_vencimiento=?, concepto=?, responsable=?, iva=?, coste_total=?, base_imponible=?, numero_factura=?, tipo_pago=?, irpf=?
                WHERE id_factura=?
            """
            cursor.execute(query, (
                factura.id_cliente,
                factura.tipo,
                factura.nombre,
                factura.direccion,
                factura.nif,
                factura.fecha_facturacion,
                factura.fecha_vencimiento,
                factura.concepto,
                factura.responsable,
                factura.iva,
                factura.coste_total,
                factura.base_imponible,
                factura.numero_factura,
                factura.tipo_pago,
                factura.irpf,
                factura.id_factura
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar factura: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_factura):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_factura = ?"
            cursor.execute(query, (id_factura,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de factura: {e}")
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
            print(f"Error al contar facturas: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, factura: Factura) -> str:
        return str(factura)