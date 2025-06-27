from src.controlador.gestores.crud.crud_persona import crear_persona, eliminar_persona
from src.controlador.gestores.crud.crud_usuario import crear_usuario, eliminar_usuario
from src.controlador.gestores.crud.crud_log_sistema import crear_log_sistema, leer_log_sistema, actualizar_log_sistema, eliminar_log_sistema

def test_crud_log_sistema():
    # Crear una persona para la clave foránea
    persona = crear_persona(
        id_persona=1,
        nombre="Marta",
        apellido="Rodríguez",
        email="marta.rodriguez@example.com",
        telefono="912345678",
        dni="12345678E",
        direccion="Calle Sol 456",
        cp="28005",
        poblacion="Madrid",
        pais="España"
    )
    print(f"Persona creada: {persona}")
    if persona is None:
        print("Error: No se pudo crear la persona. Finalizando la prueba.")
        return

    # Crear un usuario para la clave foránea
    usuario = crear_usuario(
        id_usuario=1,
        id_persona=persona.id_persona,
        fecha_nacimiento="1990-05-20",
        rol="Editor",
        preferencias="Notificaciones por email",
        password="password456"
    )
    print(f"Usuario creado: {usuario}")
    if usuario is None:
        print("Error: No se pudo crear el usuario. Finalizando la prueba.")
        return

    # Crear un log_sistema
    log_sistema = crear_log_sistema(
        id_log_sistema=1,
        usuario_id=usuario.id_usuario,
        fecha="2025-06-27 13:22:00",
        accion="Inicio de sesión",
        descripcion="El usuario inició sesión en el sistema",
        nivel="INFO"
    )
    print(f"Log_Sistema creado: {log_sistema}")
    if log_sistema is None:
        print("Error: No se pudo crear el log_sistema. Finalizando la prueba.")
        return

    # Leer el log_sistema
    log_sistema_leido = leer_log_sistema(log_sistema.id_log_sistema)
    print(f"Log_Sistema leído: {log_sistema_leido}")

    # Actualizar el log_sistema
    actualizado = actualizar_log_sistema(
        log_sistema.id_log_sistema,
        fecha="2025-06-27 14:00:00",
        accion="Actualización de perfil",
        descripcion="El usuario actualizó su perfil en el sistema",
        nivel="INFO"
    )
    print(f"Log_Sistema actualizado: {actualizado}")
    log_sistema_leido = leer_log_sistema(log_sistema.id_log_sistema)
    print(f"Log_Sistema después de actualizar: {log_sistema_leido}")

    # Eliminar el log_sistema
    eliminado = eliminar_log_sistema(log_sistema.id_log_sistema)
    print(f"Log_Sistema eliminado: {eliminado}")
    log_sistema_leido = leer_log_sistema(log_sistema.id_log_sistema)
    print(f"Log_Sistema después de eliminar: {log_sistema_leido}")

    # Limpiar el usuario y la persona creados
    eliminar_usuario(usuario.id_usuario)
    print(f"Usuario eliminado: {usuario.id_usuario}")
    eliminar_persona(persona.id_persona)
    print(f"Persona eliminada: {persona.id_persona}")

if __name__ == "__main__":
    test_crud_log_sistema()