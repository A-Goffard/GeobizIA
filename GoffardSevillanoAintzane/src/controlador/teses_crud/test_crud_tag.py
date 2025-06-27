from src.controlador.gestores.crud.crud_tag import crear_tag, leer_tag, actualizar_tag, eliminar_tag

def test_crud_tag():
    # Crear un tag
    tag = crear_tag(palabra_clave="sostenibilidad", categoria="ambiental", frecuencia_uso=5)
    print(f"Tag creado: {tag}")

    if tag is None:
        print("Error: No se pudo crear el tag. Finalizando la prueba.")
        return

    # Leer el tag
    tag_leido = leer_tag(tag.id_tag)
    print(f"Tag leído: {tag_leido}")

    # Actualizar el tag
    actualizado = actualizar_tag(tag.id_tag, palabra_clave="eco", frecuencia_uso=10)
    print(f"Tag actualizado: {actualizado}")
    tag_leido = leer_tag(tag.id_tag)
    print(f"Tag después de actualizar: {tag_leido}")

    # Eliminar el tag
    eliminado = eliminar_tag(tag.id_tag)
    print(f"Tag eliminado: {eliminado}")
    tag_leido = leer_tag(tag.id_tag)
    print(f"Tag después de eliminar: {tag_leido}")

if __name__ == "__main__":
    test_crud_tag()
