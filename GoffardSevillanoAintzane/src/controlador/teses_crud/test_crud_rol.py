from src.controlador.gestores.crud.crud_rol import crear_rol, leer_rol, actualizar_rol, eliminar_rol

def test_crud_rol():
    # Crear un rol
    rol = crear_rol(id_rol=1, nombre="Administrador", descripcion="Rol con permisos completos")
    print(f"Rol creado: {rol}")
    
    if rol is None:
        print("Error: No se pudo crear el rol. Finalizando la prueba.")
        return

    # Leer el rol
    rol_leido = leer_rol(rol.id_rol)
    print(f"Rol leído: {rol_leido}")

    # Actualizar el rol
    actualizado = actualizar_rol(rol.id_rol, nombre="Super Administrador", descripcion="Rol actualizado")
    print(f"Rol actualizado: {actualizado}")
    rol_leido = leer_rol(rol.id_rol)
    print(f"Rol después de actualizar: {rol_leido}")

    # Eliminar el rol
    eliminado = eliminar_rol(rol.id_rol)
    print(f"Rol eliminado: {eliminado}")
    rol_leido = leer_rol(rol.id_rol)
    print(f"Rol después de eliminar: {rol_leido}")

if __name__ == "__main__":
    test_crud_rol()