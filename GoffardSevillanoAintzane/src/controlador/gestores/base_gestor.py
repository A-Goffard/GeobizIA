from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class BaseGestor(ABC, Generic[T]):
    def __init__(self, table_name: str, id_field: str, domain_class: type):
        """
        Inicializa el gestor base para operaciones de negocio.

        Args:
            table_name (str): Nombre de la tabla en la base de datos.
            id_field (str): Nombre del campo de clave primaria.
            domain_class (type): Clase del dominio para crear instancias.
        """
        self.table_name = table_name
        self.id_field = id_field
        self.domain_class = domain_class

    @abstractmethod
    def agregar(self, **kwargs) -> Optional[T]:
        """
        Agrega un nuevo registro, aplicando lógica de negocio.

        Args:
            **kwargs: Diccionario con los valores de los campos.

        Returns:
            Optional[T]: Objeto del dominio creado, o None si falla.
        """
        pass

    @abstractmethod
    def eliminar(self, id_value) -> bool:
        """
        Elimina un registro por su ID.

        Args:
            id_value: Valor del campo ID.

        Returns:
            bool: True si se eliminó, False si no.
        """
        pass

    @abstractmethod
    def buscar(self, id_value) -> Optional[T]:
        """
        Busca un registro por su ID.

        Args:
            id_value: Valor del campo ID.

        Returns:
            Optional[T]: Objeto del dominio si se encuentra, o None si no.
        """
        pass

    @abstractmethod
    def mostrar_todos_los_elem(self) -> List[T]:
        """
        Devuelve todos los registros.

        Returns:
            List[T]: Lista de objetos del dominio.
        """
        pass

    @abstractmethod
    def actualizar(self, id_value, **kwargs) -> bool:
        """
        Actualiza un registro existente.

        Args:
            id_value: Valor del campo ID.
            **kwargs: Diccionario con los campos a actualizar.

        Returns:
            bool: True si se actualizó, False si no.
        """
        pass

    @abstractmethod
    def existe(self, id_value) -> bool:
        """
        Verifica si un registro existe por su ID.

        Args:
            id_value: Valor del campo ID.

        Returns:
            bool: True si el registro existe, False si no.
        """
        pass

    @abstractmethod
    def cantidad_elementos(self) -> int:
        """
        Devuelve el número total de registros.

        Returns:
            int: Cantidad de registros.
        """
        pass