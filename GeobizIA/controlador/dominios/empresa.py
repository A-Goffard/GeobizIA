class Empresa:
    def __init__(self, id_empresa, nombre, sector, logo, ubicacion):
        self._id_empresa = id_empresa
        self._nombre = nombre
        self._sector = sector
        self._logo = logo
        self._ubicacion = ubicacion

    @property
    def id_empresa(self):
        return self._id_empresa

    @id_empresa.setter
    def id_empresa(self, id_empresa):
        self._id_empresa = id_empresa

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def sector(self):
        return self._sector

    @sector.setter
    def sector(self, sector):
        self._sector = sector

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, logo):
        self._logo = logo

    @property
    def ubicacion(self):
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    # @staticmethod
    # def crear(id_empresa, nombre, sector, logo, ubicacion):
    #     return Empresa(id_empresa, nombre, sector, logo, ubicacion)

    def __str__(self):
        return f"ID: {self.id_empresa}, Nombre: {self.nombre}, Sector: {self.sector}, Logo: {self.logo}, Ubicación: {self.ubicacion}"