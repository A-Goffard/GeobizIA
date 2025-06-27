from src.controlador.gestores.crud.crud_tipo_publicacion import crear_tipo_publicacion, leer_tipo_publicacion, actualizar_tipo_publicacion, eliminar_tipo_publicacion

def test_crud_tipo_publicacion():
    # Crear un tipo_publicacion
    tipo_publicacion = crear_tipo_publicacion(
        id_tipo_publicacion=1,
        nombre="Artículo",
        descripcion="Publicación de tipo artículo"
    )
    print(f"Tipo_Publicacion creado: {tipo_publicacion}")
    if tipo_publicacion is None:
        print("Error: No se pudo crear el tipo_publicacion. Finalizando la prueba.")
        return

    # Leer el tipo_publicacion
    tipo_publicacion_leido = leer_tipo_publicacion(tipo_publicacion.id_tipo_publicacion)
    print(f"Tipo_Publicacion leído: {tipo_publicacion_leido}")

    # Actualizar el tipo_publicacion
    actualizado = actualizar_tipo_publicacion(
        tipo_publicacion.id_tipo_publicacion,
        nombre="Informe",
        descripcion="Publicación de tipo informe técnico"
    )
    print(f"Tipo_Publicacion actualizado: {actualizado}")
    tipo_publicacion_leido = leer_tipo_publicacion(tipo_publicacion.id_tipo_publicacion)
    print(f"Tipo_Publicacion después de actualizar: {tipo_publicacion_leido}")

    # Eliminar el tipo_publicacion
    eliminado = eliminar_tipo_publicacion(tipo_publicacion.id_tipo_publicacion)
    print(f"Tipo_Publicacion eliminado: {eliminado}")
    tipo_publicacion_leido = leer_tipo_publicacion(tipo_publicacion.id_tipo_publicacion)
    print(f"Tipo_Publicacion después de eliminar: {tipo_publicacion_leido}")

if __name__ == "__main__":
    test_crud_tipo_publicacion()