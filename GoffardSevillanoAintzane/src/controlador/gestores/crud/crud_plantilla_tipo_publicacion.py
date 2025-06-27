from src.controlador.dominios.plantilla_tipo_publicacion import PlantillaTipoPublicacion
from src.controlador.base_crud import BaseCRUD

class CRUDPlantillaTipoPublicacion(BaseCRUD):

    def __init__(self):
        super().__init__("plantilla_tipo_publicacion", ["id_plantilla", "id_tipo_publicacion"])

    def agregar(self, id_plantilla: int, id_tipo_publicacion: int) -> bool:
        sql = """
        INSERT INTO plantilla_tipo_publicacion (id_plantilla, id_tipo_publicacion)
        VALUES (?, ?)
        """
        params = (id_plantilla, id_tipo_publicacion)
        return self.ejecutar_sql(sql, params)

    def actualizar(self, id_plantilla: int, id_tipo_publicacion: int, nuevos_valores: dict) -> bool:
        # No es común actualizar claves primarias en tablas relacionales, 
        # pero si lo necesitas, aquí un ejemplo básico:
        sql = """
        UPDATE plantilla_tipo_publicacion
        SET id_plantilla = ?, id_tipo_publicacion = ?
        WHERE id_plantilla = ? AND id_tipo_publicacion = ?
        """
        params = (
            nuevos_valores.get("id_plantilla", id_plantilla),
            nuevos_valores.get("id_tipo_publicacion", id_tipo_publicacion),
            id_plantilla,
            id_tipo_publicacion
        )
        return self.ejecutar_sql(sql, params)

    def eliminar(self, id_plantilla: int, id_tipo_publicacion: int) -> bool:
        sql = """
        DELETE FROM plantilla_tipo_publicacion
        WHERE id_plantilla = ? AND id_tipo_publicacion = ?
        """
        params = (id_plantilla, id_tipo_publicacion)
        return self.ejecutar_sql(sql, params)

    def buscar(self, clave: tuple) -> PlantillaTipoPublicacion | None:
        sql = """
        SELECT id_plantilla, id_tipo_publicacion
        FROM plantilla_tipo_publicacion
        WHERE id_plantilla = ? AND id_tipo_publicacion = ?
        """
        params = clave
        fila = self.leer_uno(sql, params)
        if fila:
            return PlantillaTipoPublicacion(fila[0], fila[1])
        return None

    def listar(self, filtro: dict = None) -> list[PlantillaTipoPublicacion]:
        sql = "SELECT id_plantilla, id_tipo_publicacion FROM plantilla_tipo_publicacion"
        params = []
        if filtro:
            condiciones = []
            if "id_plantilla" in filtro:
                condiciones.append("id_plantilla = ?")
                params.append(filtro["id_plantilla"])
            if "id_tipo_publicacion" in filtro:
                condiciones.append("id_tipo_publicacion = ?")
                params.append(filtro["id_tipo_publicacion"])
            if condiciones:
                sql += " WHERE " + " AND ".join(condiciones)

        filas = self.leer_varios(sql, tuple(params))
        return [PlantillaTipoPublicacion(f[0], f[1]) for f in filas]
