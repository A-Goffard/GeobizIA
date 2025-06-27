from src.controlador.gestores.crud.crud_persona import crear_persona, eliminar_persona
from src.controlador.gestores.crud.crud_usuario import crear_usuario, leer_usuario, actualizar_usuario, eliminar_usuario

def test_crud_usuario():
    # Crear una persona para la clave foránea
    persona = crear_persona(
        id_persona=1,
        nombre="Juan",
        apellido="Pérez",
        email="juan.perez@example.com",
        telefono="123456789",
        dni="12345678A",
        direccion="Calle Falsa 123",
        cp="28001",
        poblacion="Madrid",
        pais="España"
    )
    print(f"Persona creada: {persona}")
    if persona is None:
        print("Error: No se pudo crear la persona. Finalizando la prueba.")
        return

    # Crear un usuario
    usuario = crear_usuario(
        id_usuario=1,
        id_persona=persona.id_persona,
        fecha_nacimiento="1990-01-01",
        rol="Usuario",
        preferencias="Notificaciones por email",
        password="contraseña123"
    )
    print(f"Usuario creado: {usuario}")
    if usuario is None:
        print("Error: No se pudo crear el usuario. Finalizando la prueba.")
        return

    # Leer el usuario
    usuario_leido = leer_usuario(usuario.id_usuario)
    print(f"Usuario leído: {usuario_leido}")

    # Actualizar el usuario
    actualizado = actualizar_usuario(
        usuario.id_usuario,
        fecha_nacimiento="1990-02-02",
        rol="Administrador",
        preferencias="Notificaciones por SMS",
        password="nueva_contraseña456"
    )
    print(f"Usuario actualizado: {actualizado}")
    usuario_leido = leer_usuario(usuario.id_usuario)
    print(f"Usuario después de actualizar: {usuario_leido}")

    # Eliminar el usuario
    eliminado = eliminar_usuario(usuario.id_usuario)
    print(f"Usuario eliminado: {eliminado}")
    usuario_leido = leer_usuario(usuario.id_usuario)
    print(f"Usuario después de eliminar: {usuario_leido}")

    # Limpiar la persona creada
    eliminar_persona(persona.id_persona)
    print(f"Persona eliminada: {persona.id_persona}")

if __name__ == "__main__":
    test_crud_usuario()