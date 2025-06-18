class Evento:
    def __init__(self, id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica):
        self._id_evento = id_evento
        self._nombre = nombre
        self._tipo = tipo
        self._lugar = lugar
        self._fecha_comienzo = fecha_comienzo
        self._fecha_final = fecha_final
        self._poblacion = poblacion
        self._tematica = tematica

    @staticmethod
    def crear_evento(id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica):
        return Evento(id_evento, nombre, tipo, lugar, fecha_comienzo, fecha_final, poblacion, tematica)

    @property
    def id_evento(self): return self._id_evento
    @id_evento.setter
    def id_evento(self, id_evento): self._id_evento = id_evento

    @property
    def nombre(self): return self._nombre
    @nombre.setter
    def nombre(self, nombre): self._nombre = nombre

    @property
    def tipo(self): return self._tipo
    @tipo.setter
    def tipo(self, tipo): self._tipo = tipo

    @property
    def lugar(self): return self._lugar
    @lugar.setter
    def lugar(self, lugar): self._lugar = lugar

    @property
    def fecha_comienzo(self): return self._fecha_comienzo
    @fecha_comienzo.setter
    def fecha_comienzo(self, fecha_comienzo): self._fecha_comienzo = fecha_comienzo

    @property
    def fecha_final(self): return self._fecha_final
    @fecha_final.setter
    def fecha_final(self, fecha_final): self._fecha_final = fecha_final

    @property
    def poblacion(self): return self._poblacion
    @poblacion.setter
    def poblacion(self, poblacion): self._poblacion = poblacion

    @property
    def tematica(self): return self._tematica
    @tematica.setter
    def tematica(self, tematica): self._tematica = tematica

    def __str__(self):
        return (
            f"ID: {self.id_evento}, Nombre: {self.nombre}, Tipo: {self.tipo}, Lugar: {self.lugar}, "
            f"Fecha comienzo: {self.fecha_comienzo}, Fecha final: {self.fecha_final}, "
            f"Población: {self.poblacion}, Temática: {self.tematica}"
        )
