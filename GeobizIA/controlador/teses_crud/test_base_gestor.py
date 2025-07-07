import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from GeobizIA.controlador.gestores.roles import Roles

@pytest.fixture
def gestor_eventos():
    gestor = Roles()
    # Elimina el rol con id=100 si existe para evitar conflictos de clave primaria
    gestor.eliminar(100)
    return gestor

def test_base_gestor():
    gestor = Roles()

    # Crear un rol
    rol = gestor.agregar(id_rol=100, nombre="TestRol", descripcion="Rol de prueba")
    print(f"Rol creado: {rol}")

    # Buscar el rol
    rol_buscado = gestor.buscar(100)
    print(f"Rol buscado: {rol_buscado}")

    # Mostrar todos los roles
    roles = gestor.listar()
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

