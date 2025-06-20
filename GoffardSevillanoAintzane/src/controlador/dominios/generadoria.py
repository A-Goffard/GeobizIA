class GeneradorIA:
    def __init__(self, id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion):
        self._id_generador_ia = id_generador_ia
        self._nombre = nombre
        self._descripcion = descripcion
        self._empresa_id = empresa_id
        self._configuraciones = configuraciones
        self._ejemplos_estilo = ejemplos_estilo
        self._ultima_generacion = ultima_generacion

    @staticmethod
    def crear_generador_ia(id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion):
        return GeneradorIA(id_generador_ia, nombre, descripcion, empresa_id, configuraciones, ejemplos_estilo, ultima_generacion)

    @property
    def id_generador_ia(self): return self._id_generador_ia
    @id_generador_ia.setter
    def id_generador_ia(self, id_generador_ia): self._id_generador_ia = id_generador_ia

    @property
    def nombre(self): return self._nombre
    @nombre.setter
    def nombre(self, nombre): self._nombre = nombre

    @property
    def descripcion(self): return self._descripcion
    @descripcion.setter
    def descripcion(self, descripcion): self._descripcion = descripcion

    @property
    def empresa_id(self): return self._empresa_id
    @empresa_id.setter
    def empresa_id(self, empresa_id): self._empresa_id = empresa_id

    @property
    def configuraciones(self): return self._configuraciones
    @configuraciones.setter
    def configuraciones(self, configuraciones): self._configuraciones = configuraciones

    @property
    def ejemplos_estilo(self): return self._ejemplos_estilo
    @ejemplos_estilo.setter
    def ejemplos_estilo(self, ejemplos_estilo): self._ejemplos_estilo = ejemplos_estilo

    @property
    def ultima_generacion(self): return self._ultima_generacion
    @ultima_generacion.setter
    def ultima_generacion(self, ultima_generacion): self._ultima_generacion = ultima_generacion

    def __str__(self):
        return (
            f"ID: {self.id_generador_ia}, Nombre: {self.nombre}, Descripción: {self.descripcion}, "
            f"Empresa ID: {self.empresa_id}, Configuraciones: {self.configuraciones}, "
            f"Ejemplos estilo: {self.ejemplos_estilo}, Última generación: {self.ultima_generacion}"
        )
