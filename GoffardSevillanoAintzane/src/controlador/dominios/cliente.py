from abc import ABC, abstractmethod
from .persona import Persona

class Cliente(Persona):
    def __init__(self, id_cliente, nombre, apellido, email, telefono, tipo, direccion, cp, poblacion, pais, fecha_registro):
        super().__init__(id_cliente, nombre, apellido, email, telefono)
        self._id_cliente = id_cliente
        self._tipo = tipo
        self._direccion = direccion
        self._cp = cp
        self._poblacion = poblacion
        self._pais = pais
        self._fecha_registro = fecha_registro

    @property
    def id_cliente(self): return self._id_cliente
    @id_cliente.setter
    def id_cliente(self, id_cliente): self._id_cliente = id_cliente

    @property
    def tipo(self): return self._tipo
    @tipo.setter
    def tipo(self, tipo): self._tipo = tipo

    @property
    def direccion(self): return self._direccion
    @direccion.setter
    def direccion(self, direccion): self._direccion = direccion

    @property
    def cp(self): return self._cp
    @cp.setter
    def cp(self, cp): self._cp = cp

    @property
    def poblacion(self): return self._poblacion
    @poblacion.setter
    def poblacion(self, poblacion): self._poblacion = poblacion

    @property
    def pais(self): return self._pais
    @pais.setter
    def pais(self, pais): self._pais = pais

    @property
    def fecha_registro(self): return self._fecha_registro
    @fecha_registro.setter
    def fecha_registro(self, fecha_registro): self._fecha_registro = fecha_registro

    @abstractmethod
    def get_tipo(self) -> str:
        pass