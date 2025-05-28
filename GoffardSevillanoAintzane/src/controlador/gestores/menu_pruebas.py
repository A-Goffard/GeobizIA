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
    def mostrar_elemento(self, elemento):
        return str(elemento)

def solicitar_atributos(clase, opcional=False):
    atributos = {}
    parametros = clase.__init__.__code__.co_varnames[1:clase.__init__.__code__.co_argcount]
    for atributo in parametros:
        valor = input(f"Ingrese {atributo}{' (opcional)' if opcional else ''}: ")
        if valor or not opcional:
            if atributo == "id":
                try:
                    valor = int(valor)
                except ValueError:
                    print("El ID debe ser un número entero.")
                    return solicitar_atributos(clase, opcional)
            atributos[atributo] = valor
    return atributos

def menu_pruebas(gestor, clase_item):
    while True:
        print(f"\nMenú de Pruebas para {clase_item.__name__}")
        print("1. Agregar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Mostrar Todos")
        print("5. Existe")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            atributos = solicitar_atributos(clase_item)
            item = clase_item(**atributos)
            if gestor.agregar(item):
                print(f"{clase_item.__name__} agregado exitosamente.")
            else:
                print(f"No se pudo agregar el {clase_item.__name__}.")

        elif opcion == "2":
            atributos = solicitar_atributos(clase_item)
            item = clase_item(**atributos)
            encontrado = gestor.buscar(item)
            if encontrado:
                print(gestor.mostrar_elemento(encontrado))
            else:
                print(f"{clase_item.__name__} no encontrado.")

        elif opcion == "3":
            atributos = solicitar_atributos(clase_item)
            item = clase_item(**atributos)
            if gestor.eliminar(item):
                print(f"{clase_item.__name__} eliminado exitosamente.")
            else:
                print(f"No se encontró el {clase_item.__name__} para eliminar.")

        elif opcion == "4":
            elementos = gestor.mostrar_todos_los_elem()
            if elementos:
                for item in elementos:
                    print(gestor.mostrar_elemento(item))
            else:
                print(f"No hay elementos en {clase_item.__name__}.")

        elif opcion == "5":
            atributos = solicitar_atributos(clase_item)
            item = clase_item(**atributos)
            if gestor.existe(item):
                print(f"El elemento existe en {clase_item.__name__}.")
            else:
                print(f"El elemento NO existe en {clase_item.__name__}.")

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
