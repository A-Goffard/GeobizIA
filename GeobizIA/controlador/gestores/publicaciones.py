from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.publicacion import Publicacion
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Publicaciones(BaseGestor[Publicacion]):
    def __init__(self):
        super().__init__(table_name="publicacion", id_field="id_publicacion", domain_class=Publicacion)

    def agregar(self, publicacion: Publicacion):
        if self.existe(publicacion.id_publicacion):
            print(f"Error: Ya existe una publicación con id_publicacion={publicacion.id_publicacion}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia, id_generador_ia, feedback_empresa, id_tipo_publicacion, id_plantilla)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                publicacion.id_publicacion,
                publicacion.titulo,
                publicacion.contenido,
                publicacion.autor,
                publicacion.fecha_creacion,
                publicacion.estado,
                publicacion.tags,
                publicacion.palabras_clave,
                publicacion.generada_por_ia,
                publicacion.id_generador_ia,
                publicacion.feedback_empresa,
                publicacion.id_tipo_publicacion,
                publicacion.id_plantilla
            ))
            conn.commit()
            return publicacion
        except Exception as e:
            print(f"Error al agregar publicación: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_publicacion):
        if not self.existe(id_publicacion):
            print(f"Error: No existe una publicación con id_publicacion={id_publicacion}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_publicacion = ?"
            cursor.execute(query, (id_publicacion,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar publicación: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_publicacion):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia, id_generador_ia, feedback_empresa, id_tipo_publicacion, id_plantilla FROM {self.table_name} WHERE id_publicacion = ?"
            cursor.execute(query, (id_publicacion,))
            row = cursor.fetchone()
            if row:
                return Publicacion(
                    id_publicacion=row[0],
                    titulo=row[1],
                    contenido=row[2],
                    autor=row[3],
                    fecha_creacion=row[4],
                    estado=row[5],
                    tags=row[6],
                    palabras_clave=row[7],
                    generada_por_ia=row[8],
                    id_generador_ia=row[9],
                    feedback_empresa=row[10],
                    id_tipo_publicacion=row[11],
                    id_plantilla=row[12]
                )
            return None
        except Exception as e:
            print(f"Error al buscar publicación: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_publicacion, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave, generada_por_ia, id_generador_ia, feedback_empresa, id_tipo_publicacion, id_plantilla FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Publicacion(
                id_publicacion=row[0],
                titulo=row[1],
                contenido=row[2],
                autor=row[3],
                fecha_creacion=row[4],
                estado=row[5],
                tags=row[6],
                palabras_clave=row[7],
                generada_por_ia=row[8],
                id_generador_ia=row[9],
                feedback_empresa=row[10],
                id_tipo_publicacion=row[11],
                id_plantilla=row[12]
            ) for row in rows]
        except Exception as e:
            print(f"Error al listar publicaciones: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, publicacion: Publicacion):
        if not self.existe(publicacion.id_publicacion):
            print(f"Error: No existe una publicación con id_publicacion={publicacion.id_publicacion}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET titulo=?, contenido=?, autor=?, fecha_creacion=?, estado=?, tags=?, palabras_clave=?, generada_por_ia=?, id_generador_ia=?, feedback_empresa=?, id_tipo_publicacion=?, id_plantilla=?
                WHERE id_publicacion=?
            """
            cursor.execute(query, (
                publicacion.titulo,
                publicacion.contenido,
                publicacion.autor,
                publicacion.fecha_creacion,
                publicacion.estado,
                publicacion.tags,
                publicacion.palabras_clave,
                publicacion.generada_por_ia,
                publicacion.id_generador_ia,
                publicacion.feedback_empresa,
                publicacion.id_tipo_publicacion,
                publicacion.id_plantilla,
                publicacion.id_publicacion
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar publicación: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_publicacion):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_publicacion = ?"
            cursor.execute(query, (id_publicacion,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de publicación: {e}")
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
            print(f"Error al contar publicaciones: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, publicacion: Publicacion) -> str:
        return str(publicacion)