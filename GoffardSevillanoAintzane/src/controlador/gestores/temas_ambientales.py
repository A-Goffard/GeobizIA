from src.controlador.gestores.base_gestor import BaseGestor
from src.controlador.dominios.tema_ambiental import Tema_Ambiental
from src.controlador.crud.crud_tema_ambiental import CrudTemaAmbiental
from src.controlador.validaciones.validar_tema_ambiental import validar_datos_tema_ambiental

class Temas_Ambientales(BaseGestor[Tema_Ambiental]):
    def __init__(self):
        super().__init__(
            table_name="tema_ambiental",
            id_field="id_tema_ambiental",
            domain_class=Tema_Ambiental
        )
        self.crud = CrudTemaAmbiental()

    def agregar(self, **kwargs) -> Tema_Ambiental:

        id_tema_ambiental = kwargs.get("id_tema_ambiental")
        if id_tema_ambiental is not None and self.crud.existe(id_tema_ambiental):
            print(f"Error: Ya existe un tema_ambiental con id_tema_ambiental={id_tema_ambiental}.")
            return None
        valido, msg = validar_datos_tema_ambiental(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return None
        return self.crud.crear(**kwargs)

    def eliminar(self, id_value) -> bool:
  
        if not self.crud.existe(id_value):
            print(f"Error: No existe un tema_ambiental con id_tema_ambiental={id_value}.")
            return False
        return self.crud.eliminar(id_value)

    def buscar(self, id_value) -> Tema_Ambiental:
 
        return self.crud.leer(id_value)

    def mostrar_todos_los_elem(self) -> list[Tema_Ambiental]:
  
        return self.crud.listar()

    def actualizar(self, id_value, **kwargs) -> bool:
   
        valido, msg = validar_datos_tema_ambiental(kwargs)
        if not valido:
            print(f"Error: {msg}")
            return False
        return self.crud.actualizar(id_value, **kwargs)

    def existe(self, id_value) -> bool:

        return self.crud.existe(id_value)

    def cantidad_elementos(self) -> int:

        return self.crud.contar()