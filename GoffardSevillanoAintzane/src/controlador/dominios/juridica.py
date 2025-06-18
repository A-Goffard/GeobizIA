from .cliente import Cliente

class Juridica(Cliente):
    def __init__(self, id_cliente, nombre, apellido, email, telefono, tipo, direccion, cp, poblacion, pais, fecha_registro, nif):
        super().__init__(id_cliente, nombre, apellido, email, telefono, tipo, direccion, cp, poblacion, pais, fecha_registro)
        self._id_cliente = id_cliente
        self._nif = nif

    @property
    def id_cliente(self): return self._id_cliente
    @id_cliente.setter
    def id_cliente(self, id_cliente): self._id_cliente = id_cliente

    @property
    def nif(self): return self._nif
    @nif.setter
    def nif(self, nif): self._nif = nif

    def get_tipo(self):
        return "Juridica"

    def __str__(self):
        return (
            f"ID: {self.id_cliente}, Tipo: {self.tipo}, Nombre: {self.nombre}, NIF: {self.nif}, "
            f"Dirección: {self.direccion}, CP: {self.cp}, Población: {self.poblacion}, País: {self.pais}, "
            f"Email: {self.email}, Teléfono: {self.telefono}, Fecha registro: {self.fecha_registro}"
        )
