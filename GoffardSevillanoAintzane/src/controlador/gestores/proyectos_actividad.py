from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.proyecto_actividad import ProyectoActividad

class ProyectosActividad(BaseGestor[ProyectoActividad]):
    def __init__(self):
        super().__init__(
            table_name="proyecto_actividad",
            fields=["proyecto_id", "actividad_id"],
            id_field=None,  # No hay id único simple
            domain_class=ProyectoActividad
        )

    def agregar(self, proyecto_id, actividad_id):
        # Validar claves foráneas
        if not self.validar_clave_foranea("proyecto_id", proyecto_id, "proyecto", "id_proyecto"):
            print(f"Error: El proyecto_id {proyecto_id} no existe en la tabla proyecto.")
            return None
        if not self.validar_clave_foranea("actividad_id", actividad_id, "actividad", "id_actividad"):
            print(f"Error: El actividad_id {actividad_id} no existe en la tabla actividad.")
            return None

        sql = f"INSERT INTO {self.table_name} (proyecto_id, actividad_id) VALUES (?, ?)"
        try:
            self.cursor.execute(sql, (proyecto_id, actividad_id))
            self.conexion.commit()
            return ProyectoActividad.crear(proyecto_id, actividad_id)
        except Exception as e:
            print(f"Error al agregar: {e}")
            return None

    def eliminar(self, proyecto_id, actividad_id):
        sql = f"DELETE FROM {self.table_name} WHERE proyecto_id = ? AND actividad_id = ?"
        try:
            self.cursor.execute(sql, (proyecto_id, actividad_id))
            self.conexion.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False

    def buscar(self, proyecto_id, actividad_id):
        sql = f"SELECT proyecto_id, actividad_id FROM {self.table_name} WHERE proyecto_id = ? AND actividad_id = ?"
        self.cursor.execute(sql, (proyecto_id, actividad_id))
        row = self.cursor.fetchone()
        if row:
            return ProyectoActividad.crear(row[0], row[1])
        return None

    def listar_por_proyecto(self, proyecto_id):
        sql = f"SELECT proyecto_id, actividad_id FROM {self.table_name} WHERE proyecto_id = ?"
        self.cursor.execute(sql, (proyecto_id,))
        rows = self.cursor.fetchall()
        return [ProyectoActividad.crear(row[0], row[1]) for row in rows]

    # actualizar no tiene sentido aquí porque la clave primaria son ambas columnas,
    # si quisieras cambiar algo, eliminar y agregar otro registro.

