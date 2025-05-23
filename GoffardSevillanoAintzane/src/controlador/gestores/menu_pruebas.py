import sys
import os
from importlib import import_module
from base_gestor import BaseGestor

# Añadir el directorio raíz del proyecto al sys.path para imports relativos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Item:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}"

class Gestor(BaseGestor):
    pass

def solicitar_atributos(clase, opcional=False):
    atributos = {}
    parametros = clase.__init__.__code__.co_varnames[1:clase.__init__.__code__.co_argcount]
    for atributo in parametros:
        valor = input(f"Ingrese {atributo}{' (opcional)' if opcional else ''}: ")
        if valor or not opcional:
            atributos[atributo] = valor
    return atributos

def menu_pruebas(gestor, clase_item):
    while True:
        print(f"\nMenú de Pruebas para {clase_item.__name__}")
        print("1. Agregar")
        print("2. Modificar")
        print("3. Buscar")
        print("4. Eliminar")
        print("5. Mostrar Todos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            atributos = solicitar_atributos(clase_item)
            item = clase_item(**atributos)
            print(gestor.agregar(item))

        elif opcion == "2":
            id_item = input("Ingrese el ID del elemento a modificar: ")
            cambios = solicitar_atributos(clase_item, opcional=True)
            print(gestor.modificar(id_item, **cambios))

        elif opcion == "3":
            id_item = input("Ingrese el ID del elemento a buscar: ")
            item = gestor.buscar(id_item)
            if item:
                print(item)
            else:
                print(f"{clase_item.__name__} no encontrado.")

        elif opcion == "4":
            id_item = input("Ingrese el ID del elemento a eliminar: ")
            print(gestor.eliminar(id_item))

        elif opcion == "5":
            if gestor.lista:
                for item in gestor.lista:
                    print(item)
            else:
                print(f"No hay elementos en {clase_item.__name__}.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    # Ejemplo: Cambia estos imports para probar otras clases y gestores
    # from gestores.usuarios import Usuarios
    # from dominios.usuario import Usuario
    
    # gestor = Usuarios()
    # clase = Usuario
    
    from gestores.publicaciones import Publicaciones
    from dominios.publicacion import Publicacion

    gestor = Publicaciones()
    clase = Publicacion

    menu_pruebas(gestor, clase)
