from abc import ABC, abstractmethod
from .persona import Persona

class Cliente(Persona):
    def __init__(self, id_cliente, tipo, nombre, apellido, razon_social, nif, dni, email, telefono, direccion, cp, poblacion, pais, fecha_registro):
        super().__init__(id_cliente, nombre, apellido, email, telefono)
        self._id_cliente = id_cliente
        self._tipo = tipo
        self._razon_social = razon_social
        self._nif = nif
        self._dni = dni
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
    def razon_social(self): return self._razon_social
    @razon_social.setter
    def razon_social(self, razon_social): self._razon_social = razon_social

    @property
    def nif(self): return self._nif
    @nif.setter
    def nif(self, nif): self._nif = nif

    @property
    def dni(self): return self._dni
    @dni.setter
    def dni(self, dni): self._dni = dni

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