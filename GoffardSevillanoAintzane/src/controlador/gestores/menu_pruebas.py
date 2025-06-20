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
    def get_id_field():
        for v in clase_item.__init__.__code__.co_varnames[1:clase_item.__init__.__code__.co_argcount]:
            if v.startswith("id_"):
                return v
        for v in clase_item.__init__.__code__.co_varnames[1:clase_item.__init__.__code__.co_argcount]:
            if v == "id":
                return v
        raise Exception("No se encontró campo de id en el constructor.")

    def get_id_value():
        id_field = get_id_field()
        valor = input(f"Ingrese {id_field}: ")
        return id_field, valor  # No convertir a int, comparar como string

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
            id_field, valor = get_id_value()
            if id_field is None:
                continue
            encontrado = None
            for elem in gestor.mostrar_todos_los_elem():
                if hasattr(elem, id_field) and str(getattr(elem, id_field)) == str(valor):
                    encontrado = elem
                    break
            if encontrado:
                print(gestor.mostrar_elemento(encontrado))
            else:
                print(f"{clase_item.__name__} no encontrado.")

        elif opcion == "3":
            id_field, valor = get_id_value()
            if id_field is None:
                continue
            eliminado = False
            for elem in gestor.mostrar_todos_los_elem():
                if hasattr(elem, id_field) and str(getattr(elem, id_field)) == str(valor):
                    eliminado = gestor.eliminar(elem)
                    break
            if eliminado:
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
            id_field, valor = get_id_value()
            if id_field is None:
                continue
            existe = False
            for elem in gestor.mostrar_todos_los_elem():
                if hasattr(elem, id_field) and str(getattr(elem, id_field)) == str(valor):
                    existe = True
                    break
            if existe:
                print(f"El elemento existe en {clase_item.__name__}.")
            else:
                print(f"El elemento NO existe en {clase_item.__name__}.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    # --- BLOQUES DE IMPORTS Y VARIABLES PARA PRUEBAS ---

    # --- USUARIOS ---
    from gestores.usuarios import Usuarios
    from dominios.usuario import Usuario
    gestor = Usuarios()
    clase = Usuario

    # --- PARTICIPANTES ---
    # from gestores.participantes import ParticipanteFactory
    # from dominios.participante import Participante
    # gestor = ParticipanteFactory()
    # clase = Participante

    # --- CLIENTES ---
    # from gestores.clientes import Clientes
    # from dominios.cliente import Cliente
    # gestor = Clientes()
    # clase = Cliente

    # --- PUBLICACIONES ---
    # from gestores.publicaciones import Publicaciones
    # from dominios.publicacion import Publicacion
    # gestor = Publicaciones()
    # clase = Publicacion

    # --- PROYECTOS ---
    # from gestores.proyectos import Proyectos
    # from dominios.proyecto import Proyecto
    # gestor = Proyectos()
    # clase = Proyecto

    # --- PROGRAMACIONES ---
    # from gestores.programaciones import Programaciones
    # from dominios.programacion import Programacion
    # gestor = Programaciones()
    # clase = Programacion

    # --- PLANTILLAS ---
    # from gestores.plantillas import Plantillas
    # from dominios.plantilla import Plantilla
    # gestor = Plantillas()
    # clase = Plantilla

    # --- EMPRESAS ---
    # from gestores.empresas import Empresas
    # from dominios.empresa import Empresa
    # gestor = Empresas()
    # clase = Empresa

    # --- EVENTOS ---
    # from gestores.eventos import Eventos
    # from dominios.evento import Evento
    # gestor = Eventos()
    # clase = Evento

    # --- FACTURAS ---
    # from gestores.facturas import Facturas
    # from dominios.factura import Factura
    # gestor = Facturas()
    # clase = Factura

    # --- GENERADORES IA ---
    # from gestores.generadoresia import GeneradoresIA
    # from dominios.generadoria import GeneradorIA
    # gestor = GeneradoresIA()
    # clase = GeneradorIA

    # --- DOCUMENTOS ---
    # from gestores.documentos import GestorDocumentos
    # from dominios.documento import Documento
    # gestor = GestorDocumentos()
    # clase = Documento

    # --- RECURSOS MULTIMEDIA ---
    # from gestores.recursos_multimedia import RecursosMultimedia
    # from dominios.recurso_multimedia import RecursoMultimedia
    # gestor = RecursosMultimedia()
    # clase = RecursoMultimedia

    # --- REDES SOCIALES ---
    # from gestores.redes_sociales import RedesSociales
    # from dominios.redsocial import RedSocial
    # gestor = RedesSociales()
    # clase = RedSocial

    # --- ROLES ---
    # from gestores.roles import Roles
    # from dominios.rol import Rol
    # gestor = Roles()
    # clase = Rol

    # --- TAGS PALABRAS CLAVE ---
    # from gestores.tags_palabras_claves import Tags
    # from dominios.tags_palabras_clave import Tag
    # gestor = Tags()
    # clase = Tag

    # --- TEMAS AMBIENTALES ---
    # from gestores.temas_ambientales import TemasAmbientales
    # from dominios.tema_ambiental import TemaAmbiental
    # gestor = TemasAmbientales()
    # clase = TemaAmbiental

    # --- LOGS SISTEMA ---
    # from gestores.logs_sistema import LogSistema
    # from dominios.log_sistema import LogSistema
    # gestor = LogSistema()
    # clase = LogSistema

    # --- AUDITORIAS PUBLICACIONES ---
    # from gestores.auditorias_publicaciones import AuditoriaPublicacion
    # from dominios.auditoria_publicacion import AuditoriaPublicacion
    # gestor = AuditoriaPublicacion()
    # clase = AuditoriaPublicacion

    menu_pruebas(gestor, clase)