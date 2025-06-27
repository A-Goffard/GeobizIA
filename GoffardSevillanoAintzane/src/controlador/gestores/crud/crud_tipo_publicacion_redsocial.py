from src.controlador.dominios.tipo_publicacion_redsocial import TipoPublicacionRedSocial
from src.controlador.base_crud import BaseCRUD

class CRUDTipoPublicacionRedSocial(BaseCRUD):

    def __init__(self):
        super().__init__("tipo_publicacion_redsocial", ["id_tipo_publicacion", "id_red_social"])

    def agregar(self, id_tipo_publicacion: int, id_red_social: int) -> bool:
        sql = """
        INSERT INTO tipo_publicacion_redsocial (id_tipo_publicacion, id_red_social)
        VALUES (?, ?)
        """
        params = (id_tipo_publicacion, id_red_social)
        return self.ejecutar_sql(sql, params)

    def actualizar(self, id_tipo_publicacion: int, id_red_social: int, nuevos_valores: dict) -> bool:
        # Actualizar claves primarias es poco común, pero aquí un ejemplo si se requiere:
        sql = """
        UPDATE tipo_publicacion_redsocial
        SET id_tipo_publicacion = ?, id_red_social = ?
        WHERE id_tipo_publicacion = ? AND id_red_social = ?
        """
        params = (
            nuevos_valores.get("id_tipo_publicacion", id_tipo_publicacion),
            nuevos_valores.get("id_red_social", id_red_social),
            id_tipo_publicacion,
            id_red_social
        )
        return self.ejecutar_sql(sql, params)

    def eliminar(self, id_tipo_publicacion: int, id_red_social: int) -> bool:
        sql = """
        DELETE FROM tipo_publicacion_redsocial
        WHERE id_tipo_publicacion = ? AND id_red_social = ?
        """
        params = (id_tipo_publicacion, id_red_social)
        return self.ejecutar_sql(sql, params)

    def buscar(self, clave: tuple) -> TipoPublicacionRedSocial | None:
        sql = """
        SELECT id_tipo_publicacion, id_red_social
        FROM tipo_publicacion_redsocial
        WHERE id_tipo_publicacion = ? AND id_red_social = ?
        """
        params = clave
        fila = self.leer_uno(sql, params)
        if fila:
            return TipoPublicacionRedSocial(fila[0], fila[1])
        return None

    def listar(self, filtro: dict = None) -> list[TipoPublicacionRedSocial]:
        sql = "SELECT id_tipo_publicacion, id_red_social FROM tipo_publicacion_redsocial"
        params = []
        if filtro:
            condiciones = []
            if "id_tipo_publicacion" in filtro:
                condiciones.append("id_tipo_publicacion = ?")
                params.append(filtro["id_tipo_publicacion"])
            if "id_red_social" in filtro:
                condiciones.append("id_red_social = ?")
                params.append(filtro["id_red_social"])
            if condiciones:
                sql += " WHERE " + " AND ".join(condiciones)

        filas = self.leer_varios(sql, tuple(params))
        return [TipoPublicacionRedSocial(f[0], f[1]) for f in filas]
