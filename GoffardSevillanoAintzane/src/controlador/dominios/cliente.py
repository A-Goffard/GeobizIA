from abc import ABC, abstractmethod
from .persona import Persona

class Cliente(Persona):
    def __init__(self, id_cliente, id_persona, tipo, razon_social, nif, fecha_registro, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais):
        super().__init__(id_persona, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais)
        self._id_cliente = id_cliente
        self._tipo = tipo
        self._razon_social = razon_social
        self._nif = nif
        self._fecha_registro = fecha_registro

    @staticmethod
    def crear_cliente(id_cliente, id_persona, tipo, razon_social, nif, fecha_registro, nombre, apellido, email, telefono, dni, direccion, cp, poblacion, pais):
        return Cliente(
            id_cliente=id_cliente,
            id_persona=id_persona,
            tipo=tipo,
            razon_social=razon_social,
            nif=nif,
            fecha_registro=fecha_registro,
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            dni=dni,
            direccion=direccion,
            cp=cp,
            poblacion=poblacion,
            pais=pais
        )

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
    def fecha_registro(self): return self._fecha_registro
    @fecha_registro.setter
    def fecha_registro(self, fecha_registro): self._fecha_registro = fecha_registro

    @abstractmethod
    def get_tipo(self) -> str:
        pass

    def get_tipo(self) -> str:
        return "Cliente"

    def __str__(self):
        return (
            f"ID Cliente: {self.id_cliente}, ID Persona: {self.id_persona}, Tipo: {self.tipo}, "
            f"Razón social: {self.razon_social}, NIF: {self.nif}, Fecha registro: {self.fecha_registro}, "
            f"{super().__str__()}"
        )