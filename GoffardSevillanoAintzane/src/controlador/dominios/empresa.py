class Empresa:
    def __init__(self, id_empresa, id_persona, razon_social=None, nif=None, sector=None, tamano=None, fecha_registro=None):
        self._id_empresa = id_empresa
        self._id_persona = id_persona
        self._razon_social = razon_social
        self._nif = nif
        self._sector = sector
        self._tamano = tamano
        self._fecha_registro = fecha_registro

    @property
    def id_empresa(self):
        return self._id_empresa

    @id_empresa.setter
    def id_empresa(self, id_empresa):
        self._id_empresa = id_empresa

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def razon_social(self):
        return self._razon_social

    @razon_social.setter
    def razon_social(self, razon_social):
        self._razon_social = razon_social

    @property
    def nif(self):
        return self._nif

    @nif.setter
    def nif(self, nif):
        self._nif = nif

    @property
    def sector(self):
        return self._sector

    @sector.setter
    def sector(self, sector):
        self._sector = sector

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    @staticmethod
    def crear(id_empresa, id_persona, razon_social=None, nif=None, sector=None, tamano=None, fecha_registro=None):
        return Empresa(id_empresa, id_persona, razon_social, nif, sector, tamano, fecha_registro)

    def __str__(self):
        return f"ID: {self.id_empresa}, ID Persona: {self.id_persona}, Razón Social: {self.razon_social or 'N/A'}, NIF: {self.nif or 'N/A'}, Sector: {self.sector or 'N/A'}, Tamaño: {self.tamano or 'N/A'}, Fecha Registro: {self.fecha_registro or 'N/A'}"