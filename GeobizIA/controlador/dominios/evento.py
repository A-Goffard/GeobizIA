class Evento:
    def __init__(self, id_evento=None, nombre=None, tipo=None, lugar=None, fecha_comienzo=None, fecha_final=None, poblacion=None, tematica=None):
        self._id_evento = id_evento
        self._nombre = nombre
        self._tipo = tipo
        self._lugar = lugar
        self._fecha_comienzo = fecha_comienzo
        self._fecha_final = fecha_final
        self._poblacion = poblacion
        self._tematica = tematica

    @property
    def id_evento(self):
        return self._id_evento

    @id_evento.setter
    def id_evento(self, id_evento):
        self._id_evento = id_evento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def lugar(self):
        return self._lugar

    @lugar.setter
    def lugar(self, lugar):
        self._lugar = lugar

    @property
    def fecha_comienzo(self):
        return self._fecha_comienzo

    @fecha_comienzo.setter
    def fecha_comienzo(self, fecha_comienzo):
        self._fecha_comienzo = fecha_comienzo

    @property
    def fecha_final(self):
        return self._fecha_final

    @fecha_final.setter
    def fecha_final(self, fecha_final):
        self._fecha_final = fecha_final

    @property
    def poblacion(self):
        return self._poblacion

    @poblacion.setter
    def poblacion(self, poblacion):
        self._poblacion = poblacion

    @property
    def tematica(self):
        return self._tematica

    @tematica.setter
    def tematica(self, tematica):
        self._tematica = tematica

    # @staticmethod
    # def crear(id_evento, nombre=None, tipo=None, lugar=None, fecha_comienzo=None, fecha_final=None, poblacion=None, tematica=None):
    #     return Evento(id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica)

    def __str__(self):
        return (
            f"ID: {self.id_evento}, Nombre: {self.nombre or 'N/A'}, Tipo: {self.tipo or 'N/A'}, "
            f"Lugar: {self.lugar or 'N/A'}, Fecha Comienzo: {self.fecha_comienzo or 'N/A'}, "
            f"Fecha Final: {self.fecha_final or 'N/A'}, Población: {self.poblacion or 'N/A'}, "
            f"Temática: {self.tematica or 'N/A'}"
        )
        
    def to_dict(self):
        return {
            "id_evento": self.id_evento,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "lugar": self.lugar,
            "fecha_comienzo": self.fecha_comienzo,
            "fecha_final": self.fecha_final,
            "poblacion": self.poblacion,
            "tematica": self.tematica
        }
