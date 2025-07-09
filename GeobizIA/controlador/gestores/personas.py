from GeobizIA.controlador.gestores.base_gestor import BaseGestor
from GeobizIA.controlador.dominios.persona import Persona
from GeobizIA.modelo.database.db_conexion import get_connection, close_connection

class Personas(BaseGestor[Persona]):
    def __init__(self):
        super().__init__(table_name="persona", id_field="id_persona", domain_class=Persona)

    def agregar(self, persona: Persona):
        # La comprobación de existencia por ID no es necesaria para un nuevo registro con IDENTITY.
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # --- AJUSTE CLAVE: Usar OUTPUT para obtener el ID en una sola consulta ---
            query = f"""
                INSERT INTO {self.table_name} (nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais)
                OUTPUT INSERTED.id_persona
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            # Se ejecuta la consulta y se obtiene el ID directamente.
            last_id = cursor.execute(query, (
                persona.nombre,
                persona.apellido,
                persona.email,
                persona.telefono,
                persona.dni,
                persona.direccion,
                persona.cp,
                persona.poblacion,
                persona.pais
            )).fetchval()
            
            conn.commit()
            
            if last_id is not None:
                persona.id_persona = last_id
                return persona
            else:
                # Si no se obtiene un ID, algo falló.
                raise Exception("La consulta INSERT no devolvió un ID.")

        except Exception as e:
            # --- MEJORA DE DIAGNÓSTICO ---
            print(f"----------- ERROR EN GESTOR DE PERSONAS AL AGREGAR -----------")
            print(f"Error de base de datos: {e}")
            print(f"Datos que se intentaron insertar: {persona}")
            print(f"-----------------------------------------------------------")
            conn.rollback() # Deshacer cambios si hay un error
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
                return Persona(
                    id_persona=row[0],
                    nombre=row[1],
                    apellido=row[2],
                    email=row[3],
                    telefono=row[4],
                    dni=row[5],
                    direccion=row[6],
                    cp=row[7],
                    poblacion=row[8],
                    pais=row[9]
                )
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
            personas = []
            for row in rows:
                personas.append(Persona(
                    id_persona=row[0],
                    nombre=row[1],
                    apellido=row[2],
                    email=row[3],
                    telefono=row[4],
                    dni=row[5],
                    direccion=row[6],
                    cp=row[7],
                    poblacion=row[8],
                    pais=row[9]
                ))
            return personas
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