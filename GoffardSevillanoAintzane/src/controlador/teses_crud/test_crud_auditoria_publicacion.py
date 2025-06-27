from src.controlador.gestores.crud.crud_persona import crear_persona, eliminar_persona
from src.controlador.gestores.crud.crud_usuario import crear_usuario, eliminar_usuario
from src.controlador.gestores.crud.crud_generadorIA import crear_generadorIA, eliminar_generadorIA
from src.controlador.gestores.crud.crud_plantilla import crear_plantilla, eliminar_plantilla
from src.controlador.gestores.crud.crud_tipo_publicacion import crear_tipo_publicacion, eliminar_tipo_publicacion
from src.controlador.gestores.crud.crud_publicacion import crear_publicacion, eliminar_publicacion
from src.controlador.gestores.crud.crud_auditoria_publicacion import crear_auditoria_publicacion, leer_auditoria_publicacion, actualizar_auditoria_publicacion, eliminar_auditoria_publicacion

def test_crud_auditoria_publicacion():
    # Crear una persona para la clave foránea
    persona = crear_persona(
        id_persona=1,
        nombre="Laura",
        apellido="Martínez",
        email="laura.martinez@example.com",
        telefono="912345678",
        dni="12345678G",
        direccion="Calle Estrella 123",
        cp="28004",
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
        fecha_nacimiento="1985-03-15",
        rol="Administrador",
        preferencias="Notificaciones por email",
        password="password789"
    )
    print(f"Usuario creado: {usuario}")
    if usuario is None:
        print("Error: No se pudo crear el usuario. Finalizando la prueba.")
        return

    # Crear un generadorIA para la clave foránea
    generadorIA = crear_generadorIA(
        id_generador=1,
        id_usuario=usuario.id_usuario,
        nombre="Grok",
        descripcion="Generador de texto avanzado",
        tipo="IA de texto"
    )
    print(f"GeneradorIA creado: {generadorIA}")
    if generadorIA is None:
        print("Error: No se pudo crear el generadorIA. Finalizando la prueba.")
        return

    # Crear un tipo_publicacion para la clave foránea
    tipo_publicacion = crear_tipo_publicacion(
        id_tipo=1,
        nombre="Artículo",
        descripcion="Publicación de tipo artículo"
    )
    print(f"Tipo_Publicacion creado: {tipo_publicacion}")
    if tipo_publicacion is None:
        print("Error: No se pudo crear el tipo_publicacion. Finalizando la prueba.")
        return

    # Crear una plantilla para la clave foránea
    plantilla = crear_plantilla(
        id_plantilla=1,
        nombre="Plantilla Artículo",
        descripcion="Plantilla para artículos estándar",
        contenido="Contenido de ejemplo para artículos"
    )
    print(f"Plantilla creada: {plantilla}")
    if plantilla is None:
        print("Error: No se pudo crear la plantilla. Finalizando la prueba.")
        return

    # Crear una publicación para la clave foránea
    publicacion = crear_publicacion(
        id_publicacion=1,
        id_usuario=usuario.id_usuario,
        id_generador=generadorIA.id_generador,
        id_plantilla=plantilla.id_plantilla,
        id_tipo=tipo_publicacion.id_tipo,
        fecha_publicacion="2025-06-27",
        contenido="Contenido de la publicación de prueba",
        estado="Publicado",
        enlace="http://example.com/publicacion1",
        coste=50.0
    )
    print(f"Publicación creada: {publicacion}")
    if publicacion is None:
        print("Error: No se pudo crear la publicación. Finalizando la prueba.")
        return

    # Crear una auditoria_publicacion
    auditoria = crear_auditoria_publicacion(
        id_auditoria=1,
        id_publicacion=publicacion.id_publicacion,
        usuario_id=usuario.id_usuario,
        fecha="2025-06-27 15:30:00",
        accion="Creación de publicación",
        descripcion="Se creó una nueva publicación en el sistema",
        nivel="INFO"
    )
    print(f"Auditoria_Publicacion creada: {auditoria}")
    if auditoria is None:
        print("Error: No se pudo crear la auditoria_publicacion. Finalizando la prueba.")
        return

    # Leer la auditoria_publicacion
    auditoria_leida = leer_auditoria_publicacion(auditoria.id_auditoria)
    print(f"Auditoria_Publicacion leída: {auditoria_leida}")

    # Actualizar la auditoria_publicacion
    actualizado = actualizar_auditoria_publicacion(
        auditoria.id_auditoria,
        fecha="2025-06-27 16:00:00",
        accion="Edición de publicación",
        descripcion="Se editó la publicación en el sistema",
        nivel="INFO"
    )
    print(f"Auditoria_Publicacion actualizada: {actualizado}")
    auditoria_leida = leer_auditoria_publicacion(auditoria.id_auditoria)
    print(f"Auditoria_Publicacion después de actualizar: {auditoria_leida}")

    # Eliminar la auditoria_publicacion
    eliminado = eliminar_auditoria_publicacion(auditoria.id_auditoria)
    print(f"Auditoria_Publicacion eliminada: {eliminado}")
    auditoria_leida = leer_auditoria_publicacion(auditoria.id_auditoria)
    print(f"Auditoria_Publicacion después de eliminar: {auditoria_leida}")

    # Limpiar las entidades creadas
    eliminar_publicacion(publicacion.id_publicacion)
    print(f"Publicación eliminada: {publicacion.id_publicacion}")
    eliminar_plantilla(plantilla.id_plantilla)
    print(f"Plantilla eliminada: {plantilla.id_plantilla}")
    eliminar_tipo_publicacion(tipo_publicacion.id_tipo)
    print(f"Tipo_Publicacion eliminado: {tipo_publicacion.id_tipo}")
    eliminar_generadorIA(generadorIA.id_generador)
    print(f"GeneradorIA eliminado: {generadorIA.id_generador}")
    eliminar_usuario(usuario.id_usuario)
    print(f"Usuario eliminado: {usuario.id_usuario}")
    eliminar_persona(persona.id_persona)
    print(f"Persona eliminada: {persona.id_persona}")

if __name__ == "__main__":
    test_crud_auditoria_publicacion()