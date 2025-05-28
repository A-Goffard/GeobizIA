from .cliente import Cliente

class Fisica(Cliente):
    def __init__(self, id, nombre, apellido, email, telefono, tipo, direccion, cp, poblacion, pais, fecha_registro, dni, fecha_nacimiento):
        super().__init__(id, nombre, apellido, email, telefono, tipo, direccion, cp, poblacion, pais, fecha_registro)
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def dni(self): return self._dni
    @dni.setter
    def dni(self, dni): self._dni = dni

    @property
    def fecha_nacimiento(self): return self._fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento): self._fecha_nacimiento = fecha_nacimiento

    def get_tipo(self):
        return "Fisica"

    def __str__(self):
        return (
            f"ID: {self.id}, Tipo: {self.tipo}, DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellido}, "
            f"Dirección: {self.direccion}, CP: {self.cp}, Población: {self.poblacion}, País: {self.pais}, "
            f"Fecha nacimiento: {self.fecha_nacimiento}, Email: {self.email}, Teléfono: {self.telefono}, "
            f"Fecha registro: {self.fecha_registro}"
        )
