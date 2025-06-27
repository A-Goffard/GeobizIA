from src.controlador.gestores.crud.crud_persona import crear_persona, eliminar_persona
from src.controlador.gestores.crud.crud_usuario import crear_usuario, eliminar_usuario
from src.controlador.gestores.crud.crud_generadoria import crear_generador_IA, leer_generador_IA, actualizar_generador_IA, eliminar_generador_IA

def test_crud_generador_IA():
    # Crear una persona para la clave foránea
    persona = crear_persona(
        id_persona=1,
        nombre="Laura",
        apellido="Sánchez",
        email="laura.sanchez@example.com",
        telefono="987654321",
        dni="87654321D",
        direccion="Calle Luna 123",
        cp="28004",
        poblacion="Sevilla",
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
        fecha_nacimiento="1995-03-15",
        rol="Analista",
        preferencias="Notificaciones por email",
        password="password123"
    )
    print(f"Usuario creado: {usuario}")
    if usuario is None:
        print("Error: No se pudo crear el usuario. Finalizando la prueba.")
        return

    # Crear un generador_IA
    generador = crear_generador_IA(
        id_generador_IA=1,
        id_usuario=usuario.id_usuario,
        nombre="Generador de Texto",
        descripcion="Generador de texto basado en IA",
        tipo="Texto"
    )
    print(f"GeneradorIA creado: {generador}")
    if generador is None:
        print("Error: No se pudo crear el generador_IA. Finalizando la prueba.")
        return

    # Leer el generador_IA
    generador_leido = leer_generador_IA(generador.id_generador_IA)
    print(f"GeneradorIA leído: {generador_leido}")

    # Actualizar el generador_IA
    actualizado = actualizar_generador_IA(
        generador.id_generador_IA,
        nombre="Generador de Imágenes",
        descripcion="Generador de imágenes basado en IA",
        tipo="Imágenes"
    )
    print(f"GeneradorIA actualizado: {actualizado}")
    generador_leido = leer_generador_IA(generador.id_generador_IA)
    print(f"GeneradorIA después de actualizar: {generador_leido}")

    # Eliminar el generador_IA
    eliminado = eliminar_generador_IA(generador.id_generador_IA)
    print(f"GeneradorIA eliminado: {eliminado}")
    generador_leido = leer_generador_IA(generador.id_generador_IA)
    print(f"GeneradorIA después de eliminar: {generador_leido}")

    # Limpiar el usuario y la persona creados
    eliminar_usuario(usuario.id_usuario)
    print(f"Usuario eliminado: {usuario.id_usuario}")
    eliminar_persona(persona.id_persona)
    print(f"Persona eliminada: {persona.id_persona}")

if __name__ == "__main__":
    test_crud_generador_IA()