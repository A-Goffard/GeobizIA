from src.controlador.gestores.crud.crud_persona import crear_persona, eliminar_persona
from src.controlador.gestores.crud.crud_usuario import crear_usuario, eliminar_usuario
from src.controlador.gestores.crud.crud_generadoria import crear_generador_IA, eliminar_generador_IA
from src.controlador.gestores.crud.crud_tipo_publicacion import crear_tipo_publicacion, eliminar_tipo_publicacion
from src.controlador.gestores.crud.crud_publicacion import crear_publicacion, leer_publicacion, actualizar_publicacion, eliminar_publicacion

def test_crud_publicacion():
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

    # Crear un generador_IA para la clave foránea
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

    # Crear un tipo_publicacion para la clave foránea
    tipo_publicacion = crear_tipo_publicacion(
        id_tipo_publicacion=1,
        nombre="Artículo",
        descripcion="Publicación de tipo artículo"
    )
    print(f"Tipo_Publicacion creado: {tipo_publicacion}")
    if tipo_publicacion is None:
        print("Error: No se pudo crear el tipo_publicacion. Finalizando la prueba.")
        return

    # Crear una publicación
    publicacion = crear_publicacion(
        id_publicacion=1,
        id_generador_IA=generador.id_generador_IA,
        id_tipo_publicacion=tipo_publicacion.id_tipo_publicacion,
        contenido="Este es un artículo generado por IA",
        fecha_creacion="2025-06-27"
    )
    print(f"Publicación creada: {publicacion}")
    if publicacion is None:
        print("Error: No se pudo crear la publicación. Finalizando la prueba.")
        return

    # Leer la publicación
    publicacion_leida = leer_publicacion(publicacion.id_publicacion)
    print(f"Publicación leída: {publicacion_leida}")

    # Actualizar la publicación
    actualizado = actualizar_publicacion(
        publicacion.id_publicacion,
        contenido="Este es un artículo actualizado generado por IA",
        fecha_creacion="2025-06-28"
    )
    print(f"Publicación actualizada: {actualizado}")
    publicacion_leida = leer_publicacion(publicacion.id_publicacion)
    print(f"Publicación después de actualizar: {publicacion_leida}")

    # Eliminar la publicación
    eliminado = eliminar_publicacion(publicacion.id_publicacion)
    print(f"Publicación eliminada: {eliminado}")
    publicacion_leida = leer_publicacion(publicacion.id_publicacion)
    print(f"Publicación después de eliminar: {publicacion_leida}")

    # Limpiar las entidades creadas
    eliminar_tipo_publicacion(tipo_publicacion.id_tipo_publicacion)
    print(f"Tipo_Publicacion eliminado: {tipo_publicacion.id_tipo_publicacion}")
    eliminar_generador_IA(generador.id_generador_IA)
    print(f"GeneradorIA eliminado: {generador.id_generador_IA}")
    eliminar_usuario(usuario.id_usuario)
    print(f"Usuario eliminado: {usuario.id_usuario}")
    eliminar_persona(persona.id_persona)
    print(f"Persona eliminada: {persona.id_persona}")

if __name__ == "__main__":
    test_crud_publicacion()