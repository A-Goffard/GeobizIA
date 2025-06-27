from src.controlador.gestores.crud.crud_persona import crear_persona, leer_persona, actualizar_persona, eliminar_persona

def test_crud_persona():
    # Crear una persona
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

    # Leer la persona
    persona_leida = leer_persona(persona.id_persona)
    print(f"Persona leída: {persona_leida}")

    # Actualizar la persona
    actualizado = actualizar_persona(
        persona.id_persona,
        nombre="María",
        apellido="López",
        email="maria.lopez@example.com"
    )
    print(f"Persona actualizada: {actualizado}")
    persona_leida = leer_persona(persona.id_persona)
    print(f"Persona después de actualizar: {persona_leida}")

    # Eliminar la persona
    eliminado = eliminar_persona(persona.id_persona)
    print(f"Persona eliminada: {eliminado}")
    persona_leida = leer_persona(persona.id_persona)
    print(f"Persona después de eliminar: {persona_leida}")

if __name__ == "__main__":
    test_crud_persona()