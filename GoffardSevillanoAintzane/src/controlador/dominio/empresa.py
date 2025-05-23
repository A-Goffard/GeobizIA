class Empresa:
    def __init__(self, id, nombre, sector, valores, objetivos, redes_sociales, logo, ubicacion):
        self._id = id
        self._nombre = nombre
        self._sector = sector
        self._valores = valores
        self._objetivos = objetivos
        self._redes_sociales = redes_sociales
        self._logo = logo
        self._ubicacion = ubicacion

    @staticmethod
    def crear_empresa(id, nombre, sector, valores, objetivos, redes_sociales, logo, ubicacion):
        return Empresa(id, nombre, sector, valores, objetivos, redes_sociales, logo, ubicacion)

    @property
    def id(self): return self._id
    @id.setter
    def id(self, id): self._id = id

    @property
    def nombre(self): return self._nombre
    @nombre.setter
    def nombre(self, nombre): self._nombre = nombre

    @property
    def sector(self): return self._sector
    @sector.setter
    def sector(self, sector): self._sector = sector

    @property
    def valores(self): return self._valores
    @valores.setter
    def valores(self, valores): self._valores = valores

    @property
    def objetivos(self): return self._objetivos
    @objetivos.setter
    def objetivos(self, objetivos): self._objetivos = objetivos

    @property
    def redes_sociales(self): return self._redes_sociales
    @redes_sociales.setter
    def redes_sociales(self, redes_sociales): self._redes_sociales = redes_sociales

    @property
    def logo(self): return self._logo
    @logo.setter
    def logo(self, logo): self._logo = logo

    @property
    def ubicacion(self): return self._ubicacion
    @ubicacion.setter
    def ubicacion(self, ubicacion): self._ubicacion = ubicacion

    def __str__(self):
        return (
            f"ID: {self.id}, Nombre: {self.nombre}, Sector: {self.sector}, "
            f"Valores: {self.valores}, Objetivos: {self.objetivos}, "
            f"Redes sociales: {self.redes_sociales}, Logo: {self.logo}, Ubicación: {self.ubicacion}"
        )
