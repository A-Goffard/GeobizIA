class Cliente:
    def __init__(self, id_cliente, id_persona, tipo=None, razon_social=None, nif=None, fecha_registro=None):
        self._id_cliente = id_cliente
        self._id_persona = id_persona
        self._tipo = tipo
        self._razon_social = razon_social
        self._nif = nif
        self._fecha_registro = fecha_registro

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

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
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    # @staticmethod
    # def crear(id_cliente, id_persona, tipo=None, razon_social=None, nif=None, fecha_registro=None):
    #     return Cliente(id_cliente, id_persona, tipo, razon_social, nif, fecha_registro)

    def __str__(self):
        return f"ID: {self.id_cliente}, ID Persona: {self.id_persona}, Tipo: {self.tipo or 'N/A'}, Razón Social: {self.razon_social or 'N/A'}, NIF: {self.nif or 'N/A'}, Fecha Registro: {self.fecha_registro or 'N/A'}"
    
    def to_dict(self):
        return {
            'id_cliente': self.id_cliente,
            'id_persona': self.id_persona,
            'tipo': self.tipo,
            'razon_social': self.razon_social,
            'nif': self.nif,
            'fecha_registro': self.fecha_registro
        }