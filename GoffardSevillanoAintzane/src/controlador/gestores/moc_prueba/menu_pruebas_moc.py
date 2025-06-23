from .ejemplo_moc import (
    usuarios_cargados, usuarios_no_cargados,
    proyectos_cargados, proyectos_no_cargados,
    temas_ambientales_cargados, temas_ambientales_no_cargados,
    roles_cargados, roles_no_cargados
)
from .base_gestor_moc import BaseGestor

def menu_gestor(nombre, gestor, cargados, no_cargados, key=lambda x: getattr(x, 'id', getattr(x, 'nombre', None))):
    while True:
        print(f"\n--- Menú de {nombre} ---")
        print("1. Mostrar todos")
        print("2. Agregar (por id)")
        print("3. Eliminar (por id)")
        print("4. Buscar (por id)")
        print("5. Volver")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            for elem in gestor.mostrar_todos_los_elem():
                print(gestor.mostrar_elemento(elem))
        elif opcion == "2":
            id_agregar = input("ID a agregar: ")
            try:
                id_agregar = int(id_agregar)
            except:
                print("ID inválido.")
                continue
            elem = next((e for e in no_cargados if key(e) == id_agregar), None)
            if elem:
                if gestor.agregar(elem):
                    print("Agregado correctamente.")
                else:
                    print("Ya existe.")
            else:
                print("No encontrado en los no cargados.")
        elif opcion == "3":
            id_eliminar = input("ID a eliminar: ")
            try:
                id_eliminar = int(id_eliminar)
            except:
                print("ID inválido.")
                continue
            elem = next((e for e in gestor.mostrar_todos_los_elem() if key(e) == id_eliminar), None)
            if elem:
                gestor.eliminar(elem)
                print("Eliminado.")
            else:
                print("No encontrado.")
        elif opcion == "4":
            id_buscar = input("ID a buscar: ")
            try:
                id_buscar = int(id_buscar)
            except:
                print("ID inválido.")
                continue
            elem = next((e for e in gestor.mostrar_todos_los_elem() if key(e) == id_buscar), None)
            if elem:
                print("Encontrado:", gestor.mostrar_elemento(elem))
            else:
                print("No encontrado.")
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def main():
    # Inicializar gestores con los cargados
    gestor_usuarios = BaseGestor()
    for u in usuarios_cargados:
        gestor_usuarios.agregar(u)
    gestor_proyectos = BaseGestor()
    for p in proyectos_cargados:
        gestor_proyectos.agregar(p)
    gestor_temas = BaseGestor()
    for t in temas_ambientales_cargados:
        gestor_temas.agregar(t)
    gestor_roles = BaseGestor()
    for r in roles_cargados:
        gestor_roles.agregar(r)

    while True:
        print("\n=== Menú principal ===")
        print("1. Usuarios")
        print("2. Proyectos")
        print("3. Temas Ambientales")
        print("4. Roles")
        print("5. Salir")
        op = input("Elige una opción: ")
        if op == "1":
            menu_gestor(
                "Usuarios",
                gestor_usuarios,
                usuarios_cargados,
                usuarios_no_cargados,
                key=lambda x: getattr(x, "id_usuario", None)
            )
        elif op == "2":
            menu_gestor(
                "Proyectos",
                gestor_proyectos,
                proyectos_cargados,
                proyectos_no_cargados,
                key=lambda x: getattr(x, "id_proyecto", None)
            )
        elif op == "3":
            menu_gestor(
                "Temas Ambientales",
                gestor_temas,
                temas_ambientales_cargados,
                temas_ambientales_no_cargados,
                key=lambda x: getattr(x, "id", getattr(x, "id_tema_ambiental", None))
            )
        elif op == "4":
            menu_gestor(
                "Roles",
                gestor_roles,
                roles_cargados,
                roles_no_cargados,
                key=lambda x: getattr(x, "nombre", None)
            )
        elif op == "5":
            print("Adiós.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
