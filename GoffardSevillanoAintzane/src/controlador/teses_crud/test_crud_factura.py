from src.controlador.gestores.crud.crud_persona import crear_persona, eliminar_persona
from src.controlador.gestores.crud.crud_cliente import crear_cliente, eliminar_cliente
from src.controlador.gestores.crud.crud_factura import crear_factura, leer_factura, actualizar_factura, eliminar_factura

def test_crud_factura():
    # Crear una persona para la clave foránea
    persona = crear_persona(
        id_persona=1,
        nombre="Ana",
        apellido="Gómez",
        email="ana.gomez@example.com",
        telefono="987654321",
        dni="87654321F",
        direccion="Calle Luna 789",
        cp="28006",
        poblacion="Barcelona",
        pais="España"
    )
    print(f"Persona creada: {persona}")
    if persona is None:
        print("Error: No se pudo crear la persona. Finalizando la prueba.")
        return

    # Crear un cliente para la clave foránea
    cliente = crear_cliente(
        id_cliente=1,
        id_persona=persona.id_persona,
        tipo="Premium",
        razon_social="Consultoría Gómez S.L.",
        nif="B12345678",
        fecha_registro="2025-06-27"
    )
    print(f"Cliente creado: {cliente}")
    if cliente is None:
        print("Error: No se pudo crear el cliente. Finalizando la prueba.")
        return

    # Crear una factura
    factura = crear_factura(
        id_factura=1,
        id_cliente=cliente.id_cliente,
        tipo="Factura Ordinaria",
        nombre="Consultoría Gómez S.L.",
        direccion="Calle Luna 789, Barcelona",
        nif="B12345678",
        fecha_facturacion="2025-06-27",
        fecha_vencimiento="2025-07-27",
        concepto="Servicios de consultoría",
        responsable="Juan Pérez",
        iva=21.0,
        coste_total=1210.0,
        base_imponible=1000.0,
        numero_factura="FAC-2025-001",
        tipo_pago="Transferencia",
        irpf=15.0
    )
    print(f"Factura creada: {factura}")
    if factura is None:
        print("Error: No se pudo crear la factura. Finalizando la prueba.")
        return

    # Leer la factura
    factura_leida = leer_factura(factura.id_factura)
    print(f"Factura leída: {factura_leida}")

    # Actualizar la factura
    actualizado = actualizar_factura(
        factura.id_factura,
        tipo="Factura Rectificativa",
        nombre="Consultoría Gómez S.L. Actualizada",
        direccion="Calle Sol 456, Barcelona",
        nif="B12345678",
        fecha_facturacion="2025-06-28",
        fecha_vencimiento="2025-07-28",
        concepto="Servicios de consultoría actualizados",
        responsable="María López",
        iva=21.0,
        coste_total=1452.0,
        base_imponible=1200.0,
        numero_factura="FAC-2025-002",
        tipo_pago="Domiciliación",
        irpf=15.0
    )
    print(f"Factura actualizada: {actualizado}")
    factura_leida = leer_factura(factura.id_factura)
    print(f"Factura después de actualizar: {factura_leida}")

    # Eliminar la factura
    eliminado = eliminar_factura(factura.id_factura)
    print(f"Factura eliminada: {eliminado}")
    factura_leida = leer_factura(factura.id_factura)
    print(f"Factura después de eliminar: {factura_leida}")

    # Limpiar el cliente y la persona creados
    eliminar_cliente(cliente.id_cliente)
    print(f"Cliente eliminado: {cliente.id_cliente}")
    eliminar_persona(persona.id_persona)
    print(f"Persona eliminada: {persona.id_persona}")

if __name__ == "__main__":
    test_crud_factura()