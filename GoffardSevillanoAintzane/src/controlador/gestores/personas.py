from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.persona import Persona
from src.modelo.database.db_conexion import get_connection, close_connection

class Personas(BaseGestor[Persona]):
    def __init__(self):
        super().__init__(table_name="persona", id_field="id_persona", domain_class=Persona)

    def agregar(self, persona: Persona):
        if self.existe(persona.id_persona):
            print(f"Error: Ya existe una persona con id_persona={persona.id_persona}.")
            return None
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                INSERT INTO {self.table_name} (id_persona, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                persona.id_persona,
                persona.nombre,
                persona.apellido,
                persona.email,
                persona.telefono,
                persona.dni,
                persona.direccion,
                persona.cp,
                persona.poblacion,
                persona.pais
            ))
            conn.commit()
            return persona
        except Exception as e:
            print(f"Error al agregar persona: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def eliminar(self, id_persona):
        if not self.existe(id_persona):
            print(f"Error: No existe una persona con id_persona={id_persona}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_persona = ?"
            cursor.execute(query, (id_persona,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar persona: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def buscar(self, id_persona):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_persona, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais FROM {self.table_name} WHERE id_persona = ?"
            cursor.execute(query, (id_persona,))
            row = cursor.fetchone()
            if row:
                return Persona(*row)
            return None
        except Exception as e:
            print(f"Error al buscar persona: {e}")
            return None
        finally:
            close_connection(conn, cursor)

    def mostrar_todos_los_elem(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT id_persona, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Persona(*row) for row in rows]
        except Exception as e:
            print(f"Error al listar personas: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def actualizar(self, persona: Persona):
        if not self.existe(persona.id_persona):
            print(f"Error: No existe una persona con id_persona={persona.id_persona}.")
            return False
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"""
                UPDATE {self.table_name}
                SET nombre=?, apellido=?, email=?, telefono=?, dni=?, direccion=?, cp=?, poblacion=?, pais=?
                WHERE id_persona=?
            """
            cursor.execute(query, (
                persona.nombre,
                persona.apellido,
                persona.email,
                persona.telefono,
                persona.dni,
                persona.direccion,
                persona.cp,
                persona.poblacion,
                persona.pais,
                persona.id_persona
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar persona: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    def existe(self, id_persona):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = f"SELECT 1 FROM {self.table_name} WHERE id_persona = ?"
            cursor.execute(query, (id_persona,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al comprobar existencia de persona: {e}")
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
            print(f"Error al contar personas: {e}")
            return 0
        finally:
            close_connection(conn, cursor)

    def mostrar_elemento(self, persona: Persona) -> str:
        return str(persona)