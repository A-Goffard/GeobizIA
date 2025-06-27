from gestores.roles import Roles

def test_base_gestor():
    gestor = Roles()

    # Crear un rol
    rol = gestor.agregar(id_rol=100, nombre="TestRol", descripcion="Rol de prueba")
    print(f"Rol creado: {rol}")

    # Buscar el rol
    rol_buscado = gestor.buscar(100)
    print(f"Rol buscado: {rol_buscado}")

    # Mostrar todos los roles
    roles = gestor.mostrar_todos_los_elem()
    print("Todos los roles:")
    for rol in roles:
        print(rol)

    # Actualizar el rol
    actualizado = gestor.actualizar(100, nombre="TestRolModificado")
    print(f"Rol actualizado: {actualizado}")
    rol_buscado = gestor.buscar(100)
    print(f"Rol después de actualizar: {rol_buscado}")

    # Eliminar el rol
    eliminado = gestor.eliminar(100)
    print(f"Rol eliminado: {eliminado}")
    rol_buscado = gestor.buscar(100)
    print(f"Rol después de eliminar: {rol_buscado}")

if __name__ == "__main__":
    test_base_gestor()