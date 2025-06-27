from src.controlador.gestores.crud.crud_tema_ambiental_tag import buscar_relacion_tema_tag, crear_relacion_tema_tag, eliminar_relacion_tema_tag, listar_relaciones_por_tag, listar_relaciones_por_tema


def test_crud_tema_ambiental_tag():
    # Crear relación
    relacion = crear_relacion_tema_tag(1, 10)
    print(f"Creada relación: {relacion}")

    # Buscar relación
    encontrada = buscar_relacion_tema_tag(1, 10)
    print(f"Encontrada relación: {encontrada}")

    # Listar por tema
    lista_tema = listar_relaciones_por_tema(1)
    print(f"Relaciones para tema 1: {lista_tema}")

    # Listar por tag
    lista_tag = listar_relaciones_por_tag(10)
    print(f"Relaciones para tag 10: {lista_tag}")

    # Eliminar relación
    eliminada = eliminar_relacion_tema_tag(1, 10)
    print(f"Eliminada relación: {eliminada}")

if __name__ == "__main__":
    test_crud_tema_ambiental_tag()
