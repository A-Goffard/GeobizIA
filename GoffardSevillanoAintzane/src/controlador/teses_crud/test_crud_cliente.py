from src.controlador.gestores.crud.crud_persona import crear_persona, eliminar_persona
from src.controlador.gestores.crud.crud_cliente import crear_cliente, leer_cliente, actualizar_cliente, eliminar_cliente

def test_crud_cliente():
    # Crear una persona para la clave foránea
    persona = crear_persona(
        id_persona=1,
        nombre="Ana",
        apellido="Gómez",
        email="ana.gomez@example.com",
        telefono="987654321",
        dni="87654321B",
        direccion="Avenida Siempre Viva 456",
        cp="28002",
        poblacion="Barcelona",
        pais="España"
    )
    print(f"Persona creada: {persona}")
    if persona is None:
        print("Error: No se pudo crear la persona. Finalizando la prueba.")
        return

    # Crear un cliente
    cliente = crear_cliente(
        id_cliente=1,
        id_persona=persona.id_persona,
        tipo="Empresa",
        razon_social="Tech Solutions S.L.",
        nif="B12345678",
        fecha_registro="2025-06-27"
    )
    print(f"Cliente creado: {cliente}")
    if cliente is None:
        print("Error: No se pudo crear el cliente. Finalizando la prueba.")
        return

    # Leer el cliente
    cliente_leido = leer_cliente(cliente.id_cliente)
    print(f"Cliente leído: {cliente_leido}")

    # Actualizar el cliente
    actualizado = actualizar_cliente(
        cliente.id_cliente,
        tipo="Individual",
        razon_social=None,
        nif="87654321B",
        fecha_registro="2025-06-28"
    )
    print(f"Cliente actualizado: {actualizado}")
    cliente_leido = leer_cliente(cliente.id_cliente)
    print(f"Cliente después de actualizar: {cliente_leido}")

    # Eliminar el cliente
    eliminado = eliminar_cliente(cliente.id_cliente)
    print(f"Cliente eliminado: {eliminado}")
    cliente_leido = leer_cliente(cliente.id_cliente)
    print(f"Cliente después de eliminar: {cliente_leido}")

    # Limpiar la persona creada
    eliminar_persona(persona.id_persona)
    print(f"Persona eliminada: {persona.id_persona}")

if __name__ == "__main__":
    test_crud_cliente()