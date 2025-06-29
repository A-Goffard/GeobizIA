from src.controlador.crud.crud_factura import CrudFactura
from src.controlador.validaciones.validar_factura import validar_datos_factura

class Facturas:
    def __init__(self):
        self.crud = CrudFactura()

    def agregar(self, **kwargs):
        id_factura = kwargs.get("id_factura")
        if id_factura is not None and self.crud.existe(id_factura):
            print(f"Error: Ya existe una factura con id_factura={id_factura}.")
            return None
        valido, msg = validar_datos_factura(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_factura):
        if not self.crud.existe(id_factura):
            print(f"Error: No existe una factura con id_factura={id_factura}.")
            return False
        return self.crud.eliminar(id_factura)

    def buscar(self, id_factura):
        return self.crud.leer(id_factura)

    def actualizar(self, id_factura, **kwargs):
        valido, msg = validar_datos_factura(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_factura, **kwargs)

    def existe(self, id_factura):
        return self.crud.existe(id_factura)

    def listar(self):
        return self.crud.listar()