class GeneradorIA:
    def __init__(self, id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion):
        self._id_generador_ia = id_generador_ia
        self._nombre = nombre
        self._descripcion = descripcion
        self._empresa_id = empresa_id
        self._configuraciones = configuraciones
        self._ejemplos_estilo = ejemplos_estilo
        self._ultima_generacion = ultima_generacion

    @property
    def id_generador_ia(self):
        return self._id_generador_ia

    @id_generador_ia.setter
    def id_generador_ia(self, value):
        self._id_generador_ia = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def empresa_id(self):
        return self._empresa_id

    @empresa_id.setter
    def empresa_id(self, value):
        self._empresa_id = value

    @property
    def configuraciones(self):
        return self._configuraciones

    @configuraciones.setter
    def configuraciones(self, value):
        self._configuraciones = value

    @property
    def ejemplos_estilo(self):
        return self._ejemplos_estilo

    @ejemplos_estilo.setter
    def ejemplos_estilo(self, value):
        self._ejemplos_estilo = value

    @property
    def ultima_generacion(self):
        return self._ultima_generacion

    @ultima_generacion.setter
    def ultima_generacion(self, value):
        self._ultima_generacion = value

    @staticmethod
    def crear(id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion):
        return GeneradorIA(id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion)

    def __str__(self):
        return (
            f"ID: {self.id_generador_ia}, Nombre: {self.nombre or 'N/A'}, "
            f"Descripción: {self.descripcion or 'N/A'}, Empresa ID: {self.empresa_id or 'N/A'}, "
            f"Configuraciones: {self.configuraciones or 'N/A'}, Ejemplos Estilo: {self.ejemplos_estilo or 'N/A'}, "
            f"Última Generación: {self.ultima_generacion or 'N/A'}"
        )