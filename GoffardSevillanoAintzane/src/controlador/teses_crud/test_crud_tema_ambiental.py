from src.controlador.gestores.crud.crud_tema_ambiental import crear_tema_ambiental, leer_tema_ambiental, actualizar_tema_ambiental, eliminar_tema_ambiental

def test_crud_tema_ambiental():
    # Crear un tema_ambiental
    tema_ambiental = crear_tema_ambiental(
        id_tema_ambiental=1,
        nombre="Cambio Climático",
        descripcion="Tema relacionado con el calentamiento global y sus impactos"
    )
    print(f"Tema_Ambiental creado: {tema_ambiental}")
    if tema_ambiental is None:
        print("Error: No se pudo crear el tema_ambiental. Finalizando la prueba.")
        return

    # Leer el tema_ambiental
    tema_ambiental_leido = leer_tema_ambiental(tema_ambiental.id_tema_ambiental)
    print(f"Tema_Ambiental leído: {tema_ambiental_leido}")

    # Actualizar el tema_ambiental
    actualizado = actualizar_tema_ambiental(
        tema_ambiental.id_tema_ambiental,
        nombre="Cambio Climático Actualizado",
        descripcion="Tema actualizado sobre el calentamiento global y sus impactos"
    )
    print(f"Tema_Ambiental actualizado: {actualizado}")
    tema_ambiental_leido = leer_tema_ambiental(tema_ambiental.id_tema_ambiental)
    print(f"Tema_Ambiental después de actualizar: {tema_ambiental_leido}")

    # Eliminar el tema_ambiental
    eliminado = eliminar_tema_ambiental(tema_ambiental.id_tema_ambiental)
    print(f"Tema_Ambiental eliminado: {eliminado}")
    tema_ambiental_leido = leer_tema_ambiental(tema_ambiental.id_tema_ambiental)
    print(f"Tema_Ambiental después de eliminar: {tema_ambiental_leido}")

if __name__ == "__main__":
    test_crud_tema_ambiental()