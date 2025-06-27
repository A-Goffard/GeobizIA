from src.controlador.gestores.crud.crud_redsocial import crear_redsocial, leer_redsocial, actualizar_redsocial, eliminar_redsocial

def test_crud_redsocial():
    # Crear red social
    red = crear_redsocial(
        plataforma="Instagram",
        nombre_cuenta="@eco_ambiental",
        estado_conexion="Activa",
        ultima_publicacion="2025-06-01"
    )
    print(f"Red social creada: {red}")

    if red is None:
        print("Error: No se pudo crear la red social. Finalizando la prueba.")
        return

    # Leer red social
    red_leida = leer_redsocial(red.id_red_social)
    print(f"Red social leída: {red_leida}")

    # Actualizar red social
    actualizado = actualizar_redsocial(
        red.id_red_social,
        nombre_cuenta="@eco_actualizada",
        estado_conexion="En revisión"
    )
    print(f"Red social actualizada: {actualizado}")
    red_leida = leer_redsocial(red.id_red_social)
    print(f"Red social después de actualizar: {red_leida}")

    # Eliminar red social
    eliminado = eliminar_redsocial(red.id_red_social)
    print(f"Red social eliminada: {eliminado}")
    red_leida = leer_redsocial(red.id_red_social)
    print(f"Red social después de eliminar: {red_leida}")

if __name__ == "__main__":
    test_crud_redsocial()
