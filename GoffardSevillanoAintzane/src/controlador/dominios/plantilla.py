class Plantilla:
    def __init__(self, id_plantilla, titulo=None, tipo=None, contenido_base=None, fecha_creacion=None, ultima_modificacion=None):
        self._id_plantilla = id_plantilla
        self._titulo = titulo
        self._tipo = tipo
        self._contenido_base = contenido_base
        self._fecha_creacion = fecha_creacion
        self._ultima_modificacion = ultima_modificacion

    @property
    def id_plantilla(self):
        return self._id_plantilla

    @id_plantilla.setter
    def id_plantilla(self, id_plantilla):
        self._id_plantilla = id_plantilla

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def contenido_base(self):
        return self._contenido_base

    @contenido_base.setter
    def contenido_base(self, contenido_base):
        self._contenido_base = contenido_base

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion):
        self._fecha_creacion = fecha_creacion

    @property
    def ultima_modificacion(self):
        return self._ultima_modificacion

    @ultima_modificacion.setter
    def ultima_modificacion(self, ultima_modificacion):
        self._ultima_modificacion = ultima_modificacion

    # @staticmethod
    # def crear(id_plantilla, titulo=None, tipo=None, contenido_base=None, fecha_creacion=None, ultima_modificacion=None):
    #     return Plantilla(id_plantilla, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion)

    def __str__(self):
        return (
            f"ID: {self.id_plantilla}, Título: {self.titulo or 'N/A'}, Tipo: {self.tipo or 'N/A'}, "
            f"Contenido base: {self.contenido_base or 'N/A'}, Fecha creación: {self.fecha_creacion or 'N/A'}, "
            f"Última modificación: {self.ultima_modificacion or 'N/A'}"
        )