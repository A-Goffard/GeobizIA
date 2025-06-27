from src.controlador.gestores.crud.crud_plantilla import crear_plantilla, leer_plantilla, actualizar_plantilla, eliminar_plantilla

def test_crud_plantilla():
    # Crear una plantilla
    plantilla = crear_plantilla(
        id_plantilla=1,
        titulo="Plantilla Informe",
        tipo="Informe",
        contenido_base="Este es el contenido base del informe",
        fecha_creacion="2025-06-27",
        ultima_modificacion="2025-06-27"
    )
    print(f"Plantilla creada: {plantilla}")
    if plantilla is None:
        print("Error: No se pudo crear la plantilla. Finalizando la prueba.")
        return

    # Leer la plantilla
    plantilla_leida = leer_plantilla(plantilla.id_plantilla)
    print(f"Plantilla leída: {plantilla_leida}")

    # Actualizar la plantilla
    actualizado = actualizar_plantilla(
        plantilla.id_plantilla,
        titulo="Plantilla Informe Actualizado",
        tipo="Informe Técnico",
        contenido_base="Contenido base actualizado para informe técnico",
        fecha_creacion="2025-06-27",
        ultima_modificacion="2025-06-28"
    )
    print(f"Plantilla actualizada: {actualizado}")
    plantilla_leida = leer_plantilla(plantilla.id_plantilla)
    print(f"Plantilla después de actualizar: {plantilla_leida}")

    # Eliminar la plantilla
    eliminado = eliminar_plantilla(plantilla.id_plantilla)
    print(f"Plantilla eliminada: {eliminado}")
    plantilla_leida = leer_plantilla(plantilla.id_plantilla)
    print(f"Plantilla después de eliminar: {plantilla_leida}")

if __name__ == "__main__":
    test_crud_plantilla()